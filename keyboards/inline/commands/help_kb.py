from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


all_generate_menu_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Весь \"🎞 Сгенерировать\"", callback_data="all_generate_menu_1")
        ],
    ]
)

instruction_help_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣ стр.", callback_data="all_generate_menu_1"),
            InlineKeyboardButton(text="2️⃣ стр.", callback_data="all_generate_menu_2"),
        ],
        [
            InlineKeyboardButton(text="3️⃣ стр.", callback_data="all_generate_menu_3"),
            InlineKeyboardButton(text="4️⃣ стр.", callback_data="all_generate_menu_4"),
        ],
        [
            InlineKeyboardButton(text="🤖 Инструкция пользования ботом", callback_data="instruction_help")
        ],
    ]
)