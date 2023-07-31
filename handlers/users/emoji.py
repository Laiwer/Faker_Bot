from loader import dp, fake
from aiogram import types
from keyboards.inline.emoji_kb import emoji_category_keyboard
from handlers.users.start import check_sub_channel, keyboard_check_channel


@dp.message_handler(text="🎭 Эмодзи")
async def main_emoji(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=emoji_category_keyboard)


@dp.callback_query_handler(text="emoji_emoji")
async def emoji_emoji_data(call: types.CallbackQuery):
    await call.answer()
    if not await check_sub_channel(call.from_user.id):
            await keyboard_check_channel(call.message)
    else:
        msg = f"<b><i>Случайный эмодзи:</i></b>\n<code>{fake.emoji()}</code>"
        try:
            await call.message.edit_text(msg, reply_markup=emoji_category_keyboard)
        except Exception: pass