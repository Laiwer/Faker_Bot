from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


transport_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🚏 Номерной знак", callback_data="transport:_:license_plate")
        ],
        [
            InlineKeyboardButton("🚕 ВИН-номер", callback_data="transport:_:vin_number")
        ]
    ]
)