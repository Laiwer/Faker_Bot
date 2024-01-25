from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def transport_category_keyboard():
    return template_generate_inline_kb(
        {
            "🚏 Номерной знак": GenerateData(type="transport", category="-", data="license_plate", back=False),
            "🚕 ВИН-номер": GenerateData(type="transport", category="-", data="vin_number", back=False)
        }
    )