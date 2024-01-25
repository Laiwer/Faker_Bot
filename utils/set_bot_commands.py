from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats
from aiogram import Bot


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand(
                command="start",
                description="🔄 Запустить/Перезапустить бота"
            ),
            BotCommand(
                command="help",
                description="📖 Подробная информация о боте"
            ),
            BotCommand(
                command="generate",
                description="🎞 Сгенерировать данные"
            ),
            BotCommand(
                command="geolocation",
                description="🌎 Конвертер местоположения"
            ),
            BotCommand(
                command="statistics",
                description="📊 Статистика бота"
            ),
            BotCommand(
                command="subscribe",
                description="📢 Канал с обновлениями бота"
            )
        ],
        scope=BotCommandScopeAllPrivateChats()
    )
