from loader import dp, bot
from aiogram import types
from keyboards.default.generate_kb import generate_keyboard
from database.base import add_last_message
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("generate"))
async def generate(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)