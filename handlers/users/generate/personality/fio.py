from loader import dp, fake
from aiogram import types
from keyboards.callbacks.generate.personality.callback_fio import fio_inline_callback
from keyboards.inline.generate.person.fio_kb import fio_category_keyboard, fio_male_category_keyboard, fio_female_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="🪪 ФИО")
async def main_fio(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=fio_category_keyboard)


@dp.callback_query_handler(text="fio_male")
async def fio_male_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=fio_male_category_keyboard)

@dp.callback_query_handler(text="fio_female")
async def fio_female_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=fio_female_category_keyboard)

@dp.callback_query_handler(text="back_to_fio_category")
async def back_to_fio(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=fio_category_keyboard)


@dp.callback_query_handler(fio_inline_callback.filter(gender="male"))
async def male_fio(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_fio = {
            "fio_person": f"<b><i>Мужское Ф.И.О.:</i></b>\n<code>{fake.name_male()}</code>",
            "first_name": f"<b><i>Мужское имя:</i></b>\n<code>{fake.first_name_male()}</code>",
            "middle_name": f"<b><i>Мужская фамилия:</i></b>\n<code>{fake.last_name_male()}</code>",
            "last_name": f"<b><i>Мужское отчество:</i></b>\n<code>{fake.middle_name_male()}</code>"
        }
        msg = ""
        for i in test_fio:
            if i in call.data:
                msg += test_fio[i]
        try:
            await call.message.edit_text(msg, reply_markup=fio_male_category_keyboard)
        except MessageNotModified: pass


@dp.callback_query_handler(fio_inline_callback.filter(gender="female"))
async def female_fio(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_fio = {
            "fio_person": f"<b><i>Женское Ф.И.О.:</i></b>\n<code>{fake.name_female()}</code>",
            "first_name": f"<b><i>Женское имя:</i></b>\n<code>{fake.first_name_female()}</code>",
            "middle_name": f"<b><i>Женская фамилия:</i></b>\n<code>{fake.last_name_female()}</code>",
            "last_name": f"<b><i>Женское отчество:</i></b>\n<code>{fake.middle_name_female()}</code>"
        }
        msg = ""
        for i in test_fio:
            if i in call.data:
                msg += test_fio[i]
        try:
            await call.message.edit_text(msg, reply_markup=fio_female_category_keyboard)
        except MessageNotModified: pass