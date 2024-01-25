from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.person.number_phone_kb import number_phone_category_keyboard


router = Router()


@router.message(F.text == "☎️ Номер телефона")
async def main_number_phone(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=number_phone_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "number_phone"))
async def number_phone_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_number_phone = {
        "code_phone": f"<b><i>Код телефоного номера страны:</i></b>\n<code>{fake.country_calling_code()}</code>",
        "msisdn": f"<b><i>MSISDN (<a href='https://ru.wikipedia.org/wiki/MSISDN'>Википедия</a>):</i></b>\n<code>{fake.msisdn()}</code>",
        "num_phone": f"<b><i>Номер телефона (Россия):</i></b>\n<code>{fake.phone_number()}</code>",
    }
    msg = ""
    for i in test_number_phone:
        if i in call.data:
            msg += test_number_phone[i]
    await call.message.edit_text(msg, reply_markup=number_phone_category_keyboard(), disable_web_page_preview=True)