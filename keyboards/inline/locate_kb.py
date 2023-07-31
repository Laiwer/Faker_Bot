from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


locate_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🪧 Адрес", callback_data="locate:_:all_address")
        ],
        [
            InlineKeyboardButton("🏘 Адрес улицы", callback_data="locate:_:street_address")
        ],
        [
            InlineKeyboardButton("🛤 Название улицы", callback_data="locate:_:street_name")
        ],
        [
            InlineKeyboardButton("🏙 Город", callback_data="locate:_:city")
        ],
        [
            InlineKeyboardButton("📬 Почтовый индекс", callback_data="locate:_:post_index")
        ],
        [
            InlineKeyboardButton("🌐 Страна", callback_data="locate:_:country")
        ]
    ]
)