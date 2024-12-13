from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from typing import Dict, Any, Callable, Awaitable


class MediaMiddlewareCountClick(BaseMiddleware):
    def __init__(self) -> None:
        self.count_click = 0

    async def __call__(
            self,
            handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any]) -> Any:
        if event.data == "repead":
            self.count_click += 1
        if self.count_click > 2:
            self.count_click = 0
        data["count_click"] = self.count_click
        return await handler(event, data)