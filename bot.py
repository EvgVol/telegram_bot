from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ContextTypes

import settings


async def create_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("Показать последнее селфи", callback_data="selfie"),
            InlineKeyboardButton("Показать пост про увлечении", callback_data="hobby"),
            InlineKeyboardButton("Показать ссылку на исходники", callback_data="source"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = await create_keyboard()
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!', reply_markup=reply_markup)



async def handle_button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    reply_markup = await create_keyboard()

    if query.data == "selfie":
        photo_url = 'https://cdn2.thecatapi.com/images/3dl.jpg'
        await query.message.reply_photo(photo_url, reply_markup=reply_markup)
    elif query.data == "hobby":
        hobby_post = 'Здесь можно добавить информацию о вашем увлечении, пост или ссылку на ваш сайт.'
        await query.message.reply_text(hobby_post, reply_markup=reply_markup)
    elif query.data == "source":
        post_url = 'https://github.com/EvgVol/test_mentor'
        await query.message.reply_text(f'Код бота на GitHub: {post_url}', reply_markup=reply_markup)

    await query.answer()


async def what_can_you_do(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    capabilities = """Я могу:
    - Показать последнее селфи
    - Показать пост про увлечение
    - Показать ссылку на исходники бота"""
    await update.message.reply_text(capabilities)


async def who_are_you(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    about_bot = "Я - Телеграм-бот. Моя задача состоит в том, чтобы предоставлять информацию пользователю и взаимодействовать с ним."
    await update.message.reply_text(about_bot)


async def who_is_your_owner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    owner_info = "Мой владелец: Иван Иванов.\nКонтакты:\n- Телеграм: @Ivan_Ivanov\n- Email: ivan.ivanov@example.com"
    await update.message.reply_text(owner_info)


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if "что ты умеешь?" in text:
        await what_can_you_do(update, context)
    elif "кто ты?" in text:
        await who_are_you(update, context)
    elif "кто твой владелец?" in text:
        await who_is_your_owner(update, context)
    else:
        await update.message.reply_text("Извините, я не понимаю ваш вопрос. Попробуйте задать другой вопрос.")


app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_button_click))
app.add_handler(MessageHandler(Filters.text & ~Filters.command, text_handler))

app.run_polling()
