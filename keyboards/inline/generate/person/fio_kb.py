from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_to_fio_category_button = InlineKeyboardButton("⏪ Назад", callback_data="back_to_fio_category")

fio_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🚹 Мужское", callback_data="fio_male")
        ],
        [
            InlineKeyboardButton("🚺 Женское", callback_data="fio_female")
        ]
    ]
)

fio_male_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🪪 Мужское Ф.И.О.", callback_data="fio:male:fio_person")
        ],
        [
            InlineKeyboardButton("📇 Мужское имя", callback_data="fio:male:first_name")
        ],
        [
            InlineKeyboardButton("👨‍👩‍👧‍👦 Мужская фамилия", callback_data="fio:male:middle_name")
        ],
        [
            InlineKeyboardButton("👱‍♂️ Мужское отчество", callback_data="fio:male:last_name")
        ],
        [
            back_to_fio_category_button
        ],
    ]
)

fio_female_category_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("🪪 Женское Ф.И.О.", callback_data="fio:female:fio_person")
        ],
        [
            InlineKeyboardButton("📇 Женское имя", callback_data="fio:female:first_name")
        ],
        [
            InlineKeyboardButton("👨‍👩‍👧‍👦 Женская фамилия", callback_data="fio:female:middle_name")
        ],
        [
            InlineKeyboardButton("👱‍♂️ Женское отчество", callback_data="fio:female:last_name")
        ],
        [
            back_to_fio_category_button
        ],
    ]
)