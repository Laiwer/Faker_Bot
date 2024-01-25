from aiogram import types, Router
from keyboards.default.generate_kb import generate_keyboard
from aiogram.filters.command import Command


router = Router()


@router.message(Command("generate"))
async def generate(message: types.Message):
    await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)
