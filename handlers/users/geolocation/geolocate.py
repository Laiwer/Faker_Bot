from aiogram import types, F, Router, Bot
from aiogram.fsm.context import FSMContext
from geopy.geocoders import Nominatim
from keyboards.callbacks.geolocation.geolocation_category import GeolocationCategory
from keyboards.callbacks.geolocation.geolocation_data import GeolocationData
from keyboards.inline.geolocation.geolocate_kb import geolocation_choice, geolocation_address_choice
from db.base import update_data_in_geolocate, get_data_from_geolocate
from states.geolocate_state import GeolocateSearch
from data.list_answer_bot import NUMBER_ANSWER as NUM_ANSWER
from keyboards.default.back_from_state_geo_kb import back_to_main
from keyboards.default.main import main_keyboard


router = Router()


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


@router.message(F.text == "🌎 Местоположение")
async def geo_locate_main(message: types.Message):
    await message.answer("🔽 Выбери входные данные", reply_markup=geolocation_choice())


@router.message(F.text == "⏪ Вернуться")
async def error_return_to_choice(message: types.Message):
    await message.answer("⏺ Главная страница", reply_markup=main_keyboard)


@router.callback_query(F.data == "______")
async def number_callback(call: types.CallbackQuery):
    await call.answer("🔢 Страницы")


@router.callback_query(GeolocationCategory.filter(F.category == "obj_address"))
async def geocation_address(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("🔽 Выбери категорию, которая больше подходит под запрос для точности поиска\n🤓 Бот плохо ищет природные объекты (леса, горы, острова и т.д.)", reply_markup=geolocation_address_choice())


@router.callback_query(GeolocationData.filter(F.category == "obj_address"))
async def search_geolocate(call: types.CallbackQuery, callback_data: GeolocationData, state: FSMContext):
    await call.answer()
    update_data_in_geolocate(call.message.chat.id, "type_data", callback_data.data)
    if callback_data.back:
        await call.message.edit_text("🔽 Выбери входные данные", reply_markup=geolocation_choice())
    elif callback_data.category == "obj_address":
        msg_geolocate = {
            "adddress": "⬇ Введите адрес или название объекта",
            "city": "⬇ Введите название города",
            "country": "⬇ Введите название страны",
            "postalcode": "⬇ Введите почтовый индекс",
            "coordinate": "⬇ Введите координаты широты и долготы через пробел (-90 - 90, -180 - 180)",
            "point": "⬇ Скиньте геопозицию",
        }
        msg = ""
        for i in msg_geolocate:
            if i in call.data:
                msg += msg_geolocate[i]

        await call.message.delete()
        await call.message.answer(msg, reply_markup=back_to_main)
        await state.set_state(GeolocateSearch.Q1)


@router.message(GeolocateSearch.Q1, F.content_type.in_(["location", "text"]))
async def search_geolocate_q1(message: types.Message, state: FSMContext, geolocator: Nominatim):
    correct_msg = "✅ Данные приняты!"
    location = 0
    if message.text == "⏪ Вернуться":
        await message.answer("⏺ Главная страница", reply_markup=main_keyboard)
        return
    if get_data_from_geolocate(message.chat.id)[0] in ["adddress", "city", "country", "postalcode"]:
        update_data_in_geolocate(message.chat.id, "request_user", message.text)
        data = get_data_from_geolocate(message.chat.id)
        post = {}
        if data[0] == "adddress":
            post = data[1]
        else:
            post = {data[0]: data[1]}
        update_data_in_geolocate(message.chat.id, "request_user", data[1])
        location = geolocator.geocode(post, exactly_one=False, addressdetails=True, language="ru")
        await message.answer(correct_msg, reply_markup=main_keyboard)
    elif get_data_from_geolocate(message.chat.id)[0] == "coordinate":
        if len(message.text.split(" ")) == 2:
            if is_number(message.text.replace(",", ".").split(" ")[0]) and is_number(message.text.replace(",", ".").split(" ")[1]):
                coord = message.text.replace(",", ".").split(" ")
                if (float(coord[0]) <= 90 and float(coord[0]) >= -90) and (float(coord[1]) <= 180 and float(coord[1]) >= -180):
                    msg = message.text.replace(",", ".")
                    update_data_in_geolocate(message.chat.id, "request_user", msg)
                    location = geolocator.reverse(msg.split(" "), exactly_one=True, addressdetails=True, language="ru")
                    await message.answer(correct_msg, reply_markup=main_keyboard)
                else:
                    await message.answer("🔃 Введите сначала широту (в диапазоне -90 - 90), а затем долготу (-180 - 180)")
            else:
                await message.answer("🔢 Введите число или десятичное число")
        else:
            await message.answer("🔀 Введите два числа (широта и долгота)")
    elif get_data_from_geolocate(message.chat.id)[0] == "point":
        try:
            tmp = f"{message.location.latitude} {message.location.longitude}"
            update_data_in_geolocate(message.chat.id, "request_user", tmp)
            location = geolocator.reverse(tmp.split(" "), exactly_one=True, addressdetails=True, language="ru")
            await message.answer(correct_msg, reply_markup=main_keyboard)
        except Exception:
            await message.answer("🧭 Скиньте геопозицию (нажмите на скрепку)")

    if location != 0:
        if location is None:
            if get_data_from_geolocate(message.chat.id)[0] == "adddress":
                await message.answer("🚫 Не получилось найти такой объект или адрес")
            elif get_data_from_geolocate(message.chat.id)[0] in ["coordinate", "point"]:
                coords = get_data_from_geolocate(message.chat.id)[1].split(" ")
                await message.answer_location(coords[0], coords[1])
                if location is None:
                    await message.answer("🌊 Скорее всего точка находится в море или океане")
            else:
                await message.answer("🚫 Не получилось найти такой объект или адрес\n🔎 Попробуйте поискать в <b><i>🌏 Любой адрес или объект</i></b>")
        else:
            data = get_data_from_geolocate(message.chat.id)
            try:
                update_data_in_geolocate(message.chat.id, "max_index", 10 if len(location) > 10 else len(location))
            except TypeError:
                update_data_in_geolocate(message.chat.id, "max_index", 1)
            if data[0] in ["coordinate", "point"]:
                update_data_in_geolocate(message.chat.id, "max_index", 1)
            update_data_in_geolocate(message.chat.id, "now_index", 0)
            data = get_data_from_geolocate(message.chat.id)
            if data[3] == 1:
                num_list = f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}"
                inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[[
                    types.InlineKeyboardButton(text=num_list, callback_data="______")
                ]])
            else:
                num_list = f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}"
                inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[
                    [types.InlineKeyboardButton(text="⏩", callback_data=">>>>>>")],
                    [types.InlineKeyboardButton(text=num_list, callback_data="______")]
                ])
            
            if data[0] == "address":
                location = geolocator.geocode(data[1], exactly_one=False, addressdetails=True, language="ru")
            elif data[0] in ["coordinate", "point"]:
                location = geolocator.reverse(data[1].split(" "), exactly_one=True, addressdetails=True, language="ru")
            else:
                location = geolocator.geocode({data[0]: data[1]}, exactly_one=False, addressdetails=True, language="ru")
            
            
            if data[0] in ["coordinate", "point"]:
                if data[0] == "point":
                    await message.delete()
                await message.answer_location(location[-1][0], location[-1][1])
                msg = f"<code>{str(location[-1])[1:-1]}</code>\n"
                for i in location[0].split(', '):
                    msg += f"\n<code>{i}</code>"
                await message.answer(msg, reply_markup=inline_kb)
            else:
                await message.answer_location(location[data[2]][-1][0], location[data[2]][-1][1])
                msg = f"<code>{str(location[data[2]][-1])[1:-1]}</code>\n"
                for i in location[0][0].split(', '):
                    msg += f"\n<code>{i}</code>"
                await message.answer(msg, reply_markup=inline_kb)
        await state.clear()


@router.callback_query(F.data.in_(["<<<<<<", ">>>>>>"]))
async def next_or_previous_page(call: types.CallbackQuery, geolocator: Nominatim, bot: Bot):
    await call.answer()
    if call.data == ">>>>>>" and get_data_from_geolocate(call.message.chat.id)[2]+1 != 10:
        edit_page = 1
    elif call.data == "<<<<<<" and get_data_from_geolocate(call.message.chat.id)[2] != 0:
        edit_page = -1
    update_data_in_geolocate(call.message.chat.id, "now_index", get_data_from_geolocate(call.message.chat.id)[2] + edit_page)
    data = get_data_from_geolocate(call.message.chat.id)
    num_list = f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}"
    inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text="⏪", callback_data="<<<<<<"),
        types.InlineKeyboardButton(text="⏩", callback_data=">>>>>>")],
        [types.InlineKeyboardButton(text=num_list, callback_data="______")]
    ])
    if call.data == ">>>>>>":
        if get_data_from_geolocate(call.message.chat.id)[2]+1 != 10:
            await call.message.delete()
            await bot.delete_message(call.message.chat.id, call.message.message_id-1)
            data = get_data_from_geolocate(call.message.chat.id)
            if data[2]+1 == data[3]:
                num_list = f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}"
                inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[
                    [types.InlineKeyboardButton(text="⏪", callback_data="<<<<<<")],
                    [types.InlineKeyboardButton(text=num_list, callback_data="______")]
                ])
    elif call.data == "<<<<<<":
        if get_data_from_geolocate(call.message.chat.id)[2] >= 0:
            await call.message.delete()
            await bot.delete_message(call.message.chat.id, call.message.message_id-1)
            data = get_data_from_geolocate(call.message.chat.id)
            if data[2] == 0:
                num_list = f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}"
                inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[
                    [types.InlineKeyboardButton(text="⏩", callback_data=">>>>>>")],
                    [types.InlineKeyboardButton(text=num_list, callback_data="______")]
                ])
    if data[0] == "adddress":
        location = geolocator.geocode(data[1], exactly_one=False, addressdetails=True, language="ru")
    else:
        location = geolocator.geocode({data[0]: data[1]}, exactly_one=False, addressdetails=True, language="ru")
    await call.message.answer_location(location[data[2]][-1][0], location[data[2]][-1][1])
    msg = f"<code>{str(location[data[2]][-1])[1:-1]}</code>\n"
    for i in location[data[2]][0].split(', '):
        msg += f"\n<code>{i}</code>"
    await call.message.answer(msg, reply_markup=inline_kb)