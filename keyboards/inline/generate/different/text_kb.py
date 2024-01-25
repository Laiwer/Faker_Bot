from keyboards.inline.generate.template_generate import template_generate_inline_kb
from keyboards.callbacks.generate.generate_category import GenerateCategory
from keyboards.callbacks.generate.generate_data import GenerateData


back_to_text_category_button = {"⏪ Назад": GenerateData(type="text", category="-", data="-", back=True)}


def text_category_keyboard():
    return template_generate_inline_kb(
        {
            "🅰️ Буквы": GenerateCategory(type="text", category="letter"),
            "🆗 Слова": GenerateCategory(type="text", category="word"),
            "📋 Предложения": GenerateCategory(type="text", category="sentence")
        }
    )


def text_letters_category_keyboard():
    return template_generate_inline_kb(
        {
            "🅱️ Случайная буква": GenerateData(type="text", category="letter", data="random_letter", back=False),
            "🔡 Строчная буква": GenerateData(type="text", category="letter", data="random_lower_letter", back=False),
            "🔠 Заглавная буква": GenerateData(type="text", category="letter", data="random_upper_letter", back=False),
            "🆎 Случайные буквы": GenerateData(type="text", category="letter", data="letters_random", back=False),
            **back_to_text_category_button
        }
    )


def text_words_category_keyboard():
    return template_generate_inline_kb(
        {
            "🆕 Случайное слово": GenerateData(type="text", category="word", data="random_word", back=False),
            "🆓 Случайные слова": GenerateData(type="text", category="word", data="words", back=False),
            **back_to_text_category_button
        }
    )


def text_sentences_category_keyboard():
    return template_generate_inline_kb(
        {
            "📝 Параграф": GenerateData(type="text", category="sentence", data="paragraph", back=False),
            "📄 Предложение": GenerateData(type="text", category="sentence", data="random_sentence", back=False),
            "📑 Предложения": GenerateData(type="text", category="sentence", data="sentences", back=False),
            "📖 Текст": GenerateData(type="text", category="sentence", data="texts", back=False),
            **back_to_text_category_button
        }
    )