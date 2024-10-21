from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON
from database import Database

from aiogram.utils.formatting import Text, Bold

router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message, db: Database):
    await message.answer(LEXICON[message.text].replace('@', f' {message.from_user.full_name}'))
    await db.add_user(
        id=message.from_user.id,
        username=message.from_user.username

    )

