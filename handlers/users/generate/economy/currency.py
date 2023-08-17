from loader import dp, fake
from aiogram import types
from keyboards.callbacks.generate.economy.callback_currency import currecny_inline_callback
from keyboards.inline.generate.economy.currency_kb import currency_category_keyboard, currency_paper_category_keyboard, currency_crypto_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="💵 Валюты")
async def main_currency(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=currency_category_keyboard)


@dp.callback_query_handler(text="currency_paper")
async def currency_paper_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=currency_paper_category_keyboard)

@dp.callback_query_handler(text="currency_crypto")
async def currency_crypto_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=currency_crypto_category_keyboard)

@dp.callback_query_handler(text="back_to_currecny_category")
async def back_to_currency(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=currency_category_keyboard)


@dp.callback_query_handler(currecny_inline_callback.filter(what="paper"))
async def paper_currency(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        cur = ("", "")
        if "all" in call.data:
            cur = fake.currency()
        test_currency = {
            "all": f"<b><i>Валюта (с кодом):</i></b>\n<code>{cur[1]} ({cur[0]})</code>",
            "name_currency": f"<b><i>Название валюты:</i></b>\n<code>{fake.currency_name()}</code>",
            "id_currency": f"<b><i>Код валюты:</i></b>\n<code>{fake.currency_code()}</code>",
            "symbol_currency": f"<b><i>Символ валюты:</i></b>\n<code>{fake.currency_symbol()}</code>",
            "number_paper": f"<b><i>Случайное количество рублей:</i></b>\n<code>{fake.pricetag()}</code>",
        }
        msg = ""
        for i in test_currency:
            if i in call.data:
                msg += test_currency[i]
        try:
            await call.message.edit_text(msg, reply_markup=currency_paper_category_keyboard)
        except MessageNotModified: pass


@dp.callback_query_handler(currecny_inline_callback.filter(what="crypto"))
async def crypto_currency(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        cur = ("", "")
        if "all" in call.data:
            cur = fake.cryptocurrency()
        test_currency = {
            "all": f"<b><i>Криптовалютп (с кодом):</i></b>\n<code>{cur[1]} ({cur[0]})</code>",
            "name_currency": f"<b><i>Название криптовалюты:</i></b>\n<code>{fake.cryptocurrency_name()}</code>",
            "id_currency": f"<b><i>Код криптовалюты:</i></b>\n<code>{fake.cryptocurrency_code()}</code>",
        }
        msg = ""
        for i in test_currency:
            if i in call.data:
                msg += test_currency[i]
        try:
            await call.message.edit_text(msg, reply_markup=currency_crypto_category_keyboard)
        except MessageNotModified: pass