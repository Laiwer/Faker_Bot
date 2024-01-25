from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.person.language_kb import language_category_keyboard


router = Router()


@router.message(F.text == "👅 Язык")
async def main_language(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=language_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "language"))
async def bank_card_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_language = {
        "names": f"<b><i>Случайный язык:</i></b>\n<code>{fake.language_name()}</code>",
        "codes": f"<b><i>Код языка:</i></b>\n<code>{fake.language_code().upper()}</code>",
    }
    msg = ""
    for i in test_language:
        if i in call.data:
            msg += test_language[i]
    await call.message.edit_text(msg, reply_markup=language_category_keyboard())