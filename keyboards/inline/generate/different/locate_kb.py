from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData


back_to_locate_category_button = {"⏪ Назад": GenerateData(type="locate", category="-", data="-", back=True)}


def locate_category_keyboard():
    return template_generate_inline_kb(
        {
            "🏡 Адреса": GenerateCategory(type="locate", category="address"),
            "🏞 Координаты": GenerateCategory(type="locate", category="coordinate"),
            "📍 Геометка": GenerateCategory(type="locate", category="geo"),
        }
    )


def locate_address_category_keyboard():
    return template_generate_inline_kb(
        {
            "🪧 Адрес": GenerateData(type="locate", category="add_ss", data="all_address", back=False),
            "🏠 Номер дома": GenerateData(type="locate", category="add_ss", data="number_house", back=False),
            "🏘 Адрес улицы": GenerateData(type="locate", category="add_ss", data="street_address", back=False),
            "🛤 Название улицы": GenerateData(type="locate", category="add_ss", data="street_name", back=False),
            "🏙 Город": GenerateData(type="locate", category="add_ss", data="city", back=False),
            "🇷🇺 Субъекты РФ": GenerateData(type="locate", category="add_ss", data="region", back=False),
            "📬 Почтовый индекс": GenerateData(type="locate", category="add_ss", data="post_index", back=False),
            **back_to_locate_category_button
        }
    )


def locate_coordinate_category_keyboard():
    return template_generate_inline_kb(
        {
            "↔️ Долгота": GenerateData(type="locate", category="coord_s", data="longitude", back=False),
            "↕️ Широта": GenerateData(type="locate", category="coord_s", data="latitude", back=False),
            "🎛 Случайные координаты": GenerateData(type="locate", category="coord_s", data="random_coord", back=False),
            "🇺🇳 Страна": GenerateData(type="locate", category="coord_s", data="name_country", back=False),
            **back_to_locate_category_button
        }
    )


def locate_geo_category_keyboard():
    return template_generate_inline_kb(
        {
            "🇷🇺 Случайная точка России": GenerateData(type="locate", category="geo_pos", data="random_russia", back=False),
            "🌎 Случайная точка в мире": GenerateData(type="locate", category="geo_pos", data="random_world", back=False),
            **back_to_locate_category_button
        }
    )