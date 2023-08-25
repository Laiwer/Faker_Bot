from aiogram import types
from loader import dp, fake
from database.base import add_last_message
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from keyboards.inline.generate.different.text_kb import text_category_keyboard, text_letters_category_keyboard, text_words_category_keyboard, \
    text_sentences_category_keyboard
from keyboards.callbacks.generate.different.callback_text import text_inline_callback
from random import randint, choice
from aiogram.utils.exceptions import MessageNotModified


@dp.message_handler(text="📖 Текст")
async def main_locate(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    if not await check_sub_channel(message.from_user.id):
        await keyboard_check_channel(message)
    else:
        await message.answer("Выбери снизу ⬇", reply_markup=text_category_keyboard)


@dp.callback_query_handler(text="text_letters")
async def text_letter_keyboard(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=text_letters_category_keyboard)


@dp.callback_query_handler(text="text_words")
async def text_word_keyboard(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=text_words_category_keyboard)


@dp.callback_query_handler(text="text_sentences")
async def text_sentence_keyboard(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=text_sentences_category_keyboard)


@dp.callback_query_handler(text="back_to_text_category")
async def back_to_text_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    await call.message.edit_text("Выбери снизу ⬇", reply_markup=text_category_keyboard)


@dp.callback_query_handler(text_inline_callback.filter(type="letter"))
async def text_letter_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        test_text = {
            "random_letter": f"<b><i>Случайная буква (строчная, заглавная):</i></b>\n<code>{choice(lower + upper)}</code>",
            "random_lower_letter": f"<b><i>Случайная строчная буква:</i></b>\n<code>{choice(lower)}</code>",
            "random_upper_letter": f"<b><i>Случайная заглавная буква:</i></b>\n<code>{choice(upper)}</code>",
            "letters_random": f"<b><i>Случайные буквы (до 20):</i></b>\n<code>{' '.join(choice(lower + upper) for _ in range(randint(5, 20)))}</code>",
        }
        msg = ""
        for i in test_text:
            if i in call.data:
                msg += test_text[i]
        try:
            await call.message.edit_text(msg, reply_markup=text_letters_category_keyboard)
        except MessageNotModified: pass


@dp.callback_query_handler(text_inline_callback.filter(type="word"))
async def text_word_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_text = {
            "random_word": f"<b><i>Случайное слово (всего 500):</i></b>\n<code>{fake.word()}</code>",
            "words": f"<b><i>Случайные слова (до 10):</i></b>\n<code>{' '.join(fake.words(nb=randint(2, 10)))}</code>",
        }
        msg = ""
        for i in test_text:
            if i in call.data:
                msg += test_text[i]
        try:
            await call.message.edit_text(msg, reply_markup=text_words_category_keyboard)
        except MessageNotModified: pass


@dp.callback_query_handler(text_inline_callback.filter(type="sentence"))
async def text_sentence_category(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    if not await check_sub_channel(call.from_user.id):
        await keyboard_check_channel(call.message)
    else:
        test_text = {
            "paragraph": f"<b><i>Случайный параграф (до 8 предложений):</i></b>\n<code>{fake.paragraph(nb_sentences=randint(1, 8))}</code>",
            "random_sentence": f"<b><i>Случайное предложение (до 15 слов):</i></b>\n<code>{fake.sentence(nb_words=randint(3, 15))}</code>",
            "sentences": f"<b><i>Случайные предложения (до 5):</i></b>\n<code>{' '.join(fake.sentences(nb=randint(2, 5)))}</code>",
            "texts": f"<b><i>Случайный текст (до 1000 символов):</i></b>\n<code>{fake.text(max_nb_chars=1000)}</code>",
        }
        msg = ""
        for i in test_text:
            if i in call.data:
                msg += test_text[i]
        try:
            await call.message.edit_text(msg, reply_markup=text_sentences_category_keyboard)
        except MessageNotModified: pass