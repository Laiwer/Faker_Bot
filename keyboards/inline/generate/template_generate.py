from aiogram.utils.keyboard import InlineKeyboardBuilder


def template_generate_inline_kb(buttons: dict):
    keyboard_builder = InlineKeyboardBuilder()
    for button in buttons:
        keyboard_builder.button(text=button, callback_data=buttons[button])
    keyboard_builder.adjust(1, repeat=True)
    return keyboard_builder.as_markup()