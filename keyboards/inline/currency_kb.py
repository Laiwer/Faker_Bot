from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_to_currency_category_button = InlineKeyboardButton("⏪ Назад", callback_data="back_to_currecny_category")

currency_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("💶 Денежная валюта", callback_data="currency_paper")
        ],
        [
            InlineKeyboardButton("📀 Криптовалюта", callback_data="currency_crypto")
        ],
    ]
)


currency_paper_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("💵 Валюта", callback_data="currency:paper:all")
        ],
        [
            InlineKeyboardButton("🪙 Название валюты", callback_data="currency:paper:name_currency")
        ],
        [
            InlineKeyboardButton("📟 Код валюты", callback_data="currency:paper:id_currency")
        ],
        [
            InlineKeyboardButton("💠 Символ валюты", callback_data="currency:paper:symbol_currency")
        ],
        [
            InlineKeyboardButton("📶 Кол-во денег", callback_data="currency:paper:number_paper")
        ],
        [
            back_to_currency_category_button
        ]
    ]
)

currency_crypto_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("💿 Криптовалюта", callback_data="currency:crypto:all")
        ],
        [
            InlineKeyboardButton("⚙️ Название криптовалюты", callback_data="currency:crypto:name_currency")
        ],
        [
            InlineKeyboardButton("📟 Код криптовалюты", callback_data="currency:crypto:id_currency")
        ],
        [
            back_to_currency_category_button
        ]
    ]
)