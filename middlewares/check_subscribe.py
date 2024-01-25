from aiogram import BaseMiddleware
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from keyboards.inline.subscribe_channel_kb import check_subscribe_keyboard
from typing import Callable, Dict, Any, Awaitable
import uuid


class CheckingSubscribeOnChannel(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await data["bot"].get_chat_member(chat_id="@bots_rooms", user_id=event.chat.id)
        if chat_member.status != "left":
            return await handler(event, data)
        else:
            await event.answer("⬇ Для продолжения подпишись на <b><i>🤖 Bots Room</i></b>, чтобы первым пробовать новых ботов.", reply_markup=check_subscribe_keyboard)


class CheckingSubscribeOnChannelInlineMode(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[InlineQuery, Dict[str, Any]], Awaitable[Any]],
        event: InlineQuery,
        data: Dict[str, Any]
    ) -> Any:
        chat_member = await data["bot"].get_chat_member(chat_id="@bots_rooms", user_id=event.from_user.id)
        if chat_member.status != "left":
            return await handler(event, data)
        else:
            result = [
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title="⬆️ Перейди в бота по кнопке выше",
                    description='Отправь боту /start и подпишись на канал, чтобы пользоваться ботом',
                    input_message_content=InputTextMessageContent(message_text="📢"),
                    thumbnail_url="https://em-content.zobj.net/source/apple/354/loudspeaker_1f4e2.png",
                    thumbnail_height=160,
                    thumbnail_width=160
            )
            ]
            await event.answer(result, cache_time=1, is_personal=True, switch_pm_text="Перейти в бота", switch_pm_parameter="i")