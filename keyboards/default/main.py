from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🎞 Сгенерировать"),
            KeyboardButton("🌎 Местоположение")
        ],
        [
            KeyboardButton("📊 Статистика"),
        ]
    ],
    resize_keyboard=True
)