from aiogram import Router
from aiogram.types import ErrorEvent
from aiogram.exceptions import TelegramNotFound
from aiogram.fsm.context import FSMContext
import logging
from geopy.exc import GeocoderQueryError
from states.geolocate_state import GeolocateSearch


router = Router()


@router.error(GeolocateSearch.Q1)
async def error_with_geolocate_state(event: ErrorEvent, state: FSMContext):
    await event.update.message.answer("🚫 Не получилось найти такой объект или адрес")
    await state.clear()


@router.error()
async def error_handler(event: ErrorEvent):
    if isinstance(event.exception, TelegramNotFound):
        logging.warning(msg=event.exception)
    elif isinstance(event.exception, GeocoderQueryError):
        await event.update.message.answer("🚫 Не получилось найти такой объект или адрес")
    else:
        logging.error(msg=event.exception, exc_info=True)