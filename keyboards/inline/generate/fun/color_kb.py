from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


color_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🌈 Название цвета", callback_data="color:_:name_color")
        ],
        [
            InlineKeyboardButton("👾 Цвет палитры HEX", callback_data="color:_:hex_color")
        ],
        [
            InlineKeyboardButton("🔹 Цвет палитры RGB", callback_data="color:_:rgb_color")
        ],
        [
            InlineKeyboardButton("🔶 Цвет палитры CSS RGB", callback_data="color:_:rgb_css_color")
        ]
    ]
)