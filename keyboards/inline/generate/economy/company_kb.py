from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def company_category_keyboard():
    return template_generate_inline_kb(
        {
            "📰 Название маленькой компании": GenerateData(type="company", category="-", data="name_company", back=False),
            "🏢 Название крупной компании": GenerateData(type="company", category="-", data="large_company", back=False),
            "💸 Слоган компании": GenerateData(type="company", category="-", data="catch_phrase", back=False),
            "🧰 Деятельность компании": GenerateData(type="company", category="-", data="activity_company", back=False),
            "🎫 ИНН": GenerateData(type="company", category="-", data="inn", back=False),
            "📜 ОГРН": GenerateData(type="company", category="-", data="ogrn", back=False)
        }
    )