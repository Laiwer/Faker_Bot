from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bank_card_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("💳 Банковская карта", callback_data="bank_card:_:card_bank")
        ],
        [
            InlineKeyboardButton("💰 Платёжная система", callback_data="bank_card:_:pay_system")
        ],
        [
            InlineKeyboardButton("🏦 Банк", callback_data="bank_card:_:name_bank")
        ],
        [
            InlineKeyboardButton("🔢 Номер карты", callback_data="bank_card:_:id_card")
        ],
        [
            InlineKeyboardButton("🗓 Дата карты", callback_data="bank_card:_:date_card")
        ],
        [
            InlineKeyboardButton("🤫 Код безопасности", callback_data="bank_card:_:cvv")
        ],
    ]
)