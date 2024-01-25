from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.economy.company_kb import company_category_keyboard


router = Router()


@router.message(F.text == "🏢 Компания")
async def main_company(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=company_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "company"))
async def company_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_company = {
        "name_company": f"<b><i>Название маленькой компании:</i></b>\n<code>{fake.company()}</code>",
        "large_company": f"<b><i>Название крупной компании:</i></b>\n<code>{fake.large_company()}</code>",
        "catch_phrase": f"<b><i>Слоган компании:</i></b>\n<code>{fake.catch_phrase()}</code>",
        "activity_company": f"<b><i>Деятельность компании:</i></b>\n<code>{fake.bs()}</code>",
        "inn": f"<b><i>ИНН (Идентификационный номер налогоплательщика):</i></b>\n<code>{fake.businesses_inn()}</code>",
        "ogrn": f"<b><i>ОГРН (Основной государственный регистрационный номер):</i></b>\n<code>{fake.businesses_ogrn()}</code>",
    }
    msg = ""
    for i in test_company:
        if i in call.data:
            msg += test_company[i]
    await call.message.edit_text(msg, reply_markup=company_category_keyboard())