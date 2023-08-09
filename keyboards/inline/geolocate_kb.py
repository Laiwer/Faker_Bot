from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


geolocation_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🗿 Объекты и адреса", callback_data="geolocate_obj_addr")
        ],
        [
            InlineKeyboardButton("🧮 Координаты", callback_data="geolocate:_:coordinate")
        ],
        [
            InlineKeyboardButton("📍 Геопозиция", callback_data="geolocate:_:point")
        ],
    ]
)

geolocation_address_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🌏 Любой адрес или объект", callback_data="geolocate:_:address")
        ],
        [
            InlineKeyboardButton("🏙 Название города", callback_data="geolocate:_:city")
        ],
        [
            InlineKeyboardButton("🏳️ Название страны", callback_data="geolocate:_:country")
        ],
        [
            InlineKeyboardButton("📫 Почтовый индекс", callback_data="geolocate:_:postalcode")
        ],
        [
            InlineKeyboardButton("⬅ Назад", callback_data="back_to_geolocation_choice")
        ]
    ]
)