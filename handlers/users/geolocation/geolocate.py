from loader import dp, bot, geolocator
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from keyboards.inline.geolocation.geolocate_kb import geolocation_choice, geolocation_address_choice
from keyboards.callbacks.geolocation.callback_geolocate import geolocate_inline_callback
from database.base import add_last_message, update_data_in_geolocate, get_data_from_geolocate, existe_in_db, \
add_user_in_geolocate
from states.geolocate_state import geolocate_search
from data.list_answer_bot import NUMBER_ANSWER as NUM_ANSWER
from keyboards.default.back_from_state_geo_kb import back_to_main
from keyboards.default.main import main_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action, bot_action_location
from aiogram.utils.exceptions import MessageNotModified


def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


@dp.message_handler(text="🌎 Местоположение")
async def geo_locate_main(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("🔽 Выбери входные данные", reply_markup=geolocation_choice)


@dp.callback_query_handler(text="geolocate_obj_addr")
async def geocation_address(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("🔽 Выбери категорию, которая больше подходит под запрос для точности поиска\n🤓 Бот плохо ищет природные объекты (леса, горы, острова и т.д.)", reply_markup=geolocation_address_choice)


@dp.callback_query_handler(text="back_to_geolocation_choice")
async def back_to_geolocation_choice(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("🔽 Выбери входные данные", reply_markup=geolocation_choice)


@dp.message_handler(state=geolocate_search.Q1, text="⏪ Вернуться")
async def return_to_geolocate_choice(message: types.Message, state: FSMContext):
    await bot_action(message)
    add_last_message(message.chat.id)
    await message.answer("⏺ Главная страница", reply_markup=main_keyboard)
    await state.finish()


@dp.message_handler(text="⏪ Вернуться")
async def error_return_to_choice(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    await message.answer("⏺ Главная страница", reply_markup=main_keyboard)


@dp.callback_query_handler(geolocate_inline_callback.filter(_pass="_"))
async def search_geolocate(call: types.CallbackQuery):
    await bot_action(call.message)
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.message.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        update_data_in_geolocate(call.message.chat.id, "type_data", call.data[12:])
        msg_geolocate = {
            "address": "⬇ Введите адрес или название объекта",
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

        await bot.delete_message(call.message.chat.id, call.message.message_id)
        await call.message.answer(msg, reply_markup=back_to_main)
        await geolocate_search.Q1.set()


@dp.message_handler(state=geolocate_search.Q1, content_types=[types.ContentType.LOCATION, types.ContentType.TEXT])
async def search_geolocate_q1(message: types.Message, state: FSMContext):
    await bot_action(message)
    add_last_message(message.chat.id)
    location = 0
    if get_data_from_geolocate(message.chat.id)[0] in ["address", "city", "country", "postalcode"]:
        update_data_in_geolocate(message.chat.id, "request_user", message.text)
        data = get_data_from_geolocate(message.chat.id)
        post = {}
        if data[0] == "address":
            post = data[1]
        else:
            post = {data[0]: data[1]}
        update_data_in_geolocate(message.chat.id, "request_user", data[1])
        location = geolocator.geocode(post, exactly_one=False, addressdetails=True, language="ru")
        await message.answer("✅ Данные приняты!", reply_markup=main_keyboard)
    elif get_data_from_geolocate(message.chat.id)[0] == "coordinate":
        if len(message.text.split(" ")) == 2:
            if is_number(message.text.replace(",", ".").split(" ")[0]) and is_number(message.text.replace(",", ".").split(" ")[1]):
                coord = message.text.replace(",", ".").split(" ")
                if (float(coord[0]) <= 90 and float(coord[0]) >= -90) and (float(coord[1]) <= 180 and float(coord[1]) >= -180):
                    msg = message.text.replace(",", ".")
                    update_data_in_geolocate(message.chat.id, "request_user", msg)
                    location = geolocator.reverse(msg.split(" "), exactly_one=True, addressdetails=True, language="ru")
                    await message.answer("✅ Данные приняты!", reply_markup=main_keyboard)
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
            await message.answer("✅ Данные приняты!", reply_markup=main_keyboard)
        except Exception:
            await message.answer("🧭 Скиньте геопозицию (нажмите на скрепку)")

    await bot_action(message)
    if location != 0:
        if location is None:
            if get_data_from_geolocate(message.chat.id)[0] == "address":
                await message.answer("🚫 Не получилось найти такой объект или адрес")
            elif get_data_from_geolocate(message.chat.id)[0] in ["coordinate", "point"]:
                coords = get_data_from_geolocate(message.chat.id)[1].split(" ")
                await bot_action_location(message)
                await message.answer_location(coords[0], coords[1])
                if location is None:
                    await bot_action(message)
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
                inline_kb = types.InlineKeyboardMarkup(row_width=1)
                inline_kb.insert(types.InlineKeyboardButton(f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}", callback_data="______"))
            else:
                inline_kb = types.InlineKeyboardMarkup(row_width=1)
                inline_kb.insert(types.InlineKeyboardButton("⏩", callback_data=">>>>>>"))
                inline_kb.insert(types.InlineKeyboardButton(f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}", callback_data="______"))
            
            if data[0] == "address":
                location = geolocator.geocode(data[1], exactly_one=False, addressdetails=True, language="ru")
            elif data[0] in ["coordinate", "point"]:
                location = geolocator.reverse(data[1].split(" "), exactly_one=True, addressdetails=True, language="ru")
            else:
                location = geolocator.geocode({data[0]: data[1]}, exactly_one=False, addressdetails=True, language="ru")
            
            
            if data[0] in ["coordinate", "point"]:
                if data[0] == "point":
                    await bot.delete_message(message.chat.id, message.message_id)
                await bot_action_location(message)
                await message.answer_location(location[-1][0], location[-1][1])
                msg = f"<code>{str(location[-1])[1:-1]}</code>\n"
                for i in location[0].split(', '):
                    msg += f"\n<code>{i}</code>"
                await bot_action(message)
                await message.answer(msg, reply_markup=inline_kb)
            else:
                await bot_action_location(message)
                await message.answer_location(location[data[2]][-1][0], location[data[2]][-1][1])
                msg = f"<code>{str(location[data[2]][-1])[1:-1]}</code>\n"
                for i in location[0][0].split(', '):
                    msg += f"\n<code>{i}</code>"
                await bot_action(message)
                await message.answer(msg, reply_markup=inline_kb)
        await state.finish()


@dp.callback_query_handler(text=">>>>>>")
async def next_page(call: types.CallbackQuery):
    await bot_action(call.message)
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.message.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        if get_data_from_geolocate(call.message.chat.id)[2]+1 != 10:
            update_data_in_geolocate(call.message.chat.id, "now_index", get_data_from_geolocate(call.message.chat.id)[2]+1)

            await bot.delete_message(call.message.chat.id, call.message.message_id-1)
            await bot.delete_message(call.message.chat.id, call.message.message_id)

            data = get_data_from_geolocate(call.message.chat.id)
            if data[2]+1 == data[3]:
                inline_kb = types.InlineKeyboardMarkup(row_width=1)
                inline_kb.insert(types.InlineKeyboardButton("⏪", callback_data="<<<<<<"))
                inline_kb.insert(types.InlineKeyboardButton(f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}", callback_data="______"))
            else:
                inline_kb = types.InlineKeyboardMarkup(row_width=2)
                inline_kb.insert(types.InlineKeyboardButton("⏪", callback_data="<<<<<<"))
                inline_kb.insert(types.InlineKeyboardButton("⏩", callback_data=">>>>>>"))
                inline_kb.insert(types.InlineKeyboardButton(f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}", callback_data="______"))

            if data[0] == "address":
                location = geolocator.geocode(data[1], exactly_one=False, addressdetails=True, language="ru")
            else:
                location = geolocator.geocode({data[0]: data[1]}, exactly_one=False, addressdetails=True, language="ru")
            
            await call.message.answer_location(location[data[2]][-1][0], location[data[2]][-1][1])
            msg = f"<code>{str(location[data[2]][-1])[1:-1]}</code>\n"
            for i in location[data[2]][0].split(', '):
                msg += f"\n<code>{i}</code>"
            await call.message.answer(msg, reply_markup=inline_kb)


@dp.callback_query_handler(text="<<<<<<")
async def previus_page(call: types.CallbackQuery):
    await bot_action(call.message)
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.message.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        if get_data_from_geolocate(call.message.chat.id)[2] != 0:
            update_data_in_geolocate(call.message.chat.id, "now_index", get_data_from_geolocate(call.message.chat.id)[2]-1)
            await bot.delete_message(call.message.chat.id, call.message.message_id-1)
            await bot.delete_message(call.message.chat.id, call.message.message_id)

            data = get_data_from_geolocate(call.message.chat.id)
            if data[2] == 0:
                inline_kb = types.InlineKeyboardMarkup(row_width=1)
                inline_kb.insert(types.InlineKeyboardButton("⏩", callback_data=">>>>>>"))
                inline_kb.insert(types.InlineKeyboardButton(f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}", callback_data="______"))
            else:
                inline_kb = types.InlineKeyboardMarkup(row_width=2)
                inline_kb.insert(types.InlineKeyboardButton("⏪", callback_data="<<<<<<"))
                inline_kb.insert(types.InlineKeyboardButton("⏩", callback_data=">>>>>>"))
                inline_kb.insert(types.InlineKeyboardButton(f"{NUM_ANSWER[data[2]+1]} / {NUM_ANSWER[data[3]]}", callback_data="______"))

            if data[0] == "address":
                location = geolocator.geocode(data[1], exactly_one=False, addressdetails=True, language="ru")
            else:
                location = geolocator.geocode({data[0]: data[1]}, exactly_one=False, addressdetails=True, language="ru")
            
            await call.message.answer_location(location[data[2]][-1][0], location[data[2]][-1][1])
            msg = f"<code>{str(location[data[2]][-1])[1:-1]}</code>\n"
            for i in location[data[2]][0].split(', '):
                msg += f"\n<code>{i}</code>"
            await call.message.answer(msg, reply_markup=inline_kb)


@dp.callback_query_handler(text="______")
async def number_callback(call: types.CallbackQuery):
    await call.answer("🔢 Страницы")
    add_last_message(call.message.chat.id)