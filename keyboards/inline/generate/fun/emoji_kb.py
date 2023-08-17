from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


emoji_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🎭 Эмодзи", callback_data="emoji_emoji")
        ]
    ]
)