from loader import dp, fake
from aiogram import types
from keyboards.callbacks.generate.different.callback_datetime import datetime_inline_callback
from keyboards.inline.generate.different.date_time_kb import datetime_category_keyboard, datetime_dates_category_keyboard, \
    datetime_dating_category_keyboard, datetime_times_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import add_last_message
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="📅 Дата и время")
async def main_datetime(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=datetime_category_keyboard)


@dp.callback_query_handler(text="datetime_dating")
async def datetime_dating_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=datetime_dating_category_keyboard)

@dp.callback_query_handler(text="datetime_dates")
async def datetime_dates_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=datetime_dates_category_keyboard)

@dp.callback_query_handler(text="datetime_times")
async def datetime_times_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=datetime_times_category_keyboard)

@dp.callback_query_handler(text="back_to_datetime_category")
async def back_to_datetime(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=datetime_category_keyboard)


@dp.callback_query_handler(datetime_inline_callback.filter(what="dating"))
async def dating_datetime(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_datetime = {
            "day_month": f"<b><i>День месяца:</i></b>\n<code>{fake.day_of_month()}</code>",
            "day_week": f"<b><i>День недели:</i></b>\n<code>{fake.day_of_week()}</code>",
            "num_month": f"<b><i>Номер месяца:</i></b>\n<code>{fake.month()}</code>",
            "name_month": f"<b><i>Название месяца:</i></b>\n<code>{fake.month_name()}</code>",
            "year": f"<b><i>Год:</i></b>\n<code>{fake.year()}</code>",
            "centure": f"<b><i>Век:</i></b>\n<code>{fake.century()}</code>",
        }
        msg = ""
        for i in test_datetime:
            if i in call.data:
                msg += test_datetime[i]
        try:
            await call.message.edit_text(msg, reply_markup=datetime_dating_category_keyboard)
        except MessageNotModified: pass


@dp.callback_query_handler(datetime_inline_callback.filter(what="dates"))
async def dates_datetime(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_datetime = {
            "birthday": f"<b><i>Дата рождения:</i></b>\n<code>{fake.date_of_birth().strftime('%d.%m.%Y')}</code>",
            "random_date": f"<b><i>Случайная дата:</i></b>\n<code>{fake.date_time_ad().strftime('%d.%m.%Y')}</code>",
            "date_month": f"<b><i>Дата в этом месяце:</i></b>\n<code>{fake.date_this_month().strftime('%d.%m.%Y')}</code>",
            "date_year": f"<b><i>Дата в этом году:</i></b>\n<code>{fake.date_this_year().strftime('%d.%m.%Y')}</code>",
            "date_decade": f"<b><i>Дата в этом десятилетии:</i></b>\n<code>{fake.date_this_decade().strftime('%d.%m.%Y')}</code>",
            "date_centure": f"<b><i>Дата в этом веке:</i></b>\n<code>{fake.date_this_century().strftime('%d.%m.%Y')}</code>",
            "future_date": f"<b><i>Будущая дата:</i></b>\n<code>{fake.future_date(end_date='+100y').strftime('%d.%m.%Y')}</code>",
        }
        msg = ""
        for i in test_datetime:
            if i in call.data:
                msg += test_datetime[i]
        try:
            await call.message.edit_text(msg, reply_markup=datetime_dates_category_keyboard)
        except MessageNotModified: pass


@dp.callback_query_handler(datetime_inline_callback.filter(what="times"))
async def times_datetime(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_datetime = {
            "time_24": f"<b><i>Время:</i></b>\n<code>{fake.time()}</code>",
            "time_zone": f"<b><i>Часовая зона:</i></b>\n<code>{fake.timezone()}</code>",
        }
        msg = ""
        for i in test_datetime:
            if i in call.data:
                msg += test_datetime[i]
        try:
            await call.message.edit_text(msg, reply_markup=datetime_times_category_keyboard)
        except MessageNotModified: pass