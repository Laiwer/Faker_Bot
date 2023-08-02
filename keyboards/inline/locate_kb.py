from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_to_locate_category_button = InlineKeyboardButton("⏪ Назад", callback_data="back_to_locate_category")

locate_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🏡 Адреса", callback_data="locate_address_category")
        ],
        [
            InlineKeyboardButton("🏞 Координаты", callback_data="locate_coordinate_category")
        ],
        [
            InlineKeyboardButton("📍 Геометка", callback_data="locate_geo_category")
        ]
    ]
)

locate_address_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🪧 Адрес", callback_data="locate:add_ss:all_address")
        ],
        [
            InlineKeyboardButton("🏠 Номер дома", callback_data="locate:add_ss:number_house")
        ],
        [
            InlineKeyboardButton("🏘 Адрес улицы", callback_data="locate:add_ss:street_address")
        ],
        [
            InlineKeyboardButton("🛤 Название улицы", callback_data="locate:add_ss:street_name")
        ],
        [
            InlineKeyboardButton("🏙 Город", callback_data="locate:add_ss:city")
        ],
        [
            InlineKeyboardButton("📬 Почтовый индекс", callback_data="locate:add_ss:post_index")
        ],
        [
            back_to_locate_category_button
        ]
    ]
)

locate_coordinate_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("↔️ Долгота", callback_data="locate:coord_s:longitude")
        ],
        [
            InlineKeyboardButton("↕️ Широта", callback_data="locate:coord_s:latitude")
        ],
        [
            InlineKeyboardButton("🎛 Случайные координаты", callback_data="locate:coord_s:random_coord")
        ],
        [
            InlineKeyboardButton("🇺🇳 Страна", callback_data="locate:coord_s:name_country")
        ],
        [
            back_to_locate_category_button
        ]
    ]
)

locate_geo_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🇷🇺 Случайная точка России", callback_data="locate:geo_pos:random_russia")
        ],
        [
            InlineKeyboardButton("🌎 Случайная точка в мире", callback_data="locate:geo_pos:random_world")
        ],
        [
            back_to_locate_category_button
        ]
    ]
)