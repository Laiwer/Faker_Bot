from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


back_to_menu_button = InlineKeyboardButton("⏪ Назад", callback_data="back_to_text_category")

text_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🅰️ Буквы", callback_data="text_letters")
        ],
        [
            InlineKeyboardButton("🆗 Слова", callback_data="text_words")
        ],
        [
            InlineKeyboardButton("📋 Предложения", callback_data="text_sentences")
        ]
    ]
)

text_letters_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🅱️ Случайная буква", callback_data="text:letter:random_letter")
        ],
        [
            InlineKeyboardButton("🔡 Строчная буква", callback_data="text:letter:random_lower_letter")
        ],
        [
            InlineKeyboardButton("🔠 Заглавная буква", callback_data="text:letter:random_upper_letter")
        ],
        [
            InlineKeyboardButton("🆎 Случайные буквы", callback_data="text:letter:letters_random")
        ],
        [
            back_to_menu_button
        ]
    ]
)

text_words_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🆕 Случайное слово", callback_data="text:word:random_word")
        ],
        [
            InlineKeyboardButton("🆓 Случайные слова", callback_data="text:word:words")
        ],
        [
            back_to_menu_button
        ]
    ]
)

text_sentences_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📝 Параграф", callback_data="text:sentence:paragraph")
        ],
        [
            InlineKeyboardButton("📄 Предложение", callback_data="text:sentence:random_sentence")
        ],
        [
            InlineKeyboardButton("📑 Предложения", callback_data="text:sentence:sentences")
        ],
        [
            InlineKeyboardButton("📖 Текст", callback_data="text:sentence:texts")
        ],
        [
            back_to_menu_button
        ]
    ]
)