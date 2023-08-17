from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "🔄 Запустить/Перезапустить бота"),
            types.BotCommand("help", "📖 Подробная информация о боте"),
            types.BotCommand("generate", "🎞 Сгенерировать данные"),
            types.BotCommand("geolocation", "🌎 Конвертер местоположения"),
            types.BotCommand("statistics", "📊 Статистика бота"),
        ]
    )
