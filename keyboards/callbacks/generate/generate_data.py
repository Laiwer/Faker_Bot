from aiogram.filters.callback_data import CallbackData


class GenerateData(CallbackData, prefix="generate_data"):
    type: str
    category: str
    data: str
    back: bool