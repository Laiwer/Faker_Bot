from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.technology.email_kb import email_category_keyboard


router = Router()


@router.message(F.text == "✉️ Почта")
async def main_email(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=email_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "email"))
async def email_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_email = {
        "personal": f"<b><i>Личный email:</i></b>\n<code>{fake.free_email()}</code>",
        "business": f"<b><i>Email для бизнеса:</i></b>\n<code>{fake.company_email()}</code>",
    }
    msg = ""
    for i in test_email:
        if i in call.data:
            msg += test_email[i]
    await call.message.edit_text(msg, reply_markup=email_category_keyboard())