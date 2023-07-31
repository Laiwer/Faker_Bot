from aiogram import types
from loader import dp
from random import choice
from data.list_answer_bot import TEXT_ANSWER
from handlers.users.start import check_sub_channel, keyboard_check_channel


@dp.message_handler()
async def all_message(message: types.Message):
        if message.chat.type == "private":
                if await check_sub_channel(message.from_user.id):
                        await message.answer(choice(TEXT_ANSWER))
                else:
                        await keyboard_check_channel(message)