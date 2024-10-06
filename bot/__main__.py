import asyncio
import logging

from bot.app import (
    bot,
    dp,
)

logger = logging.getLogger(__name__)

# Запуск процесса поллинга новых апдейтов
async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Bot started")
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
