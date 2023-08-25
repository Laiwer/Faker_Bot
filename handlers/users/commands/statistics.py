from loader import dp, bot
from aiogram import types
from keyboards.inline.statistics.statistics_kb import statistics_inline_keyboard
from database.base import add_last_message, count_active_bot_users, count_all_bot_users, count_recently_bot_users, \
    count_time_in_bot
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from aiogram.dispatcher.filters import Command
from data.data_config import ADMINS


@dp.message_handler(Command("statistics"))
async def statistics(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        time = ""
        timee = count_time_in_bot(ADMINS[0])
        if timee[0] == 0:
            if timee[1] == 0:
                time += f"{timee[2]} ч. {0 if timee[3] < 0 else timee[3]} мин."
            else:
                time += f"{timee[1]} дн. {timee[2]} ч."
        else:
            time += f"{timee[0]} мес. {timee[1]} дн. {timee[2]} ч."

        msg = f"👥 <b><i>Всего пользователей бота:</i>\n\t\t\t\t\t\t{count_all_bot_users():,} чел.</b>"
        msg += f"\n\n👋 <b><i>Новые пользователи бота за последний час:</i>\n\t\t\t\t\t\t{count_recently_bot_users('j'):,} чел.</b>"
        msg += f"\n\n✅ <b><i>Новые пользователи бота за последние сутки:</i>\n\t\t\t\t\t\t{count_active_bot_users('j'):,} чел.</b>"
        msg += f"\n\n⏳ <b><i>Пользователи бота за последний час:</i>\n\t\t\t\t\t\t{count_recently_bot_users('l'):,} чел.</b>"
        msg += f"\n\n📆 <b><i>Пользователи бота за последние сутки:</i>\n\t\t\t\t\t\t{count_active_bot_users('l'):,} чел.</b>"
        msg += f"\n\n⏰ <b><i>Бот работает:</i>\n\t\t\t\t\t\t{time}</b>"
        await message.answer(msg, reply_markup=statistics_inline_keyboard)