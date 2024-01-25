from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.fun.color_kb import color_category_keyboard


router = Router()


@router.message(F.text == "🎨 Цвет")
async def main_color(message: types.Message):
    await message.answer("Выбери снизу ⬇", reply_markup=color_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "color"))
async def color_data(call: types.CallbackQuery, fake: Faker):
    await call.answer()
    test_color = {
        "name_color": f"<b><i>Название цвета:</i></b>\n<code>{fake.color_name()}</code>",
        "hex_color": f"<b><i>Hex цвет (#FFFFFF):</i></b>\n<code>{fake.hex_color()}</code>",
        "rgb_color": f"<b><i>RGB цвет (256,256,256):</i></b>\n<code>{fake.rgb_color()}</code>",
        "rgb_css_color": f"<b><i>RGB CSS цвет (rgb(256,256,256)):</i></b>\n<code>{fake.rgb_css_color()}</code>"
    }
    msg = ""
    for i in test_color:
        if i in call.data:
            msg += test_color[i]
    await call.message.edit_text(msg, reply_markup=color_category_keyboard())
