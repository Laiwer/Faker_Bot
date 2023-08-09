from loader import dp
from aiogram import types
from keyboards.default.generate_kb import generate_keyboard
from keyboards.default.main import main_keyboard
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from database.base import existe_in_db


@dp.message_handler(lambda message: not existe_in_db("user", message.chat.id) or not existe_in_db("geolocate", message.chat.id))
async def check_in_database(message: types.Message):
    await message.answer("ℹ Отправьте боту /start")


@dp.callback_query_handler(lambda call: not existe_in_db("user", call.message.chat.id) or not existe_in_db("geolocate", call.message.chat.id))
async def check_in_database(call: types.CallbackQuery):
    await call.answer("ℹ Отправьте боту /start", show_alert=True)


@dp.message_handler(text="🎞 Сгенерировать")
async def pin_keyboard(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)


@dp.message_handler(text="⏪ Вернуться на главную")
async def back_to_main(message: types.Message):
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("⏺ Главная страница", reply_markup=main_keyboard)