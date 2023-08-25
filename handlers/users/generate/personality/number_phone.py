from aiogram import types
from loader import dp, fake
from database.base import add_last_message
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from keyboards.inline.generate.person.number_phone_kb import number_phone_category_keyboard
from keyboards.callbacks.generate.personality.callback_number_phone import number_phone_inline_callback
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="☎️ Номер телефона")
async def main_number_phone(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=number_phone_category_keyboard)


@dp.callback_query_handler(number_phone_inline_callback.filter(_pass="_"))
async def number_phone_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_number_phone = {
            "code_phone": f"<b><i>Код телефоного номера страны:</i></b>\n<code>{fake.country_calling_code()}</code>",
            "msisdn": f"<b><i>MSISDN (<a href='https://ru.wikipedia.org/wiki/MSISDN'>Википедия</a>):</i></b>\n<code>{fake.msisdn()}</code>",
            "num_phone": f"<b><i>Номер телефона (Россия):</i></b>\n<code>{fake.phone_number()}</code>",
        }
        msg = ""
        for i in test_number_phone:
            if i in call.data:
                msg += test_number_phone[i]
        try:
            await call.message.edit_text(msg, reply_markup=number_phone_category_keyboard, disable_web_page_preview=True)
        except MessageNotModified: pass