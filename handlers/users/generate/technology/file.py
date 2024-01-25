from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.technology.file_kb import file_category_keyboard
from random import randint


router = Router()


@router.message(F.text == "💾 Файл")
async def main_file(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=file_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "file"))
async def file_data(call: types.CallbackQuery):
    fake = Faker()
    await call.answer()
    test_file = {
        "name": f"<b><i>Имя файла:</i></b>\n<code>{fake.file_name()}</code>",
        "expansion": f"<b><i>Расширение файла:</i></b>\n<code>{fake.file_extension()}</code>",
        "path": f"<b><i>Путь к файлу:</i></b>\n<code>{fake.file_path(depth=randint(1, 5))}</code>",
    }
    msg = ""
    for i in test_file:
        if i in call.data:
            msg += test_file[i]
    await call.message.edit_text(msg, reply_markup=file_category_keyboard())