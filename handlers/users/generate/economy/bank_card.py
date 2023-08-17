from loader import dp, fake
from aiogram import types
from keyboards.callbacks.generate.economy.callback_bank_card import bank_card_inline_callback
from keyboards.inline.generate.economy.bank_card_kb import bank_card_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="💳 Банковская карта")
async def main_bank_card(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=bank_card_category_keyboard)


@dp.callback_query_handler(bank_card_inline_callback.filter(_pass="_"))
async def bank_card_data(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
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
        try:
            await call.message.edit_text(msg, reply_markup=bank_card_category_keyboard)
        except MessageNotModified: pass