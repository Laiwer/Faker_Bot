from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def job_category_keyboard():
    return template_generate_inline_kb(
        {
            "🛠 Профессия": GenerateData(type="job", category="-", data="-", back=False)
        }
    )
