from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


company_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📰 Название маленькой компании", callback_data="company:_:name_company")
        ],
        [
            InlineKeyboardButton("🏢 Название крупной компании", callback_data="company:_:large_company")
        ],
        [
            InlineKeyboardButton("💸 Слоган компании", callback_data="company:_:catch_phrase")
        ],
        [
            InlineKeyboardButton("🧰 Деятельность компании", callback_data="company:_:activity_company")
        ],
        [
            InlineKeyboardButton("🎫 ИНН", callback_data="company:_:inn")
        ],
        [
            InlineKeyboardButton("📜 ОГРН", callback_data="company:_:ogrn")
        ],
    ]
)