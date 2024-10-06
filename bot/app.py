from aiogram import (
    Bot,
    Dispatcher,
    types,
)
from aiogram.filters.command import Command

from bot.settings import settings

bot = Bot(token=settings.tg.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message) -> None:
    await message.answer("Hello!")
