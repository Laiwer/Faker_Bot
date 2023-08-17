from loader import dp
from aiogram import types
from database.base import add_last_message, count_all_bot_users, count_recently_bot_users, count_active_bot_users, \
    count_time_in_bot
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from keyboards.inline.statistics.statistics_kb import statistics_category_keyboard
from keyboards.callbacks.statistics.callback_statistics import statistics_inline_callback
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="📊 Статистика")
async def statistic_main(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("🔽 Выбери снизу", reply_markup=statistics_category_keyboard)


@dp.callback_query_handler(statistics_inline_callback.filter(_pass="_"))
async def statistics_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        time = ""
        if "time_bots" in call.data:
            timee = count_time_in_bot(call.message.chat.id)
            if timee[0] == 0:
                if timee[1] == 0:
                    time += f"{timee[2]} ч. {0 if timee[3] < 0 else timee[3]} мин."
                else:
                    time += f"{timee[1]} дн. {timee[2]} ч."
            else:
                time += f"{timee[0]} мес. {timee[1]} дн. {timee[2]} ч."
        test_statistics = {
            "all_users": f"<b><i>Всего пользователей бота:</i>\n{count_all_bot_users():,} чел.</b>",
            "hour_users": f"<b><i>Пользователи бота за последний час:</i>\n{count_recently_bot_users():,} чел.</b>",
            "day_users": f"<b><i>Пользователи бота за последние сутки:</i>\n{count_active_bot_users():,} чел.</b>",
            "time_bots": f"<b><i>Время, проведённое в боте:</i>\n{time}</b>",
        }
        msg = ""
        for i in test_statistics:
            if i in call.data:
                msg += test_statistics[i]
        try:
            await call.message.edit_text(msg, reply_markup=statistics_category_keyboard)
        except MessageNotModified: pass