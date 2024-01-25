from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


check_subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📰 Новостной канал", url="https://t.me/bots_rooms")
        ],
        [
            InlineKeyboardButton(text="✅ Проверить подписку", callback_data="check_subscribe_on_news_channel")
        ],
    ]
)