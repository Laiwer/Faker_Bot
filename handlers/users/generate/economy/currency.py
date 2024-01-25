from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.economy.currency_kb import currency_category_keyboard, currency_paper_category_keyboard, currency_crypto_category_keyboard


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "💵 Валюты")
async def main_currency(message: types.Message):
    await message.answer(choice_msg, reply_markup=currency_category_keyboard())


@router.callback_query(GenerateCategory.filter(F.type == "currency"))
async def currency_category(call: types.CallbackQuery, callback_data: GenerateCategory):
    await call.answer()
    if callback_data.category == "paper":
        await call.message.edit_text(choice_msg, reply_markup=currency_paper_category_keyboard())
    elif callback_data.category == "crypto":
        await call.message.edit_text(choice_msg, reply_markup=currency_crypto_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "currency"))
async def currency_category_data(call: types.CallbackQuery, callback_data: GenerateData, fake: Faker):
    await call.answer()
    if callback_data.back:
        await call.message.edit_text(choice_msg, reply_markup=currency_category_keyboard())
        return
    elif callback_data.category == "paper":
        cur = fake.currency()
        test_currency = {
            "all": f"<b><i>Валюта (с кодом):</i></b>\n<code>{cur[1]} ({cur[0]})</code>",
            "name_currency": f"<b><i>Название валюты:</i></b>\n<code>{fake.currency_name()}</code>",
            "id_currency": f"<b><i>Код валюты:</i></b>\n<code>{fake.currency_code()}</code>",
            "symbol_currency": f"<b><i>Символ валюты:</i></b>\n<code>{fake.currency_symbol()}</code>",
            "number_paper": f"<b><i>Случайное количество рублей:</i></b>\n<code>{fake.pricetag()}</code>",
        }
        keyboard = currency_paper_category_keyboard()
    elif callback_data.category == "crypto":
        cur = fake.cryptocurrency()
        test_currency = {
            "all": f"<b><i>Криптовалютп (с кодом):</i></b>\n<code>{cur[1]} ({cur[0]})</code>",
            "name_currency": f"<b><i>Название криптовалюты:</i></b>\n<code>{fake.cryptocurrency_name()}</code>",
            "id_currency": f"<b><i>Код криптовалюты:</i></b>\n<code>{fake.cryptocurrency_code()}</code>",
        }
        keyboard = currency_crypto_category_keyboard()
    msg = ""
    for i in test_currency:
        if i in call.data:
            msg += test_currency[i]
    await call.message.edit_text(msg, reply_markup=keyboard)