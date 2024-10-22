from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON
from database import Database
from keyboards.start_inline_kb import create_start_keyboard


router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart())
async def process_start_command(message: Message, db: Database):

    if db.get_user(id=message.from_user.id)==message.from_user.id:
        await message.answer(LEXICON[message.text].replace('@', f' {message.from_user.full_name}'),
                                reply_markup=create_start_keyboard(
                                'login',
                                'registration'
                                )
                            )
    else : 
        await message.answer(LEXICON[message.text].replace(', @', f' {''}'),
                                reply_markup=create_start_keyboard(
                                'login',
                                'registration'
                                )
                            )
    
    #await db.add_user(
        #id=message.from_user.id,
        #username=message.from_user.username

    #)
@router.callback_query(F.data == 'registration')
async def process_registration_press(callback: CallbackQuery, db: Database):
        await db.add_user(
            id=callback.from_user.id,
            username=callback.from_user.username

        )
        await callback.answer()

