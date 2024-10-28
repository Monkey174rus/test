import asyncio

from aiogram import Bot, Dispatcher

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers import user_handlers
from config.config import Config, load_config
from middlewares.db import DatabaseMiddleware
from database.base import create_table
from aiogram.fsm.storage.redis import RedisStorage


async def main():
    config: Config = load_config()
    engine = create_async_engine(url=config.db.url, echo=True)
    session = async_sessionmaker(engine, expire_on_commit=False)

    storage = RedisStorage.from_url(config.redis.url)

    await create_table(engine)

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)
    dp.include_router(user_handlers.router)
    dp.update.middleware(DatabaseMiddleware(session=session))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())