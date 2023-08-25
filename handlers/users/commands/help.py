from aiogram import types
from loader import dp, bot
from database.base import add_last_message
from keyboards.inline.commands.help_kb import instruction_help_category_keyboard, all_generate_menu_category_keyboard
from aiogram.dispatcher.filters import CommandHelp
from aiogram.utils.exceptions import MessageNotModified
from handlers.users.commands.start import bot_action


msg = "\nЯ 🥸 <b>𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</b>."
msg += "\n\n🎞 Умею генерировать различные данные во вкладке <b><i>Сгенерировать</i></b> (фио, расположение, даты и т.д.). Со всеми данными можешь ознакомиться ниже по кнопке <b><i>\"Весь 🎞 Сгенирировать\"</i></b>. В боте более <b>80 <i>разных данных</i></b>."
msg += "\n🌎 Также с недавним обновлением я научился работать с местоположением. Скинь мне координаты или геопозицию во вкладке <b><i>Местоположение</i></b> и я покажу полностью адрес, почтовый индекс, страну и т.д."
msg += "\n📊 Вы можете увидеть статистику бота, в которой представлено: <b><i>Всего пользователей</i></b>, <b><i>Пользователи за час</i></b>, <b><i>Пользователи за 24 часа</i></b> и <b><i>Использование бота</i></b>."
msg += "\n\n🔍 Следи за регулярными обновлениями в <a href='https://t.me/faker_bots_channel'>канале 𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝'а</a>"
msg += "\n🆕 Отправляй /start и начинай пользоваться самым оригинальным и полезным ботом!"


@dp.message_handler(CommandHelp())
async def command_help(message: types.Message):
    await bot_action(message)
    add_last_message(message.chat.id)
    text = f"Привет <b>{message.chat.full_name}</b>!" + msg
    await message.answer(text, reply_markup=all_generate_menu_category_keyboard, disable_web_page_preview=True)


@dp.callback_query_handler(text="instruction_help")
async def command_help(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    text = f"Привет <b>{call.message.chat.full_name}</b>!" + msg
    await call.message.edit_text(text, reply_markup=all_generate_menu_category_keyboard, disable_web_page_preview=True)


@dp.callback_query_handler(text="all_generate_menu")
async def command_help(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    msg = "🎞 Сгенерировать"
    msg += "\n\t\t\t\t👤 Личность"
    msg += "\n\t\t\t\t\t\t\t\t🪪 ФИО"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🚹 Мужское"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🪪 Мужское Ф.И.О.</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📇 Мужское имя</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👨‍👩‍👧‍👦 Мужская фамилия</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👱‍♂️ Мужское отчество</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🚺 Женское"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🪪 Женское Ф.И.О.</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📇 Женское имя</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👨‍👩‍👧‍👦 Женская фамилия</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👱‍♂️ Женское отчество</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t👅 Язык"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👅 Язык</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>⌨️ Код языка</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t🧑 Человек"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👱‍♂️ Профиль</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👶 Упрощённый профиль</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t☎️ Номер телефона"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🚩 Код страны</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📺 MSISDN</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📞 Номер телефона</i></b>"
    msg += "\n\t\t\t\t💰 Экономика"
    msg += "\n\t\t\t\t\t\t\t\t💳 Банковская карта"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💳 Банковская карта</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💰 Платёжная система</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🏦 Банк</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🔢 Номер карты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🗓 Дата карты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🤫 Код безопасности</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t🏢 Компания"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📰 Название маленькой компании</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🏢 Название крупной компании</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💸 Слоган компании</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🧰 Деятельность компании</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🎫 ИНН</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📜 ОГРН</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t💵 Валюты"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t💶 Денежная валюта"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💵 Валюта</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🪙 Название валюты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📟 Код валюты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💠 Символ валюты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📶 Кол-во денег</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t📀 Криптовалюта"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💿 Криптовалюта</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>⚙️ Название криптовалюты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📟 Код криптовалюты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t🛠 Профессия"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🛠 Профессия</i></b>"
    msg += "\n\t\t\t\t🪄 Развлечения"
    msg += "\n\t\t\t\t\t\t\t\t🎭 Эмодзи"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🎭 Эмодзи</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t🎨 Цвет"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🌈 Название цвета</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👾 Цвет палитры HEX</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🔹 Цвет палитры RGB</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🔶 Цвет палитры CSS RGB</i></b>"
    try:
        await call.message.edit_text(msg, reply_markup=instruction_help_category_keyboard)
    except MessageNotModified: pass



@dp.callback_query_handler(text="all_generate_menu_2")
async def command_help(call: types.CallbackQuery):
    await call.answer()
    add_last_message(call.message.chat.id)
    msg = "🎞 Сгенерировать"
    msg += "\n\t\t\t\t⛓ Разное"
    msg += "\n\t\t\t\t\t\t\t\t🗺 Расположение"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🏡 Адреса"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🪧 Адрес</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🏠 Номер дома</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🏘 Адрес улицы</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🛤 Название улицы</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🏙 Город</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🇷🇺 Субъекты РФ</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📬 Почтовый индекс</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🏞 Координаты"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>↔️ Долгота</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>↕️ Широта</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🎛 Случайные координаты</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🇺🇳 Страна</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t📍 Геометка"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🇷🇺 Случайная точка России</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🌎 Случайная точка в мире</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t📅 Дата и время"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t📅 Промежуток времени"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>☀️ День месяца</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📰 День недели</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🗓 Номер месяца</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📅 Название месяца</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🌏 Год</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>⚱️ Век</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🗓 Даты"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>👶 Дата рождения</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🗒 Случайная дата</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📅 Дата в этом месяце</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🌍 Дата в этом году</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>💫 Дата в этом десятилетии</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🏺 Дата в этом веке</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🔮 Будущая дата</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t⏰ Время"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🕓 Время</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>✈️ Часовые зоны</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t🚗 Транспорт"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🚏 Номерной знак</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🚕 ВИН-номер</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t📖 Текст"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🅰️ Буквы"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🅱️ Случайная буква</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🔡 Строчная буква</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🔠 Заглавная буква</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🆎 Случайные буквы</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t🆗 Слова"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🆕 Случайное слово</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>🆓 Случайные слова</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t📋 Предложения"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📝 Параграф</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📄 Предложение</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📑 Предложения</i></b>"
    msg += "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<b><i>📖 Текст</i></b>"
    try:
        await call.message.edit_text(msg, reply_markup=instruction_help_category_keyboard)
    except MessageNotModified: pass