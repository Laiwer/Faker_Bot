from aiogram import types, Router, F
from keyboards.default.generate_kb import generate_keyboard, personality_generate_keyboard, economy_generate_keyboard, \
    fun_generate_keyboard, different_generate_keyboard, technology_generate_keyboard
from keyboards.default.main import main_keyboard


router = Router()


@router.message(F.text == "🎞 Сгенерировать")
async def pin_keyboard(message: types.Message):
    await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)


@router.message(F.text == "👤 Личность")
async def keyboard_personaly(message: types.Message):
    await message.answer("👤 Личность", reply_markup=personality_generate_keyboard)


@router.message(F.text == "💰 Экономика")
async def keyboard_personaly(message: types.Message):
    await message.answer("💰 Экономика", reply_markup=economy_generate_keyboard)


@router.message(F.text == "🤖 Технологии")
async def keyboard_personaly(message: types.Message):
    await message.answer("🤖 Технологии", reply_markup=technology_generate_keyboard)


@router.message(F.text == "🪄 Развлечения")
async def keyboard_personaly(message: types.Message):
    await message.answer("🪄 Развлечения", reply_markup=fun_generate_keyboard)


@router.message(F.text == "⛓ Разное")
async def keyboard_personaly(message: types.Message):
    await message.answer("⛓ Разное", reply_markup=different_generate_keyboard)


@router.message(F.text == "◀ Вернутся к категориям")
async def back_to_category(message: types.Message):
    await message.answer("⏬ Выбирай снизу, что генерировать", reply_markup=generate_keyboard)


@router.message(F.text == "⏪ Вернуться на главную")
async def back_to_main(message: types.Message):
    await message.answer("⏺ Главная страница", reply_markup=main_keyboard)
