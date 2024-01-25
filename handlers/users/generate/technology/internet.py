from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.technology.internet_kb import internet_category_keyboard
from random import randint


router = Router()


@router.message(F.text == "📡 Интернет")
async def main_internet(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=internet_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "internet"))
async def internet_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_internet = {
        "domain": f"<b><i>Имя домена:</i></b>\n<code>{fake.domain_name(levels=randint(1, 3))}</code>",
        "url": f"<b><i>Случайное URL:</i></b>\n<code>{fake.url()}</code>",
        "hosting": f"<b><i>Имя хостинга:</i></b>\n<code>{fake.hostname(levels=randint(1, 3))}</code>",
        "public_v4": f"<b><i>Публичный IPv4:</i></b>\n<code>{fake.ipv4_public()}</code>",
        "private_v4": f"<b><i>Приватный IPv4:</i></b>\n<code>{fake.ipv4_private()}</code>",
        "ipv6": f"<b><i>IPv6:</i></b>\n<code>{fake.ipv6()}</code>",
        "mac": f"<b><i>MAC-адрес:</i></b>\n<code>{fake.mac_address()}</code>",
    }
    msg = ""
    for i in test_internet:
        if i in call.data:
            msg += test_internet[i]
    await call.message.edit_text(msg, reply_markup=internet_category_keyboard())