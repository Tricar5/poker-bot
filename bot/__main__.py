import asyncio

from bot.app import (
    bot,
    dp,
)


# Запуск процесса поллинга новых апдейтов
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
