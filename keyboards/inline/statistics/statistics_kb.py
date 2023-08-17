from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


statistics_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🧑‍💻 Всего пользователей", callback_data="statistics:_:all_users")
        ],
        [
            InlineKeyboardButton("⏳ Пользователи за час", callback_data="statistics:_:hour_users")
        ],
        [
            InlineKeyboardButton("📆 Пользователи за 24 часа", callback_data="statistics:_:day_users")
        ],
        [
            InlineKeyboardButton("⏰ Использование бота", callback_data="statistics:_:time_bots")
        ],
    ]
)