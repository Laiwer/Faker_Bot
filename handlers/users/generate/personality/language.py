from loader import dp, fake
from aiogram import types
from keyboards.inline.generate.person.language_kb import language_category_keyboard
from keyboards.callbacks.generate.personality.callback_language import language_inline_callback
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="👅 Язык")
async def main_language(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=language_category_keyboard)


@dp.callback_query_handler(language_inline_callback.filter(_pass="_"))
async def language_data(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_language = {
            "names": f"<b><i>Случайный язык:</i></b>\n<code>{fake.language_name()}</code>",
            "codes": f"<b><i>Код языка:</i></b>\n<code>{fake.language_code().upper()}</code>",
        }
        msg = ""
        for i in test_language:
            if i in call.data:
                msg += test_language[i]
        try:
            await call.message.edit_text(msg, reply_markup=language_category_keyboard)
        except MessageNotModified: pass