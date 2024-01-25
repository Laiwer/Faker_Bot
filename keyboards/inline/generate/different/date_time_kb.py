from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.template_generate import template_generate_inline_kb


back_to_datetime_category_data = {"⏪ Назад": GenerateData(type="datetime", category="-", data="-", back=True)}


def datetime_category_keyboard():
    return template_generate_inline_kb(
        {
            "📅 Промежуток времени": GenerateCategory(type="datetime", category="dating"),
            "🗓 Даты": GenerateCategory(type="datetime", category="dates"),
            "⏰ Время": GenerateCategory(type="datetime", category="times"),
        }
    )


def datetime_dating_category_keyboard():
    return template_generate_inline_kb(
        {
            "☀️ День месяца": GenerateData(type="datetime", category="dating", data="day_month", back=False),
            "📰 День недели": GenerateData(type="datetime", category="dating", data="day_week", back=False),
            "🗓 Номер месяца": GenerateData(type="datetime", category="dating", data="num_month", back=False),
            "📅 Название месяца": GenerateData(type="datetime", category="dating", data="name_month", back=False),
            "🌏 Год": GenerateData(type="datetime", category="dating", data="year", back=False),
            "⚱️ Век": GenerateData(type="datetime", category="dating", data="centure", back=False),
            **back_to_datetime_category_data
        }
    )


def datetime_dates_category_keyboard():
    return template_generate_inline_kb(
        {
            "👶 Дата рождения": GenerateData(type="datetime", category="dates", data="birthday", back=False),
            "🗒 Случайная дата": GenerateData(type="datetime", category="dates", data="random_date", back=False),
            "📅 Дата в этом месяце": GenerateData(type="datetime", category="dates", data="date_month", back=False),
            "🌍 Дата в этом году": GenerateData(type="datetime", category="dates", data="date_year", back=False),
            "💫 Дата в этом десятилетии": GenerateData(type="datetime", category="dates", data="date_decade", back=False),
            "🏺 Дата в этом веке": GenerateData(type="datetime", category="dates", data="date_centure", back=False),
            "🔮 Будущая дата": GenerateData(type="datetime", category="dates", data="future_date", back=False),
            **back_to_datetime_category_data
        }
    )


def datetime_times_category_keyboard():
    return template_generate_inline_kb(
        {
            "🕓 Время": GenerateData(type="datetime", category="times", data="time_24", back=False),
            "✈️ Часовые зоны": GenerateData(type="datetime", category="times", data="time_zone", back=False),
            **back_to_datetime_category_data
        }
    )