from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData


back_to_token_sys_category_button = {"⏪ Назад": GenerateData(type="token_sys", category="-", data="-", back=True)}


def token_sys_category_keyboard():
    return template_generate_inline_kb(
        {
            "📲 Операционная система": GenerateCategory(type="token_sys", category="os"),
            "🛰 Браузер": GenerateCategory(type="token_sys", category="browser")
        }
    )


def token_sys_os_category_keyboard():
    return template_generate_inline_kb(
        {
            "🦖 Токен Android": GenerateData(type="token_sys", category="os", data="android", back=False),
            "🍏 Токен IOS": GenerateData(type="token_sys", category="os", data="ios", back=False),
            "🌃 Токен Windows": GenerateData(type="token_sys", category="os", data="windows", back=False),
            "🐧 Токен Linux": GenerateData(type="token_sys", category="os", data="linux", back=False),
            "🖥 Токен MacOS": GenerateData(type="token_sys", category="os", data="macos", back=False),
            **back_to_token_sys_category_button
        }
    )


def token_sys_browser_category_keyboard():
    return template_generate_inline_kb(
        {
            "😎 User-Agent": GenerateData(type="token_sys", category="browser", data="u_a", back=False),
            "🧬 User-Agent (Chrome)": GenerateData(type="token_sys", category="browser", data="ua_ch", back=False),
            "🧭 User-Agent (Safari)": GenerateData(type="token_sys", category="browser", data="ua_sf", back=False),
            "🦊 User-Agent (Firefox)": GenerateData(type="token_sys", category="browser", data="ua_ff", back=False),
            "🛟 User-Agent (Opera)": GenerateData(type="token_sys", category="browser", data="ua_op", back=False),
            "🕸 User-Agent (Internet Explorer)": GenerateData(type="token_sys", category="browser", data="ua_ie", back=False),
            **back_to_token_sys_category_button
        }
    )