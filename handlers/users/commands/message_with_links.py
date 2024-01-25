from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command


router = Router()


@router.message(Command("subscribe"))
async def channel_with_updates_command(message: Message):
    await message.answer("<a href='https://t.me/faker_bots_channel'>Канал 𝙵𝚊𝚔𝚎𝚛 𝙱𝚘𝚝</a>\n⬆️⬆️⬆️ Переходи и подписывайся на канал, чтобы быть в курсе новый обновлений")