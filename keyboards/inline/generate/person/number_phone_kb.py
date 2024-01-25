from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def number_phone_category_keyboard():
    return template_generate_inline_kb(
        {
            "🚩 Код страны": GenerateData(type="number_phone", category="-", data="code_phone", back=False),
            "📺 MSISDN": GenerateData(type="number_phone", category="-", data="msisdn", back=False),
            "📞 Номер телефона": GenerateData(type="number_phone", category="-", data="num_phone", back=False)
        }
    )