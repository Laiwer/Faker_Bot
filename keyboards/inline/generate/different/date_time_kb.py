from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_to_datetime_category_button = InlineKeyboardButton("⏪ Назад", callback_data="back_to_datetime_category")


datetime_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📅 Промежуток времени", callback_data="datetime_dating")
        ],
        [
            InlineKeyboardButton("🗓 Даты", callback_data="datetime_dates")
        ],
        [
            InlineKeyboardButton("⏰ Время", callback_data="datetime_times")
        ],
    ]
)


datetime_dating_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("☀️ День месяца", callback_data="datetime:dating:day_month")
        ],
        [
            InlineKeyboardButton("📰 День недели", callback_data="datetime:dating:day_week")
        ],
        [
            InlineKeyboardButton("🗓 Номер месяца", callback_data="datetime:dating:num_month")
        ],
        [
            InlineKeyboardButton("📅 Название месяца", callback_data="datetime:dating:name_month")
        ],
        [
            InlineKeyboardButton("🌏 Год", callback_data="datetime:dating:year")
        ],
        [
            InlineKeyboardButton("⚱️ Век", callback_data="datetime:dating:centure")
        ],
        [
            back_to_datetime_category_button
        ]
    ]
)


datetime_dates_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("👶 Дата рождения", callback_data="datetime:dates:birthday")
        ],
        [
            InlineKeyboardButton("🗒 Случайная дата", callback_data="datetime:dates:random_date")
        ],
        [
            InlineKeyboardButton("📅 Дата в этом месяце", callback_data="datetime:dates:date_month")
        ],
        [
            InlineKeyboardButton("🌍 Дата в этом году", callback_data="datetime:dates:date_year")
        ],
        [
            InlineKeyboardButton("💫 Дата в этом десятилетии", callback_data="datetime:dates:date_decade")
        ],
        [
            InlineKeyboardButton("🏺 Дата в этом веке", callback_data="datetime:dates:date_centure")
        ],
        [
            InlineKeyboardButton("🔮 Будущая дата", callback_data="datetime:dates:future_date")
        ],
        [
            back_to_datetime_category_button
        ]
    ]
)


datetime_times_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🕓 Время", callback_data="datetime:times:time_24")
        ],
        [
            InlineKeyboardButton("✈️ Часовые зоны", callback_data="datetime:times:time_zone")
        ],
        [
            back_to_datetime_category_button
        ]
    ]
)