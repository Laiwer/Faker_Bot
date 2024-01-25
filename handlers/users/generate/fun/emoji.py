from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.fun.emoji_kb import emoji_category_keyboard


router = Router()


@router.message(F.text == "🎭 Эмодзи")
async def main_emoji(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=emoji_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "emoji"))
async def emoji_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    await call.message.edit_text(f"<b><i>Случайный эмодзи:</i></b>\n<code>{fake.emoji()}</code>", reply_markup=emoji_category_keyboard())