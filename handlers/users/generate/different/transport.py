from loader import dp, fake
from aiogram import types
from keyboards.callbacks.generate.different.callback_transport import transport_inline_callback
from keyboards.inline.generate.different.transport_kb import transport_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="🚗 Транспорт")
async def main_transport(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=transport_category_keyboard)


@dp.callback_query_handler(transport_inline_callback.filter(_pass="_"))
async def transport_data(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_transport = {
            "license_plate": f"<b><i>Номерной знак (включая специальные номера):</i></b>\n<code>{fake.license_plate()}</code>",
            "vin_number": f"<b><i>ВИН-номер (идентификатор):</i></b>\n<code>{fake.vin()}</code>"
        }
        msg = ""
        for i in test_transport:
            if i in call.data:
                msg += test_transport[i]
        try:
            await call.message.edit_text(msg, reply_markup=transport_category_keyboard)
        except MessageNotModified: pass