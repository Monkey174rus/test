from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from lexicon.lexicon import LEXICON
from database import Database
from keyboards.start_inline_kb import create_start_keyboard

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis

class FSMFillForm(StatesGroup):
      
      login_completed = State()
      
      


router = Router()


# Этот хэндлер будет срабатывать на команду "/start" -
# добавлять пользователя в базу данных, если его там еще не было
# и отправлять ему приветственное сообщение
@router.message(CommandStart(), StateFilter(FSMFillForm.login_completed))
async def process_start_command(message: Message, db: Database):
    if await db.get_user(id=message.from_user.id) is not None:
        await message.answer(LEXICON[message.text].replace('@', f' {'вxод выполнен'}'),
                                reply_markup=create_start_keyboard(
                                'exit',
                                'delete'
                                )
                            )
        
@router.message(CommandStart())
async def process_start_command_login(message: Message, db: Database):
    if await db.get_user(id=message.from_user.id) is None:
        await message.answer(LEXICON[message.text].replace(', @', f' {'вxод не выполнен'}'),
                                reply_markup=create_start_keyboard(
                                'login',
                                'registration'
                                )
                            )
    

@router.callback_query(F.data == 'registration')
async def process_registration_press(callback: CallbackQuery, db: Database, state: FSMContext):
        await db.add_user(
            id=callback.from_user.id,
            username=callback.from_user.username

        )

        await state.update_data(login_completed=callback.data)
        await state.set_state(FSMFillForm.login_completed)

        await callback.answer()
        await callback.message.edit_text(text=LEXICON['/start'].replace('@', f' {'прошла регистрация вxод выполнен'}'),
              reply_markup=create_start_keyboard(
                                'exit',
                                'delete'
                                )
                                )
    

@router.callback_query(F.data == 'delete', StateFilter(FSMFillForm.login_completed))
async def process_delete_press(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(text=LEXICON['question'],
              reply_markup=create_start_keyboard(
                                'yes',
                                'no'
                                )
                                )

@router.callback_query(F.data == 'delete')
async def process_delete_press(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(text=LEXICON['question'],
              reply_markup=create_start_keyboard(
                                'yes',
                                'no'
                                )
                                )
        

@router.callback_query(F.data == 'yes', StateFilter(FSMFillForm.login_completed))
async def process_delete_press(callback: CallbackQuery, db: Database, state: FSMContext):
        await db.delete_user(
            id=callback.from_user.id
        )
        await state.update_data(login_completed=callback.data)
        await state.clear ()
        await callback.answer()
        await callback.message.edit_text(text=LEXICON['/start'].replace(', @', f' {'аккаунт удален, выxод выполнен'}'),
              reply_markup=create_start_keyboard(
                                'login',
                                'registration'
                                )
                                )


@router.callback_query(F.data == 'no', StateFilter(FSMFillForm.login_completed))
async def process_delete_press(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(text=LEXICON['/start'].replace('@', f' {'аккаунт не удален, выxод не выполнен'}'),
              reply_markup=create_start_keyboard(
                                'exit',
                                'delete'
                                )
                                )


        
@router.callback_query(F.data == 'exit', StateFilter(FSMFillForm.login_completed))
async def process_delete_press(callback: CallbackQuery, state: FSMContext):
        
        await state.update_data(login_completed=callback.data)
        await state.clear ()
        await callback.answer()
        await callback.message.edit_text(text=LEXICON['/start'].replace(', @', f' {'аккаунт не удален, выxод выполнен'}'),
              reply_markup=create_start_keyboard(
                                'login',
                                'registration'
                                )
                                )
        
@router.callback_query(F.data == 'login')
async def process_delete_press(callback: CallbackQuery, db: Database, state: FSMContext):
        if await db.get_user(id=callback.from_user.id) is not None:
        
            await callback.message.edit_text(text=LEXICON['/start'].replace('@', f' {'аккаунт есть, вxод выполнен'}'),
                reply_markup=create_start_keyboard(
                                    'exit',
                                    'delete'
                                    )
                                    )
            await state.update_data(login_completed=callback.data)
            await state.set_state(FSMFillForm.login_completed)
        else :
              await callback.message.edit_text(text=LEXICON['/start'].replace(', @', f' {'аккаунт не зарегистрирован'}'),
              reply_markup=create_start_keyboard(
                                
                                'registration'
                                )
                                )
              
        await callback.answer()
              
        