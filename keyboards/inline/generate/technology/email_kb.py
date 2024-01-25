from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def email_category_keyboard():
    return template_generate_inline_kb(
        {
            "✉️ Личный email": GenerateData(type="email", category="-", data="personal", back=False),
            "📨 Email для бизнеса": GenerateData(type="email", category="-", data="business", back=False)
        }
    )