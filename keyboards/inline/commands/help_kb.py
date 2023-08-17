from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


all_generate_menu_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Весь \"🎞 Сгенерировать\"", callback_data="all_generate_menu")
        ],
    ]
)

instruction_help_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("1️⃣ стр.", callback_data="all_generate_menu"),
            InlineKeyboardButton("2️⃣ стр.", callback_data="all_generate_menu_2")
        ],
        [
            InlineKeyboardButton("🤖 Инструкция пользования ботом", callback_data="instruction_help")
        ],
    ]
)