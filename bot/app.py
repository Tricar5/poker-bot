from aiogram.filters.command import Command
from aiogram import (
    Bot,
    Dispatcher,
    types,
)
from bot.settings import settings

bot = Bot(token=settings.tg.token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
