from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def language_category_keyboard():
    return template_generate_inline_kb(
        {
            "👅 Язык": GenerateData(type="language", category="-", data="names", back=False),
            "⌨️ Код языка": GenerateData(type="language", category="-", data="codes", back=False)
        }
    )