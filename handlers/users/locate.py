from loader import dp, fake
from aiogram import types
from keyboards.callbacks.callback_locate import locate_inline_callback
from keyboards.inline.locate_kb import locate_category_keyboard
from handlers.users.start import check_sub_channel, keyboard_check_channel


@dp.message_handler(text="🗺 Расположение")
async def main_locate(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
            await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=locate_category_keyboard)


@dp.callback_query_handler(locate_inline_callback.filter(_pass="_"))
async def locate_data(call: types.CallbackQuery):
    await call.answer()
    if not await check_sub_channel(call.from_user.id):
            await keyboard_check_channel(call.message)
    else:
        test_locate = {
            "all_address": f"<b><i>Полный адрес:</i></b>\n<code>{fake.address()}</code>",
            "street_address": f"<b><i>Адрес с улицей и домом:</i></b>\n<code>{fake.street_address()}</code>",
            "street_name": f"<b><i>Название улицы:</i></b>\n<code>{fake.street_name()}</code>",
            "city": f"<b><i>Название города:</i></b>\n<code>{fake.city()}</code>",
            "post_index": f"<b><i>Почтовый индекс:</i></b>\n<code>{fake.postcode()}</code>",
            "country": f"<b><i>Название страны:</i></b>\n<code>{fake.country()}</code>"
        }
        msg = ""
        for i in test_locate:
            if i in call.data:
                msg += test_locate[i]
        try:
            await call.message.edit_text(msg, reply_markup=locate_category_keyboard)
        except Exception: pass