from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.technology.token_system_kb import token_sys_category_keyboard, token_sys_os_category_keyboard, token_sys_browser_category_keyboard


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "🔐 Токен системы")
async def main_token_sys(message: types.Message):
    await message.answer(choice_msg, reply_markup=token_sys_category_keyboard())


@router.callback_query(GenerateCategory.filter(F.type == "token_sys"))
async def token_sys_category(call: types.CallbackQuery, callback_data: GenerateCategory):
    await call.answer()
    if callback_data.category == "os":
        await call.message.edit_text(choice_msg, reply_markup=token_sys_os_category_keyboard())
    elif callback_data.category == "browser":
        await call.message.edit_text(choice_msg, reply_markup=token_sys_browser_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "token_sys"))
async def token_sys_category_data(call: types.CallbackQuery, callback_data: GenerateData, fake: Faker):
    await call.answer()
    if callback_data.back:
        await call.message.edit_text(choice_msg, reply_markup=token_sys_category_keyboard())
        return
    elif callback_data.category == "os":
        test_token_sys = {
            "android": f"<b><i>Токен Android:</i></b>\n<code>{fake.android_platform_token()}</code>",
            "ios": f"<b><i>Токен IOS:</i></b>\n<code>{fake.ios_platform_token()}</code>",
            "windows": f"<b><i>Токен Windows:</i></b>\n<code>{fake.windows_platform_token()}</code>",
            "linux": f"<b><i>Токен Linux:</i></b>\n<code>{fake.linux_platform_token()}</code>",
            "macos": f"<b><i>Токен MacOS:</i></b>\n<code>{fake.mac_platform_token()}</code>",
        }
        keyboard = token_sys_os_category_keyboard()
    elif callback_data.category == "browser":
        test_token_sys = {
            "u_a": f"<b><i>User-Agent:</i></b>\n<code>{fake.user_agent()}</code>",
            "ua_ch": f"<b><i>User-Agent (Chrome):</i></b>\n<code>{fake.chrome()}</code>",
            "ua_sf": f"<b><i>User-Agent (Safari):</i></b>\n<code>{fake.safari()}</code>",
            "ua_ff": f"<b><i>User-Agent (Firefox):</i></b>\n<code>{fake.firefox()}</code>",
            "ua_op": f"<b><i>User-Agent (Opera):</i></b>\n<code>{fake.opera()}</code>",
            "ua_ie": f"<b><i>User-Agent (Internet Explorer):</i></b>\n<code>{fake.internet_explorer()}</code>",
        }
        keyboard = token_sys_browser_category_keyboard()
    msg = ""
    for i in test_token_sys:
        if i in call.data:
            msg += test_token_sys[i]
    await call.message.edit_text(msg, reply_markup=keyboard)