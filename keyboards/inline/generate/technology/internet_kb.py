from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_data import GenerateData


def internet_category_keyboard():
    return template_generate_inline_kb(
        {
            "🖨 Имя домена": GenerateData(type="internet", category="-", data="domain", back=False),
            "🌐 Случайное URL": GenerateData(type="internet", category="-", data="url", back=False),
            "🗄 Имя хостинга": GenerateData(type="internet", category="-", data="hosting", back=False),
            "🔓 Публичный IPv4": GenerateData(type="internet", category="-", data="public_v4", back=False),
            "🔐 Приватный IPv4": GenerateData(type="internet", category="-", data="private_v4", back=False),
            "🔏 IPv6": GenerateData(type="internet", category="-", data="ipv6", back=False),
            "🔌 MAC-адрес": GenerateData(type="internet", category="-", data="mac", back=False),
        }
    )