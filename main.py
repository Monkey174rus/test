import asyncio

from aiogram import Bot, Dispatcher

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.user_exit.exit_handler import exit_router
from handlers.user_login.login_handler import login_router
from config.config import Config, load_config
from middlewares.db import DatabaseMiddleware

from middlewares.i18n import TranslatorMiddleware
from middlewares.states_middleware import StatesMiddleware
from states.states import FSMFauthoriz

from database.base import create_table
from aiogram.fsm.storage.redis import RedisStorage

from lexicon.lexicon_en import LEXICON_EN
from lexicon.lexicon_ru import LEXICON_RU

translations = {
        'default': 'ru',
            'en': LEXICON_EN,
                'ru': LEXICON_RU,
                }

async def main():
    config: Config = load_config()
    engine = create_async_engine(url=config.db.url, echo=True)
    session = async_sessionmaker(engine, expire_on_commit=False)

    storage = RedisStorage.from_url(config.redis.url)

    await create_table(engine)

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)
    
    dp.update.middleware(StatesMiddleware())
    #передача FSM в диспетчер 
    dp.workflow_data.update({'st': FSMFauthoriz})

    dp.include_router(login_router)
    dp.include_router(exit_router)

    

    dp.update.middleware(TranslatorMiddleware())
    dp.update.middleware(DatabaseMiddleware(session=session))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translations=translations)

if __name__ == '__main__':
    asyncio.run(main())