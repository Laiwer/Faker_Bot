from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🪪 ФИО"),
            KeyboardButton(text="🗺 Расположение"),
        ],
        [
            KeyboardButton(text="📅 Дата и время"),
            KeyboardButton(text="💳 Банковская карта"),
        ],
        [
            KeyboardButton(text="🏢 Компания"),
            KeyboardButton(text="💵 Валюты"),
        ],
        [
            KeyboardButton(text="🛠 Профессия"),
            KeyboardButton(text="🚗 Транспорт"),
        ],
        [
            KeyboardButton(text="👅 Язык"),
            KeyboardButton(text="🎭 Эмодзи"),
        ],
        [
            KeyboardButton(text="⏪ Вернуться на главную")
        ]
    ],
    resize_keyboard=True
)