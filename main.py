import asyncio

from aiogram import Bot, Dispatcher, Router

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
#from handlers.user_exit.exit_handler import exit_router
#from handlers.user_login.login_handler import login_router
from config.config import Config, load_config
from middlewares.db import DatabaseMiddleware
from middlewares.i18n import TranslatorRunnerMiddleware
#from middlewares.states_middleware import StatesMiddleware
from middlewares.dell_middleware import DellMiddleware
#from states.states import FSMFauthoriz

from database.base import create_table
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio.client import Redis

from fluentogram import TranslatorHub
from middlewares.i18n import TranslatorRunnerMiddleware
from utils.i18n import create_translator_hub

from aiogram_dialog import setup_dialogs
from handlers.commands import commands_router
from dialogs.start_menu.dialogs import start_dialog
from dialogs.request_openai.dialogs import request_dialog



dell={}




async def main():
    config: Config = load_config()
    engine = create_async_engine(url=config.db.url, echo=True)
    session = async_sessionmaker(engine, expire_on_commit=False)

    storage = RedisStorage(Redis.from_url(config.redis.url),key_builder=DefaultKeyBuilder(with_destiny=True))

    await create_table(engine)

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)

    translator_hub: TranslatorHub = create_translator_hub()
   # dp.update.middleware(StatesMiddleware())
    #передача FSM в диспетчер 
    #dp.workflow_data.update({'st': FSMFauthoriz})

    #dp.include_router(login_router)
    #dp.include_router(exit_router)




    dp.update.middleware(DellMiddleware())
    dp.update.middleware(TranslatorRunnerMiddleware())
    dp.update.middleware(DatabaseMiddleware(session=session))

    #aiogram-dialog
    
    dp.include_router(commands_router)
    dp.include_router(start_dialog)
    dp.include_router(request_dialog)
    setup_dialogs(dp)
    




    #aiogram-dialog
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, _translator_hub=translator_hub, _dell=dell)

if __name__ == '__main__':
    asyncio.run(main())