from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.person.fio_kb import fio_category_keyboard, fio_male_category_keyboard, fio_female_category_keyboard


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "🪪 ФИО")
async def main_fio(message: types.Message):
    await message.answer(choice_msg, reply_markup=fio_category_keyboard())


@router.callback_query(GenerateCategory.filter(F.type == "fio"))
async def fio_category(call: types.CallbackQuery, callback_data: GenerateCategory):
    await call.answer()
    if callback_data.category == "male":
        await call.message.edit_text(choice_msg, reply_markup=fio_male_category_keyboard())
    elif callback_data.category == "female":
        await call.message.edit_text(choice_msg, reply_markup=fio_female_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "fio"))
async def fio_category_data(call: types.CallbackQuery, callback_data: GenerateData, fake: Faker):
    await call.answer()
    if callback_data.back:
        await call.message.edit_text(choice_msg, reply_markup=fio_category_keyboard())
        return
    elif callback_data.category == "male":
        test_fio = {
            "fio_person": f"<b><i>Мужское Ф.И.О.:</i></b>\n<code>{fake.name_male()}</code>",
            "first_name": f"<b><i>Мужское имя:</i></b>\n<code>{fake.first_name_male()}</code>",
            "middle_name": f"<b><i>Мужская фамилия:</i></b>\n<code>{fake.last_name_male()}</code>",
            "last_name": f"<b><i>Мужское отчество:</i></b>\n<code>{fake.middle_name_male()}</code>"
        }
        keyboard = fio_male_category_keyboard()
    elif callback_data.category == "female":
        test_fio = {
            "fio_person": f"<b><i>Женское Ф.И.О.:</i></b>\n<code>{fake.name_female()}</code>",
            "first_name": f"<b><i>Женское имя:</i></b>\n<code>{fake.first_name_female()}</code>",
            "middle_name": f"<b><i>Женская фамилия:</i></b>\n<code>{fake.last_name_female()}</code>",
            "last_name": f"<b><i>Женское отчество:</i></b>\n<code>{fake.middle_name_female()}</code>"
        }
        keyboard = fio_female_category_keyboard()
    msg = ""
    for i in test_fio:
        if i in call.data:
            msg += test_fio[i]
    await call.message.edit_text(msg, reply_markup=keyboard)