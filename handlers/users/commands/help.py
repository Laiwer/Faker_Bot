from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import CommandHelp


@dp.message_handler(CommandHelp())
async def command_help(message: types.Message):
    msg = f"Привет <b>{message.from_user.full_name}</b>!"
    msg += "\nЯ 🥸 <b>𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</b>."
    msg += "\n\n🎞 Умею генерировать различные данные во вкладке <b><i>Сгенерировать</i></b> (фио, расположение, даты и т.д.)."
    msg += "\n🌎 Также с недавним обновлением я научился работать с местоположением. Скинь мне координаты или геопозицию во вкладке <b><i>Местоположение</i></b> и я покажу полностью адрес, почтовый индекс, страну и т.д."
    msg += "\n\n🔍 Следи за регулярными обновлениями в <a href='https://t.me/faker_bots_channel'>канале 𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝'а</a>"
    msg += "\n🆕 Отправляй /start и начинай пользоваться самым лучшим ботом!"
    await message.answer(msg)