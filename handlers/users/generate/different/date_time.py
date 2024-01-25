from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.different.date_time_kb import datetime_category_keyboard, datetime_dates_category_keyboard, \
    datetime_dating_category_keyboard, datetime_times_category_keyboard


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "📅 Дата и время")
async def main_datetime(message: types.Message):
    await message.answer(choice_msg, reply_markup=datetime_category_keyboard())


@router.callback_query(GenerateCategory.filter(F.type == "datetime"))
async def datetime_category(call: types.CallbackQuery, callback_data: GenerateCategory):
    await call.answer()
    if callback_data.category == "dating":
        await call.message.edit_text(choice_msg, reply_markup=datetime_dating_category_keyboard())
    elif callback_data.category == "dates":
        await call.message.edit_text(choice_msg, reply_markup=datetime_dates_category_keyboard())
    elif callback_data.category == "times":
        await call.message.edit_text(choice_msg, reply_markup=datetime_times_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "datetime"))
async def datetime_category_data(call: types.CallbackQuery, callback_data: GenerateData, fake: Faker):
    await call.answer()
    if callback_data.back:
        await call.message.edit_text(choice_msg, reply_markup=datetime_category_keyboard())
        return
    elif callback_data.category == "dating":
        test_datetime = {
            "day_month": f"<b><i>День месяца:</i></b>\n<code>{fake.day_of_month()}</code>",
            "day_week": f"<b><i>День недели:</i></b>\n<code>{fake.day_of_week()}</code>",
            "num_month": f"<b><i>Номер месяца:</i></b>\n<code>{fake.month()}</code>",
            "name_month": f"<b><i>Название месяца:</i></b>\n<code>{fake.month_name()}</code>",
            "year": f"<b><i>Год:</i></b>\n<code>{fake.year()}</code>",
            "centure": f"<b><i>Век:</i></b>\n<code>{fake.century()}</code>",
        }
        keyboard = datetime_dating_category_keyboard()
    elif callback_data.category == "dates":
        test_datetime = {
            "birthday": f"<b><i>Дата рождения:</i></b>\n<code>{fake.date_of_birth().strftime('%d.%m.%Y')}</code>",
            "random_date": f"<b><i>Случайная дата:</i></b>\n<code>{fake.date_time_ad().strftime('%d.%m.%Y')}</code>",
            "date_month": f"<b><i>Дата в этом месяце:</i></b>\n<code>{fake.date_this_month().strftime('%d.%m.%Y')}</code>",
            "date_year": f"<b><i>Дата в этом году:</i></b>\n<code>{fake.date_this_year().strftime('%d.%m.%Y')}</code>",
            "date_decade": f"<b><i>Дата в этом десятилетии:</i></b>\n<code>{fake.date_this_decade().strftime('%d.%m.%Y')}</code>",
            "date_centure": f"<b><i>Дата в этом веке:</i></b>\n<code>{fake.date_this_century().strftime('%d.%m.%Y')}</code>",
            "future_date": f"<b><i>Будущая дата:</i></b>\n<code>{fake.future_date(end_date='+100y').strftime('%d.%m.%Y')}</code>",
        }
        keyboard = datetime_dates_category_keyboard()
    elif callback_data.category == "times":
        test_datetime = {
            "time_24": f"<b><i>Время:</i></b>\n<code>{fake.time()}</code>",
            "time_zone": f"<b><i>Часовая зона:</i></b>\n<code>{fake.timezone()}</code>",
        }
        keyboard = datetime_times_category_keyboard()
    msg = ""
    for i in test_datetime:
        if i in call.data:
            msg += test_datetime[i]
    await call.message.edit_text(msg, reply_markup=keyboard)