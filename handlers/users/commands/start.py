from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot, fake
from aiogram import types
from keyboards.inline.subscribe_channel_kb import check_subscribe_keyboard
from keyboards.default.main import main_keyboard
from database.base import existe_in_db, add_user_in_data_base, add_user_in_geolocate, add_last_message, \
    update_send_start


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
        add_last_message(message.chat.id)
        update_send_start(message.chat.id, 0)
        if not existe_in_db("user", message.chat.id):
            add_user_in_data_base(message.chat.id, message.from_user.username, message.from_user.full_name)
        if not existe_in_db("geolocate", message.from_user.id):
            add_user_in_geolocate(message.from_user.id)
        
        if not await check_sub_channel(message.from_user.id):
            await keyboard_check_channel(message)
        else:
            msg = f"Привет <b>{message.from_user.full_name}</b>!"
            msg += "\nЯ 🥸 <b>𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</b>."
            msg += "\n\n📖 Узнай все функции бота отправив ему /help."
            msg += "\n⬇ Снизу на клавиатуре выбери что делать боту"
            await message.answer(msg, reply_markup=main_keyboard)


@dp.callback_query_handler(text="check_subscribe_on_news_channel")
async def bot_start(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    if await check_sub_channel(call.from_user.id):
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await check_subscribe(call.message)
    else:
        await call.answer("❗ Ты не подписался на канал!", show_alert=True)