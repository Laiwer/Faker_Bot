from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


number_phone_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🚩 Код страны", callback_data="number_phone:_:code_phone")
        ],
        [
            InlineKeyboardButton("📺 MSISDN", callback_data="number_phone:_:msisdn")
        ],
        [
            InlineKeyboardButton("📞 Номер телефона", callback_data="number_phone:_:num_phone")
        ],
    ]
)