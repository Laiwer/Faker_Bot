from keyboards.callbacks.geolocation.geolocation_category import GeolocationCategory
from keyboards.callbacks.geolocation.geolocation_data import GeolocationData
from aiogram.utils.keyboard import InlineKeyboardBuilder


def template_geolocation_inline_kb(buttons: dict):
    keyboard_builder = InlineKeyboardBuilder()
    for button in buttons:
        keyboard_builder.button(text=button, callback_data=buttons[button])
    keyboard_builder.adjust(1, repeat=True)
    return keyboard_builder.as_markup()


def geolocation_choice():
    return template_geolocation_inline_kb(
        {
            "🗿 Объекты и адреса": GeolocationCategory(category="obj_address"),
            "🧮 Координаты": GeolocationData(category="obj_address", data="coordinate", back=False),
            "📍 Геопозиция": GeolocationData(category="obj_address", data="point", back=False)
        }
    )


def geolocation_address_choice():
    return template_geolocation_inline_kb(
        {
            "🌏 Любой адрес или объект": GeolocationData(category="obj_address", data="adddress", back=False),
            "🏙 Название города": GeolocationData(category="obj_address", data="city", back=False),
            "🏳️ Название страны": GeolocationData(category="obj_address", data="country", back=False),
            "📫 Почтовый индекс": GeolocationData(category="obj_address", data="postalcode", back=False),
            "⬅ Назад": GeolocationData(category="obj_address", data="-", back=True)
        }
    )