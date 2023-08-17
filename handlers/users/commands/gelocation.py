from loader import dp
from aiogram import types
from keyboards.inline.geolocation.geolocate_kb import geolocation_choice
from database.base import add_last_message
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("geolocation"))
async def geolocation(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("🔽 Выбери входные данные", reply_markup=geolocation_choice)