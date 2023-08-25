from aiogram import types
from loader import dp
from random import choice
from data.list_answer_bot import TEXT_ANSWER, ANIMATION_ANSWER, STICKER_ANSWER
from handlers.users.commands.start import check_sub_channel, keyboard_check_channel, bot_action
from database.base import add_last_message


@dp.message_handler(content_types=types.ContentType.TEXT)
async def all_message(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer(choice(TEXT_ANSWER))
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.ANIMATION)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.reply_animation(choice(ANIMATION_ANSWER))
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.VOICE)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("Брррррр, не люблю звук пенопласта")
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.reply_photo(message.photo[0].file_id)
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("Это песня?")
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.DICE)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("Ставлю на ....")
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("+123456789")
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("Забавный файлик...")
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.reply_location(0, 0)
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("Не могу понять, что тут снимали...")
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.STICKER)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.reply_sticker(choice(STICKER_ANSWER))
        else:
            await keyboard_check_channel(message)


@dp.message_handler(content_types=types.ContentType.POLL)
async def all_animation(message: types.Message):
    if message.chat.type == "private":
        await bot_action(message)
        add_last_message(message.chat.id)
        if await check_sub_channel(message.from_user.id):
            await message.answer("Наверное первый вариант...")
        else:
            await keyboard_check_channel(message)