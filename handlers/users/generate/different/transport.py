from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.different.transport_kb import transport_category_keyboard


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "🚗 Транспорт")
async def main_transport(message: types.Message):
    await message.answer(choice_msg, reply_markup=transport_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "transport"))
async def transport_category_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_transport = {
            "license_plate": f"<b><i>Номерной знак (включая специальные номера):</i></b>\n<code>{fake.license_plate()}</code>",
            "vin_number": f"<b><i>ВИН-номер (идентификатор):</i></b>\n<code>{fake.vin()}</code>"
        }
    msg = ""
    for i in test_transport:
        if i in call.data:
            msg += test_transport[i]
    await call.message.edit_text(msg, reply_markup=transport_category_keyboard())