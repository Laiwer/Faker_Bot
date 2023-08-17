from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


person_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👱‍♂️ Профиль", callback_data="person:_:profile")
        ],
        [
            InlineKeyboardButton("👶 Упрощённый профиль", callback_data="person:_:simple_prof")
        ],
    ]
)