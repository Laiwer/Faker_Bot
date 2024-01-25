from aiogram.filters.callback_data import CallbackData


class GeolocationData(CallbackData, prefix="geolocation_data"):
    category: str
    data: str
    back: bool