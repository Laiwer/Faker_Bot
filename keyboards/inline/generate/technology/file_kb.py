from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def file_category_keyboard():
    return template_generate_inline_kb(
        {
            "📁 Файл": GenerateData(type="file", category="-", data="name", back=False),
            "🔗 Расширение файла": GenerateData(type="file", category="-", data="expansion", back=False),
            "🗂 Путь к файлу": GenerateData(type="file", category="-", data="path", back=False),
        }
    )