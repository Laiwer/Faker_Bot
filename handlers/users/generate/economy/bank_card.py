from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.economy.bank_card_kb import bank_card_category_keyboard


router = Router()


@router.message(F.text == "💳 Банковская карта")
async def main_bank_card(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=bank_card_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "bank_card"))
async def bank_card_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_bank_card = {
        "card_bank": f"<b><i>Банковская карта:</i></b>\n<code>{fake.credit_card_full()}</code>",
        "pay_system": f"<b><i>Платёжная система:</i></b>\n<code>{fake.credit_card_provider()}</code>",
        "name_bank": f"<b><i>Российский банк:</i></b>\n<code>{fake.bank()}</code>",
        "id_card": f"<b><i>Номер карты:</i></b>\n<code>{fake.credit_card_number()}</code>",
        "date_card": f"<b><i>Дата, до которой работает карта:</i></b>\n<code>{fake.credit_card_expire()}</code>",
        "cvv": f"<b><i>Код на заднем обороте карты:</i></b>\n<code>{fake.credit_card_security_code()}</code>",
    }
    msg = ""
    for i in test_bank_card:
        if i in call.data:
            msg += test_bank_card[i]
    await call.message.edit_text(msg, reply_markup=bank_card_category_keyboard())