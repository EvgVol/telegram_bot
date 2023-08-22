from decouple import config

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes


TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')


def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton('Фото из старшей школы', callback_data='school'),
            InlineKeyboardButton('Последнее селфи', callback_data='selfie'),
            InlineKeyboardButton('Пост про увлечения', callback_data='hobby'),
            InlineKeyboardButton('Разницу между SQL и NoSQL', callback_data='difference'),
            InlineKeyboardButton('Что ещё умею', callback_data='more'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.data == 'selfie':
        photo_url = 'https://cdn2.thecatapi.com/images/3dl.jpg'
        return query.message.reply_photo(photo_url)
    if query.data == 'school':
        photo_url = 'https://cdn2.thecatapi.com/images/3dl.jpg'
        return query.message.reply_photo(photo_url)
    elif query.data == 'hobby':
        hobby_post = 'Здесь можно добавить информацию о вашем увлечении, пост или ссылку на ваш сайт.'
        return query.message.reply_text(hobby_post)
    elif query.data == 'difference':
        difference_info = 'Здесь нужно добавить информацию про разницу между SQL и NoSQL'
        return query.message.reply_text(difference_info)
    elif query.data == 'more':
        more_info = 'Я умею отвечать на вопросы:\n что ты умеешь?\n кто ты?\n кто твой владелец?\n что такое gpt?\n'
        return query.message.reply_text(more_info)

    return query.answer()


def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = get_main_menu_keyboard()
    message = f'Привет, {update.effective_user.first_name}! Что вам показать?'
    return update.message.reply_text(message, reply_markup=reply_markup)


def what_can_you_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = get_main_menu_keyboard()
    message_text = '''Привет! Вот список того, что я могу предложить:
    - Показать последнее селфи моего хозяина;
    - Показать фото из старшей школы;
    - Показать пост про его увлечения;
    - Вывести ссылку на мой код;
    - Моороткогу ко объяснить разницу между SQL и NoSQL;
    - Расскажу (по секрету) тайную историю первой любви моего хозяина;
    - Могу ответить на несколько вопросов;
    - Дам ссылочку на резюме моего хозяина.
    '''
    return update.message.reply_text(message_text, reply_markup=reply_markup)  


def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if 'что ты умеешь?' in text:
        return what_can_you_do(update, context)
    elif 'кто ты?' in text:
        about_bot = 'Я - Телеграм-бот. Моя задача состоит в том, чтобы предоставлять информацию пользователю и взаимодействовать с ним.'
        return update.message.reply_text(about_bot)
    elif 'что такое gpt?' in text:
        about_gpt = 'Тут должна информация про то, что такое чат GPT'
        return update.message.reply_text(about_gpt)
    elif 'кто твой владелец?' in text:
        owner_info = 'Мой владелец: Евгений Волочек.\nКонтакты:\n- Телеграм: @ESVolochek\n- Email: volohek93@yandex.ru'
        return update.message.reply_text(owner_info)
    else:
        return update.message.reply_text('Извините, я не понимаю ваш вопрос. Попробуйте задать другой вопрос.')


def story(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    secret_history = 'Тут должна быть тайная история первой любви'
    return update.message.reply_text(secret_history)


def resume(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    resume_url = 'https://hh.ru/resume_converter/Волочек%20Евгений%20Сергеевич.pdf?hash=ca1334ccff0b2b8e230039ed1f584467354567&type=pdf&hhtmSource=resume&hhtmFrom=resume_list'
    return update.message.reply_text(f'Ссылка на резюме: {resume_url}')


def code(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    code_url = 'https://github.com/EvgVol/test_mentor'
    return update.message.reply_text(f'Ссылка на GitHub: {code_url}')


bot = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CommandHandler("story", story))
bot.add_handler(CommandHandler("resume", resume))
bot.add_handler(CommandHandler("code", code))
bot.add_handler(CommandHandler("menu", what_can_you_do))
bot.add_handler(CallbackQueryHandler(handle_button_click))
bot.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND, text_handler))

bot.run_polling()
