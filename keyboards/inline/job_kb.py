from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


job_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🛠 Профессия", callback_data="job_job")
        ]
    ]
)