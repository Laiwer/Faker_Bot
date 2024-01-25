from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def person_category_keyboard():
    return template_generate_inline_kb(
        {
            "👱‍♂️ Профиль": GenerateData(type="person", category="-", data="profile", back=False),
            "👶 Упрощённый профиль": GenerateData(type="person", category="-", data="simple_prof", back=False)
        }
    )