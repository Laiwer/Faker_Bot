from aiogram import types, Router
from keyboards.inline.geolocation.geolocate_kb import geolocation_choice
from aiogram.filters.command import Command


router = Router()


@router.message(Command("geolocation"))
async def geolocation(message: types.Message):
    await message.answer("🔽 Выбери входные данные", reply_markup=geolocation_choice())