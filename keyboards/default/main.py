from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎞 Сгенерировать"),
            KeyboardButton(text="🌎 Местоположение")
        ],
        [
            KeyboardButton(text="📊 Статистика"),
            KeyboardButton(text="📢 Канал с обновлениями"),
        ]
    ],
    resize_keyboard=True
)