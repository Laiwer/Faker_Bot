from loader import dp, fake
from aiogram import types
from keyboards.callbacks.callback_company import company_inline_callback
from keyboards.inline.company_kb import company_category_keyboard
from handlers.users.start import check_sub_channel, keyboard_check_channel


@dp.message_handler(text="🏢 Компания")
async def main_company(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=company_category_keyboard)


@dp.callback_query_handler(company_inline_callback.filter(_pass="_"))
async def company_data(call: types.CallbackQuery):
    await call.answer()
    if not await check_sub_channel(call.from_user.id):
            await keyboard_check_channel(call.message)
    else:
        test_company = {
            "name_company": f"<b><i>Название компании:</i></b>\n<code>{fake.company()}</code>",
            "catch_phrase": f"<b><i>Слоган компании:</i></b>\n<code>{fake.catch_phrase()}</code>",
            "activity_company": f"<b><i>Деятельность компании:</i></b>\n<code>{fake.bs()}</code>"
        }
        msg = ""
        for i in test_company:
            if i in call.data:
                msg += test_company[i]
        try:
            await call.message.edit_text(msg, reply_markup=company_category_keyboard)
        except Exception: pass