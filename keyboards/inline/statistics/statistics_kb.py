from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


statistics_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🔄 Обновить статистику", callback_data="statistics:_:update_stat")
        ],
    ]
)