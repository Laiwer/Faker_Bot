from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


company_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📰 Название компании", callback_data="company:_:name_company")
        ],
        [
            InlineKeyboardButton("💸 Слоган компании", callback_data="company:_:catch_phrase")
        ],
        [
            InlineKeyboardButton("🧰 Деятельность компании", callback_data="company:_:activity_company")
        ],
    ]
)