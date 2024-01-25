from aiogram.filters.callback_data import CallbackData


class GenerateCategory(CallbackData, prefix="generate_category"):
    type: str
    category: str