from aiogram import (
    Bot,
    Dispatcher,
)

from bot.handlers.routers import welcome_router
from bot.settings import settings

bot = Bot(token=settings.tg.token)
dp = Dispatcher()
dp.include_router(welcome_router)
