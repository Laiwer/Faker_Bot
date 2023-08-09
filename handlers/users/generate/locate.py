from loader import dp, bot, fake
from aiogram import types
from keyboards.callbacks.callback_locate import locate_inline_callback
from keyboards.inline.locate_kb import locate_category_keyboard, locate_address_category_keyboard, \
    locate_coordinate_category_keyboard, locate_geo_category_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel


@dp.message_handler(text="🗺 Расположение")
async def main_locate(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=locate_category_keyboard)


@dp.callback_query_handler(text="locate_address_category")
async def locate_address_category(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=locate_address_category_keyboard)

@dp.callback_query_handler(text="locate_coordinate_category")
async def locate_coordinate_category(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=locate_coordinate_category_keyboard)

@dp.callback_query_handler(text="locate_geo_category")
async def locate_coordinate_category(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=locate_geo_category_keyboard)

@dp.callback_query_handler(text="back_to_locate_category")
async def back_to_locate_category(call: types.CallbackQuery):
    await call.answer()
    if "Ширина" in call.message.text:
        await bot.delete_message(call.message.chat.id, call.message.message_id-1)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=locate_category_keyboard)


@dp.callback_query_handler(locate_inline_callback.filter(data="add_ss"))
async def locate_address_data(call: types.CallbackQuery):
    await call.answer()
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_locate = {
            "all_address": f"<b><i>Полный адрес:</i></b>\n<code>{fake.address()}</code>",
            "number_house": f"<b><i>Номер дома:</i></b>\n<code>{fake.building_number()}</code>",
            "street_address": f"<b><i>Адрес с улицей и домом:</i></b>\n<code>{fake.street_address()}</code>",
            "street_name": f"<b><i>Название улицы:</i></b>\n<code>{fake.street_name()}</code>",
            "city": f"<b><i>Название города:</i></b>\n<code>{fake.city()}</code>",
            "post_index": f"<b><i>Почтовый индекс:</i></b>\n<code>{fake.postcode()}</code>",
        }
        msg = ""
        for i in test_locate:
            if i in call.data:
                msg += test_locate[i]
        try:
            await call.message.edit_text(msg, reply_markup=locate_address_category_keyboard)
        except Exception: pass


@dp.callback_query_handler(locate_inline_callback.filter(data="coord_s"))
async def locate_coordinate_data(call: types.CallbackQuery):
    await call.answer()
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_locate = {
            "longitude": f"<b><i>Долгота (от -180 до 180):</i></b>\n<code>{fake.longitude()}</code>",
            "latitude": f"<b><i>Широта (от -90 до 90):</i></b>\n<code>{fake.latitude()}</code>",
            "random_coord": f"<b><i>Случайные координаты (шир., долг.):</i></b>\n<code>{', '.join([str(float(i)) for i in fake.latlng()])}</code>",
            "name_country": f"<b><i>Название страны:</i></b>\n<code>{fake.country()}</code>",
        }
        msg = ""
        for i in test_locate:
            if i in call.data:
                msg += test_locate[i]
        try:
            await call.message.edit_text(msg, reply_markup=locate_coordinate_category_keyboard)
        except Exception: pass


@dp.callback_query_handler(locate_inline_callback.filter(data="geo_pos"))
async def locate_geo_data(call: types.CallbackQuery):
    await call.answer()
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
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
        try:
            if "Ширина" in call.message.text:
                await bot.delete_message(call.message.chat.id, call.message.message_id-1)
            await call.message.delete()
            await bot.send_location(call.message.chat.id, test_locate[key][0][0], test_locate[key][0][1])
            await call.message.answer(msg, reply_markup=locate_geo_category_keyboard)
        except Exception: pass