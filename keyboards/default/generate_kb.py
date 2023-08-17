from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


back_to_main_menu_button_keyboard = KeyboardButton(text="◀ Вернутся к категориям")

generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Личность"),
            KeyboardButton(text="💰 Экономика")
        ],
        [
            # KeyboardButton(text="🤖 Технологии"),
            KeyboardButton(text="🪄 Развлечения"),
            KeyboardButton(text="⛓ Разное")
        ],
        # [
        #     KeyboardButton(text="⛓ Разное")
        # ],
        [
            KeyboardButton(text="⏪ Вернуться на главную")
        ]
    ],
    resize_keyboard=True
)

personality_generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🪪 ФИО"),
            KeyboardButton(text="👅 Язык"),
        ],
        [
            KeyboardButton(text="🧑 Человек"),
            KeyboardButton(text="☎️ Номер телефона"),
        ],
        [
            back_to_main_menu_button_keyboard
        ]
    ],
    resize_keyboard=True
)

economy_generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Банковская карта"),
            KeyboardButton(text="🏢 Компания"),
        ],
        [
            KeyboardButton(text="💵 Валюты"),
            KeyboardButton(text="🛠 Профессия"),
        ],
        [
            back_to_main_menu_button_keyboard
        ]
    ],
    resize_keyboard=True
)

technology_generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💾 Файл"),
            KeyboardButton(text="✉️ Почта"),
        ],
        [
            KeyboardButton(text="📡 Интернет"),
            KeyboardButton(text="🔐 Токен системы"),
        ],
        [
            back_to_main_menu_button_keyboard
        ]
    ],
    resize_keyboard=True
)

fun_generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎭 Эмодзи"),
            KeyboardButton(text="🎨 Цвет"),
        ],
        [
            back_to_main_menu_button_keyboard
        ]
    ],
    resize_keyboard=True
)

different_generate_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗺 Расположение"),
            KeyboardButton(text="📅 Дата и время"),
        ],
        [
            KeyboardButton(text="🚗 Транспорт"),
            KeyboardButton(text="📖 Текст"),
        ],
        [
            back_to_main_menu_button_keyboard
        ]
    ],
    resize_keyboard=True
)