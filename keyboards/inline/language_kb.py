from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


language_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👅 Язык", callback_data="language_language")
        ]
    ]
)