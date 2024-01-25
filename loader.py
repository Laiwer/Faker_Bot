import certifi
import geopy.geocoders
import ssl
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from data.data_config import BOT_TOKEN
from faker import Faker
from geopy.geocoders import Nominatim
from handlers.users.commands import geolocation, message_with_links, start, admin, help, statistics, generate
from handlers.users.generate import generate_keyboard, different, economy, fun, personality, technology
from handlers.users.geolocation import geolocate
from handlers.users.statistics import statistic
from handlers.users.channel_with_update import message_with_link
from handlers.users import nothing
from handlers.errors import error
from inline_mode import inline_generate_data
from middlewares.check_subscribe import CheckingSubscribeOnChannel, CheckingSubscribeOnChannelInlineMode
from middlewares.throttling import ThrottlingMessageMiddleware
from middlewares.add_last_message import AddLastMessageMiddleware
from middlewares.send_start import SendStartMessageMiddleware, SendStartCallbackQueryMiddleware
from middlewares.in_update_add import InUpdateAddDataMiddleware
from utils.notify_admins import on_startup_notify, on_shutdown_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(bot: Bot):
    await on_startup_notify(bot)


async def on_shutdown(bot: Bot):
    await on_shutdown_notify(bot)


async def start_bot():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    fake = Faker("ru_RU")

    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    geolocator = Nominatim(user_agent="Telegram Bot")
    
    await set_default_commands(bot)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.inline_query.middleware.register(CheckingSubscribeOnChannelInlineMode())
    dp.message.middleware.register(SendStartMessageMiddleware())
    dp.callback_query.middleware.register(SendStartCallbackQueryMiddleware())
    dp.message.middleware.register(ThrottlingMessageMiddleware())
    dp.message.middleware.register(AddLastMessageMiddleware())
    dp.message.middleware.register(CheckingSubscribeOnChannel())
    dp.message.middleware.register(InUpdateAddDataMiddleware(fake=fake, geolocator=geolocator))
    dp.callback_query.middleware.register(InUpdateAddDataMiddleware(fake=fake, geolocator=geolocator))

    dp.include_router(error.router)
    dp.include_router(inline_generate_data.router)
    dp.include_routers(
        start.router,
        admin.router,
        help.router,
        statistics.router,
        generate.router,
        geolocation.router,
        message_with_links.router
    )
    dp.include_routers(
        generate_keyboard.router,
        different.date_time.router,
        different.locate.router,
        different.text.router,
        different.transport.router,
        economy.bank_card.router,
        economy.company.router,
        economy.currency.router,
        economy.job.router,
        fun.color.router,
        fun.emoji.router,
        personality.fio.router,
        personality.language.router,
        personality.number_phone.router,
        personality.person.router,
        technology.email.router,
        technology.file.router,
        technology.internet.router,
        technology.token_system.router,
    )
    dp.include_router(geolocate.router)
    dp.include_router(statistic.router)
    dp.include_router(message_with_link.router)
    dp.include_router(nothing.router)
    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        await bot.session.close()