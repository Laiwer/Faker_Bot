from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.economy.job_kb import job_category_keyboard


router = Router()


@router.message(F.text == "🛠 Профессия")
async def main_job(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=job_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "job"))
async def job_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    await call.message.edit_text(f"<b><i>Профессия:</i></b>\n<code>{fake.job()}</code>", reply_markup=job_category_keyboard())