from loader import dp, fake
from aiogram import types
from keyboards.callbacks.generate.economy.callback_company import company_inline_callback
from keyboards.inline.generate.economy.company_kb import company_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="🏢 Компания")
async def main_company(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=company_category_keyboard)


@dp.callback_query_handler(company_inline_callback.filter(_pass="_"))
async def company_data(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_company = {
            "name_company": f"<b><i>Название маленькой компании:</i></b>\n<code>{fake.company()}</code>",
            "large_company": f"<b><i>Название крупной компании:</i></b>\n<code>{fake.large_company()}</code>",
            "catch_phrase": f"<b><i>Слоган компании:</i></b>\n<code>{fake.catch_phrase()}</code>",
            "activity_company": f"<b><i>Деятельность компании:</i></b>\n<code>{fake.bs()}</code>",
            "inn": f"<b><i>ИНН (Идентификационный номер налогоплательщика):</i></b>\n<code>{fake.businesses_inn()}</code>",
            "ogrn": f"<b><i>ОГРН (Основной государственный регистрационный номер):</i></b>\n<code>{fake.businesses_ogrn()}</code>",
        }
        msg = ""
        for i in test_company:
            if i in call.data:
                msg += test_company[i]
        try:
            await call.message.edit_text(msg, reply_markup=company_category_keyboard)
        except MessageNotModified: pass