import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ChatAction
from telegram.ext import (ApplicationBuilder, CommandHandler,
                          CallbackQueryHandler, MessageHandler,
                          filters, ContextTypes)
from gtts import gTTS
from tempfile import NamedTemporaryFile

from database import get_message_text_from_db
from settings import TELEGRAM_TOKEN


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton('Фото из старшей школы',
                              callback_data='school')],
        [InlineKeyboardButton('Последнее селфи',
                              callback_data='selfie')],
        [InlineKeyboardButton('Пост про увлечения',
                              callback_data='hobby')],
        [InlineKeyboardButton('Историю первой любви',
                              callback_data='story')],
        [InlineKeyboardButton('Разницу между SQL и NoSQL',
                              callback_data='difference')],
        [InlineKeyboardButton('Пришлю ссылку на резюме',
                              callback_data='resume')],
        [InlineKeyboardButton('Что ещё умею',
                              callback_data='more')],
    ]
    return InlineKeyboardMarkup(keyboard)


async def handle_button_click(update: Update,
                              context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    data_to_reply_function = {
        'selfie': query.message.reply_photo,
        'school': query.message.reply_photo,
    }
    message = get_message_text_from_db(query.data)

    if query.data in data_to_reply_function:
        reply_function = data_to_reply_function[query.data]
        await reply_function(message)
    else:
        await query.message.reply_text(message)

    await query.answer()


def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = get_main_menu_keyboard()
    message = get_message_text_from_db(
        'start'
    ).format(name=update.effective_user.first_name)
    return update.message.reply_text(message, reply_markup=reply_markup)


def what_can_you_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = get_main_menu_keyboard()
    message = get_message_text_from_db('what_can_you_do')
    return update.message.reply_text(message, reply_markup=reply_markup)  


async def send_voice_message(update: Update,
                             context: ContextTypes.DEFAULT_TYPE,
                             text: str):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id,
                                       action=ChatAction.RECORD_VOICE)
    tts = gTTS(text, lang='ru')
    with NamedTemporaryFile(suffix=".ogg", delete=False) as audio_file:
        audio_file_name = audio_file.name
        tts.save(audio_file_name)
        audio_file.close()
        with open(audio_file_name, 'rb') as f:
            await update.message.reply_voice(f)
        os.remove(audio_file_name)


def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    actions = {
        'что ты умеешь?': what_can_you_do,
        'кто ты?': 'who_are_you',
        'что такое gpt?': 'about_gpt',
        'кто твой владелец?': 'whose_are_you',
    }

    action = actions.get(text, 'error')
    if callable(action):
        return action(update, context)
    else:
        message = get_message_text_from_db(action)

        if action == 'about_gpt':
            return send_voice_message(update, context, message)
        else:
            return update.message.reply_text(message)


def code(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://github.com/EvgVol/test_mentor'
    return update.message.reply_text(f"Исходный код на GitHub: {url}")


bot = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CommandHandler("code", code))
bot.add_handler(CommandHandler("menu", what_can_you_do))
bot.add_handler(CallbackQueryHandler(handle_button_click))
bot.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND,
                               text_handler))

bot.run_polling()
