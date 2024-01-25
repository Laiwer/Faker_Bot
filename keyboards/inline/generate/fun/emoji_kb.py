from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def emoji_category_keyboard():
    return template_generate_inline_kb(
        {
            "🎭 Эмодзи": GenerateData(type="emoji", category="-", data="-", back=False)
        }
    )