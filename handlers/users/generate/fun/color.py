from aiogram import types
from loader import dp, fake
from database.base import add_last_message
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel
from keyboards.inline.generate.fun.color_kb import color_category_keyboard
from keyboards.callbacks.generate.fun.callback_color import color_inline_callback
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="🎨 Цвет")
async def main_color(message: types.Message):
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=color_category_keyboard)


@dp.callback_query_handler(color_inline_callback.filter(_pass="_"))
async def color_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
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
        try:
            await call.message.edit_text(msg, reply_markup=color_category_keyboard)
        except MessageNotModified: pass