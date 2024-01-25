from aiogram import types, Router, F, Bot
from aiogram.filters.command import CommandStart
from aiogram import types
from keyboards.default.main import main_keyboard
from db.base import existe_in_db, add_user_in_data_base, add_user_in_geolocate, update_send_start


router = Router()


@router.message(CommandStart())
async def bot_start(message: types.Message):
    update_send_start(message.chat.id, 0)
    if not existe_in_db("user", message.chat.id):
        add_user_in_data_base(message.chat.id, message.from_user.username, message.from_user.full_name)
    if not existe_in_db("geolocate", message.from_user.id):
        add_user_in_geolocate(message.from_user.id)

    msg = f"Привет <b>{message.from_user.full_name}</b>!"
    msg += "\nЯ 🥸 <b>𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</b>."
    msg += "\n📖 Узнай все функции бота отправив ему /help."
    await message.answer(msg, reply_markup=main_keyboard)


@router.callback_query(F.data == "check_subscribe_on_news_channel")
async def check_subscribe(call: types.CallbackQuery, bot: Bot):
    member = await bot.get_chat_member(chat_id="@bots_rooms", user_id=call.message.chat.id)
    if member.status != "left":
        await call.message.delete()
        await bot_start(call.message)
    else:
        await call.answer("❗ Ты не подписался на канал!", show_alert=True)