from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def bank_card_category_keyboard():
    return template_generate_inline_kb(
        {
            "💳 Банковская карта": GenerateData(type="bank_card", category="-", data="card_bank", back=False),
            "💰 Платёжная система": GenerateData(type="bank_card", category="-", data="pay_system", back=False),
            "🏦 Банк": GenerateData(type="bank_card", category="-", data="name_bank", back=False),
            "🔢 Номер карты": GenerateData(type="bank_card", category="-", data="id_card", back=False),
            "🗓 Дата карты": GenerateData(type="bank_card", category="-", data="date_card", back=False),
            "🤫 Код безопасности": GenerateData(type="bank_card", category="-", data="cvv", back=False)
        }
    )