from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


check_subscribe_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("📰 Новостной канал", url="https://t.me/+xd9OwxKOK2I3NjYy")
        ],
        [
            InlineKeyboardButton("✅ Проверить подписку", callback_data="check_subscribe_on_news_channel")
        ],
    ]
)