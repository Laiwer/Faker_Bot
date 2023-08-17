from loader import dp
from aiogram import types
from keyboards.default.generate_kb import generate_keyboard, personality_generate_keyboard, economy_generate_keyboard, \
    technology_generate_keyboard, fun_generate_keyboard, different_generate_keyboard
from keyboards.default.main import main_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import existe_in_db, add_last_message, get_data_from_user


@dp.message_handler(lambda message: not existe_in_db("user", message.chat.id) or not existe_in_db("geolocate", message.chat.id) or get_data_from_user(message.chat.id)[4] == 1)
async def check_in_database(message: types.Message):
    add_last_message(message.chat.id)
    await message.answer("ℹ Отправьте боту /start")


@dp.callback_query_handler(lambda call: not existe_in_db("user", call.message.chat.id) or not existe_in_db("geolocate", call.message.chat.id) or get_data_from_user(call.message.chat.id)[4] == 1)
async def check_in_database(call: types.CallbackQuery):
    add_last_message(call.message.chat.id)
    await call.answer("ℹ Отправьте боту /start", show_alert=True)


@dp.message_handler(text="🎞 Сгенерировать")
async def pin_keyboard(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)


@dp.message_handler(text="👤 Личность")
async def keyboard_personaly(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("👤 Личность", reply_markup=personality_generate_keyboard)


@dp.message_handler(text="💰 Экономика")
async def keyboard_personaly(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("💰 Экономика", reply_markup=economy_generate_keyboard)


@dp.message_handler(text="🤖 Технологии")
async def keyboard_personaly(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("🤖 Технологии", reply_markup=technology_generate_keyboard)


@dp.message_handler(text="🪄 Развлечения")
async def keyboard_personaly(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("🪄 Развлечения", reply_markup=fun_generate_keyboard)


@dp.message_handler(text="⛓ Разное")
async def keyboard_personaly(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⛓ Разное", reply_markup=different_generate_keyboard)


@dp.message_handler(text="◀ Вернутся к категориям")
async def back_to_category(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)


@dp.message_handler(text="⏪ Вернуться на главную")
async def back_to_main(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⏺ Главная страница", reply_markup=main_keyboard)