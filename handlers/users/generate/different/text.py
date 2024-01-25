from aiogram import types, Router, F
from faker import Faker
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData
from keyboards.inline.generate.different.text_kb import text_category_keyboard, text_letters_category_keyboard, text_words_category_keyboard, \
    text_sentences_category_keyboard
from random import randint, choice


router = Router()
choice_msg = "Выбери снизу ⬇"


@router.message(F.text == "📖 Текст")
async def main_text(message: types.Message):
    await message.answer(choice_msg, reply_markup=text_category_keyboard())


@router.callback_query(GenerateCategory.filter(F.type == "text"))
async def text_category(call: types.CallbackQuery, callback_data: GenerateCategory):
    await call.answer()
    if callback_data.category == "letter":
        await call.message.edit_text(choice_msg, reply_markup=text_letters_category_keyboard())
    elif callback_data.category == "word":
        await call.message.edit_text(choice_msg, reply_markup=text_words_category_keyboard())
    elif callback_data.category == "sentence":
        await call.message.edit_text(choice_msg, reply_markup=text_sentences_category_keyboard())


@router.callback_query(GenerateData.filter(F.type == "text"))
async def text_category_data(call: types.CallbackQuery, callback_data: GenerateData, fake: Faker):
    await call.answer()
    if callback_data.back:
        await call.message.edit_text(choice_msg, reply_markup=text_category_keyboard())
        return
    elif callback_data.category == "letter":
        lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        test_text = {
            "random_letter": f"<b><i>Случайная буква (строчная, заглавная):</i></b>\n<code>{choice(lower + upper)}</code>",
            "random_lower_letter": f"<b><i>Случайная строчная буква:</i></b>\n<code>{choice(lower)}</code>",
            "random_upper_letter": f"<b><i>Случайная заглавная буква:</i></b>\n<code>{choice(upper)}</code>",
            "letters_random": f"<b><i>Случайные буквы (до 20):</i></b>\n<code>{' '.join(choice(lower + upper) for _ in range(randint(5, 20)))}</code>",
        }
        keyboard = text_letters_category_keyboard()
    elif callback_data.category == "word":
        test_text = {
            "random_word": f"<b><i>Случайное слово (всего 500):</i></b>\n<code>{fake.word()}</code>",
            "words": f"<b><i>Случайные слова (до 10):</i></b>\n<code>{' '.join(fake.words(nb=randint(2, 10)))}</code>",
        }
        keyboard = text_words_category_keyboard()
    elif callback_data.category == "sentence":
        test_text = {
            "paragraph": f"<b><i>Случайный параграф (до 8 предложений):</i></b>\n<code>{fake.paragraph(nb_sentences=randint(1, 8))}</code>",
            "random_sentence": f"<b><i>Случайное предложение (до 15 слов):</i></b>\n<code>{fake.sentence(nb_words=randint(3, 15))}</code>",
            "sentences": f"<b><i>Случайные предложения (до 5):</i></b>\n<code>{' '.join(fake.sentences(nb=randint(2, 5)))}</code>",
            "texts": f"<b><i>Случайный текст (до 1000 символов):</i></b>\n<code>{fake.text(max_nb_chars=1000)}</code>",
        }
        keyboard = text_sentences_category_keyboard()
    msg = ""
    for i in test_text:
        if i in call.data:
            msg += test_text[i]
    await call.message.edit_text(msg, reply_markup=keyboard)