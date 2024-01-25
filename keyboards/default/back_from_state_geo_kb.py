from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


back_to_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏪ Вернуться")
        ]
    ],
    resize_keyboard=True
)