from aiogram import BaseMiddleware
from typing import Callable, Awaitable, Dict, Any
from aiogram.types import Message
from faker import Faker
from geopy.geocoders import Nominatim


class InUpdateAddDataMiddleware(BaseMiddleware):
    def __init__(self, fake: Faker, geolocator: Nominatim) -> None:
        super().__init__()
        self.fake = fake
        self.geolocator = geolocator
    
    async def __call__(
            self,
            handler: Callable[[Message, Dict[int, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        data["fake"] = self.fake
        data["geolocator"] = self.geolocator
        return await handler(event, data)