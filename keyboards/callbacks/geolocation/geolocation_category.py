from aiogram.filters.callback_data import CallbackData


class GeolocationCategory(CallbackData, prefix="geolocation_category"):
    category: str