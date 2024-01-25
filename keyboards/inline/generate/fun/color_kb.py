from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def color_category_keyboard():
    return template_generate_inline_kb(
        {
            "🌈 Название цвета": GenerateData(type="color", category="-", data="name_color", back=False),
            "👾 Цвет палитры HEX": GenerateData(type="color", category="-", data="hex_color", back=False),
            "🔹 Цвет палитры RGB": GenerateData(type="color", category="-", data="rgb_color", back=False),
            "🔶 Цвет палитры CSS RGB": GenerateData(type="color", category="-", data="rgb_css_color", back=False)
        }
    )