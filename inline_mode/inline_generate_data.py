from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InputLocationMessageContent
from inline_mode.data_inline_mode import GENERATE_DATA, fake_genarate_data
import uuid
from rapidfuzz import process, fuzz, utils


router = Router()


@router.inline_query()
async def inline_mode_handler(inline_query: InlineQuery):
    if inline_query.query != "":
        results = []
        correct_keys = process.extract(query=inline_query.query, choices=GENERATE_DATA.keys(), scorer=fuzz.QRatio, limit=25, processor=utils.default_process)
        for arr in correct_keys:
            key = arr[0]
            data = GENERATE_DATA[key]
            input_message_content = InputTextMessageContent(message_text=f"<b>{key}:</b>\n<code>{str(fake_genarate_data(key))}</code>")
            if key in ["Случайная точка России", "Случайная точка в мире"]:
                coord = fake_genarate_data(key)
                input_message_content = InputLocationMessageContent(latitude=coord[0], longitude=coord[1])
            results.append(
                InlineQueryResultArticle(
                    id=str(uuid.uuid4()),
                    title=key,
                    description=data["description"],
                    input_message_content=input_message_content,
                    thumbnail_url=data["thumbnail_url"],
                    thumbnail_height=160,
                    thumbnail_width=160
                )
            )
    else:
        results = [
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="⬆️ Перейди в бота по кнопке выше",
                description='И отправь боту /help, чтобы узнай полный список доступных данных',
                input_message_content=InputTextMessageContent(message_text="🤖"),
                thumbnail_url="https://em-content.zobj.net/source/apple/354/robot_1f916.png",
                thumbnail_height=160,
                thumbnail_width=160
            ),
            InlineQueryResultArticle(
                id=str(uuid.uuid4()),
                title="⬇️ Пиши что хочешь сгенерировать",
                description='Например: "Время", "Криптовалюта", "Цвет", "Номер телефона" и т.д.',
                input_message_content=InputTextMessageContent(message_text="🧑‍💻"),
                thumbnail_url="https://em-content.zobj.net/source/apple/354/technologist_1f9d1-200d-1f4bb.png",
                thumbnail_height=160,
                thumbnail_width=160
            )
        ]


    await inline_query.answer(results, cache_time=1, is_personal=True, switch_pm_text="Перейти в бота", switch_pm_parameter="i")