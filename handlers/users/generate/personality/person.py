from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.person.person_kb import person_category_keyboard


router = Router()


@router.message(F.text == "🧑 Человек")
async def main_person(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=person_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "person"))
async def person_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    text = ""
    data = fake.profile()
    text += f"<i>Имя:</i> <code>{data['name']}</code>"
    text += f"\n<i>Почта:</i> <code>{data['mail']}</code>"
    text += f"\n<i>Никнейм:</i> <code>{data['username']}</code>"
    text += f"\n<i>Дата рождения:</i> <code>{data['birthdate']}</code>"
    text += f"\n<i>Адрес:</i> <code>{data['address']}</code>"
    if "profile" in call.data:
        text += f"\n<i>Группа крови:</i> <code>{data['blood_group']}</code>"
        text += f"\n<i>Местоположение:</i> <code>{', '.join([str(float(i)) for i in data['current_location']])}</code>"
        text += f"\n<i>Профессия:</i> <code>{data['job']}</code>"
        text += f"\n<i>Компания:</i> <code>{data['company']}</code>"
    test_person = {
        "profile": f"<b><i>Профиль:</i></b>\n{text}",
        "simple_prof": f"<b><i>Упрощённый профиль:</i></b>\n{text}",
    }
    msg = ""
    for i in test_person:
        if i in call.data:
            msg += test_person[i]
    await call.message.edit_text(msg, reply_markup=person_category_keyboard())