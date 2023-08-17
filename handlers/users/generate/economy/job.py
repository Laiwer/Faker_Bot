from loader import dp, fake
from aiogram import types
from keyboards.inline.generate.economy.job_kb import job_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="🛠 Профессия")
async def main_job(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=job_category_keyboard)


@dp.callback_query_handler(text="job_job")
async def job_data(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        msg = f"<b><i>Профессия:</i></b>\n<code>{fake.job()}</code>"
        try:
            await call.message.edit_text(msg, reply_markup=job_category_keyboard)
        except MessageNotModified: pass