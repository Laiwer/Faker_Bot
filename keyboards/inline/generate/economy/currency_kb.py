from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData


back_to_currency_category_button = {"⏪ Назад": GenerateData(type="currency", category="-", data="-", back=True)}


def currency_category_keyboard():
    return template_generate_inline_kb(
        {
            "💶 Денежная валюта": GenerateCategory(type="currency", category="paper"),
            "📀 Криптовалюта": GenerateCategory(type="currency", category="crypto")
        }
    )


def currency_paper_category_keyboard():
    return template_generate_inline_kb(
        {
            "💵 Валюта": GenerateData(type="currency", category="paper", data="all", back=False),
            "🪙 Название валюты": GenerateData(type="currency", category="paper", data="name_currency", back=False),
            "📟 Код валюты": GenerateData(type="currency", category="paper", data="id_currency", back=False),
            "💠 Символ валюты": GenerateData(type="currency", category="paper", data="symbol_currency", back=False),
            "📶 Кол-во денег": GenerateData(type="currency", category="paper", data="number_paper", back=False),
            **back_to_currency_category_button
        }
    )


def currency_crypto_category_keyboard():
    return template_generate_inline_kb(
        {
            "💿 Криптовалюта": GenerateData(type="currency", category="crypto", data="all", back=False),
            "⚙️ Название криптовалюты": GenerateData(type="currency", category="crypto", data="name_currency", back=False),
            "📟 Код криптовалюты": GenerateData(type="currency", category="crypto", data="id_currency", back=False),
            **back_to_currency_category_button
        }
    )