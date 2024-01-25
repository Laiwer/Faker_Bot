from aiogram import types, Router, F, Bot
from faker import Faker
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.different.locate_kb import locate_category_keyboard, locate_address_category_keyboard, \
    locate_coordinate_category_keyboard, locate_geo_category_keyboard


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "🗺 Расположение")
async def main_locate(message: types.Message):
    await message.answer(choice_msg, reply_markup=locate_category_keyboard())


@router.callback_query(GenerateCategory.filter(F.type == "locate"))
async def locate_category(call: types.CallbackQuery, callback_data: GenerateCategory):
    await call.answer()
    if callback_data.category == "address":
        await call.message.edit_text(choice_msg, reply_markup=locate_address_category_keyboard())
    elif callback_data.category == "coordinate":
        await call.message.edit_text(choice_msg, reply_markup=locate_coordinate_category_keyboard())
    elif callback_data.category == "geo":
        await call.message.edit_text(choice_msg, reply_markup=locate_geo_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "locate"))
async def locate_category_data(call: types.CallbackQuery, callback_data: GenerateData, fake: Faker, bot: Bot):
    await call.answer()
    if callback_data.back:
        await call.message.edit_text(choice_msg, reply_markup=locate_category_keyboard())
        return
    elif callback_data.category == "geo_pos":
        _random_russia = fake.local_latlng(country_code="RU")
        _random_world = fake.location_on_land()
        test_locate = {
            "random_russia": [_random_russia, f"<b><i>Ширина, Долгота: Часовая зона:</i></b>\n<code>{_random_russia[0]}, {_random_russia[1]}\n{_random_russia[-1]}</code>"],
            "random_world": [_random_world, f"<b><i>Ширина, Долгота: Часовая зона:</i></b>\n<code>{_random_world[0]}, {_random_world[1]}\n{_random_world[-1]}</code>"],
        }
        msg = ""
        key = ""
        for i in test_locate:
            if i in call.data:
                key = i
                msg += test_locate[i][1]
        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await call.message.answer_location(test_locate[key][0][0], test_locate[key][0][1])
        await call.message.answer(msg, reply_markup=locate_geo_category_keyboard())
        return
    elif callback_data.category == "add_ss":
        test_locate = {
            "all_address": f"<b><i>Полный адрес:</i></b>\n<code>{fake.address()}</code>",
            "number_house": f"<b><i>Номер дома:</i></b>\n<code>{fake.building_number()}</code>",
            "street_address": f"<b><i>Адрес с улицей и домом:</i></b>\n<code>{fake.street_address()}</code>",
            "street_name": f"<b><i>Название улицы:</i></b>\n<code>{fake.street_name()}</code>",
            "city": f"<b><i>Название города:</i></b>\n<code>{fake.city()}</code>",
            "region": f"<b><i>Субъект Российской Федерации:</i></b>\n<code>{fake.administrative_unit()}</code>",
            "post_index": f"<b><i>Почтовый индекс:</i></b>\n<code>{fake.postcode()}</code>",
        }
        keyboard = locate_address_category_keyboard()
    elif callback_data.category == "coord_s":
        test_locate = {
            "longitude": f"<b><i>Долгота (от -180 до 180):</i></b>\n<code>{fake.longitude()}</code>",
            "latitude": f"<b><i>Широта (от -90 до 90):</i></b>\n<code>{fake.latitude()}</code>",
            "random_coord": f"<b><i>Случайные координаты (шир., долг.):</i></b>\n<code>{', '.join([str(float(i)) for i in fake.latlng()])}</code>",
            "name_country": f"<b><i>Название страны:</i></b>\n<code>{fake.country()}</code>",
        }
        keyboard = locate_coordinate_category_keyboard()
    
    msg = ""
    for i in test_locate:
        if i in call.data:
            msg += test_locate[i]
    await call.message.edit_text(msg, reply_markup=keyboard)
