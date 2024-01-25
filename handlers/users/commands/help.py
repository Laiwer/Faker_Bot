from aiogram import types, Router, F
from keyboards.inline.commands.help_kb import instruction_help_category_keyboard, all_generate_menu_category_keyboard
from aiogram.filters.command import Command
from aiogram.exceptions import TelegramBadRequest
from data.list_answer_bot import ANSWER_HELP, ANSWER_HELP_PAGE1, ANSWER_HELP_PAGE2, ANSWER_HELP_PAGE3, ANSWER_HELP_PAGE4


router = Router()


@router.message(Command("help"))
async def command_help_mes(message: types.Message):
    await message.answer(ANSWER_HELP, reply_markup=all_generate_menu_category_keyboard, disable_web_page_preview=True)


@router.callback_query(F.data == "instruction_help")
async def command_help_call(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text(ANSWER_HELP, reply_markup=all_generate_menu_category_keyboard, disable_web_page_preview=True)


@router.callback_query(F.data.contains("all_generate_menu"))
async def command_help_page1(call: types.CallbackQuery):
    await call.answer()
    msg = ""
    if "1" in call.data:
        msg = ANSWER_HELP_PAGE1

    elif "2" in call.data:
        msg = ANSWER_HELP_PAGE2

    elif "3" in call.data:
        msg = ANSWER_HELP_PAGE3

    elif "4" in call.data:
        msg = ANSWER_HELP_PAGE4

    try:
        await call.message.edit_text(msg, reply_markup=instruction_help_category_keyboard)
    except TelegramBadRequest:
        pass