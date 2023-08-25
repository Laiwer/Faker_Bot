from aiogram import types
from loader import dp, fake
from database.base import add_last_message
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from keyboards.inline.generate.person.person_kb import person_category_keyboard
from keyboards.callbacks.generate.personality.callback_person import person_inline_callback
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="🧑 Человек")
async def main_person(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=person_category_keyboard)


@dp.callback_query_handler(person_inline_callback.filter(_pass="_"))
async def person_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        text = ""
        if "profile" in call.data:
            data = fake.profile()
            text += f"<i>Имя:</i> <code>{data['name']}</code>"
            text += f"\n<i>Дата рождения:</i> <code>{data['birthdate']}</code>"
            text += f"\n<i>Группа крови:</i> <code>{data['blood_group']}</code>"
            text += f"\n<i>Адрес:</i> <code>{data['address']}</code>"
            text += f"\n<i>Местоположение:</i> <code>{', '.join([str(float(i)) for i in data['current_location']])}</code>"
            text += f"\n<i>Профессия:</i> <code>{data['job']}</code>"
            text += f"\n<i>Компания:</i> <code>{data['company']}</code>"
            text += f"\n<i>Почта:</i> <code>{data['mail']}</code>"
            text += f"\n<i>Никнейм:</i> <code>{data['username']}</code>"
        else:
            data = fake.simple_profile()
            text += f"<i>Имя:</i> <code>{data['name']}</code>"
            text += f"\n<i>Дата рождения:</i> <code>{data['birthdate']}</code>"
            text += f"\n<i>Адрес:</i> <code>{data['address']}</code>"
            text += f"\n<i>Почта:</i> <code>{data['mail']}</code>"
            text += f"\n<i>Никнейм:</i> <code>{data['username']}</code>"
        test_person = {
            "profile": f"<b><i>Профиль:</i></b>\n{text}",
            "simple_prof": f"<b><i>Упрощённый профиль:</i></b>\n{text}",
        }
        msg = ""
        for i in test_person:
            if i in call.data:
                msg += test_person[i]
        try:
            await call.message.edit_text(msg, reply_markup=person_category_keyboard)
        except MessageNotModified: pass