from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text == "📢 Канал с обновлениями")
async def channel_with_updates(message: Message):
    await message.answer("<a href='https://t.me/faker_bots_channel'>Канал 𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</a>\n⬆️⬆️⬆️ Переходи и подписывайся на канал, чтобы быть в курсе новых обновлений")