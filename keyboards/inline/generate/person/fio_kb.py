from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData


back_to_fio_category_button = {"⏪ Назад": GenerateData(type="fio", category="-", data="-", back=True)}


def fio_category_keyboard():
    return template_generate_inline_kb(
        {
            "🚹 Мужское": GenerateCategory(type="fio", category="male"),
            "🚺 Женское": GenerateCategory(type="fio", category="female")
        }
    )


def fio_male_category_keyboard():
    return template_generate_inline_kb(
        {
            "🪪 Мужское Ф.И.О.": GenerateData(type="fio", category="male", data="fio_person", back=False),
            "📇 Мужское имя": GenerateData(type="fio", category="male", data="first_name", back=False),
            "👨‍👩‍👧‍👦 Мужская фамилия": GenerateData(type="fio", category="male", data="middle_name", back=False),
            "👱‍♂️ Мужское отчество": GenerateData(type="fio", category="male", data="last_name", back=False),
            **back_to_fio_category_button
        }
    )


def fio_female_category_keyboard():
    return template_generate_inline_kb(
        {
            "🪪 Женское Ф.И.О.": GenerateData(type="fio", category="female", data="fio_person", back=False),
            "📇 Женское имя": GenerateData(type="fio", category="female", data="first_name", back=False),
            "👨‍👩‍👧‍👦 Женская фамилия": GenerateData(type="fio", category="female", data="middle_name", back=False),
            "👱‍♂️ Женское отчество": GenerateData(type="fio", category="female", data="last_name", back=False),
            **back_to_fio_category_button
        }
    )