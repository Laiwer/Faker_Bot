from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot
from aiogram import types
from keyboards.inline.subscribe_channel_kb import check_subscribe_keyboard
from keyboards.default.main_kb import main_keyboard


async def check_sub_channel(user_id):
    chat_member = await bot.get_chat_member(chat_id="@faker_bots_channel", user_id=user_id)
    if chat_member["status"] != "left":
        return True
    else:
        return False

async def keyboard_check_channel(msg):
    await msg.answer("⬇ Для продолжения подпишись на <b><i>новостной канал бота</i></b>, чтобы получать информацию об обновлениях", reply_markup=check_subscribe_keyboard)


@dp.message_handler(CommandStart())
async def check_subscribe(message: types.Message):
    if message.chat.type == "private":
        if not await check_sub_channel(message.from_user.id):
            await keyboard_check_channel(message)
        else:
            msg = f"Привет <b>{message.from_user.full_name}</b>!"
            msg += "\n\nЯ 🥸 <b>𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</b>, генерирую случайные данные: <b><i>ФИО, адреса, профессии, даты и т.п.</i></b>"
            msg += "\n\n⬇ Снизу на клавиатуре выбери что сгенирировать"
            await message.answer(msg, reply_markup=main_keyboard)

@dp.callback_query_handler(text="check_subscribe_on_news_channel")
async def bot_start(call: types.CallbackQuery):
    if await check_sub_channel(call.from_user.id):
        await call.message.delete()
        await check_subscribe(call.message)
    else:
        await call.answer("❗ Ты не подписался на канал!", show_alert=True)