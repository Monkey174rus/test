from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from filters.filters import User_Login
from keyboards.start_inline_kb import create_start_keyboard
from database import Database



login_router = Router()
login_router.message.filter(User_Login())
login_router.callback_query.filter(User_Login())



@login_router.message(Command(commands='help'))
async def process_login_command(message: Message, st, i18n, state: FSMContext):
    await message.answer(i18n.get(message.text))
    

    await state.set_state(st.login_completed)


@login_router.message(Command(commands='state'))
async def process_login_command(message: Message,  state: FSMContext):
    current_state = await state.get_state()
    
    
    if current_state is None:
            await message.answer("no")
    
    else:
         await message.answer("yes")
         await state.clear ()
    

@login_router.message(CommandStart())
async def press_start_command(message: Message, i18n, db: Database):
    if await db.get_user(id=message.from_user.id) is not None:
        
        await message.answer(i18n.get(message.text).replace('@', f' {'вxод выполнен, регистрация есть'}'),
                                reply_markup=create_start_keyboard(i18n,
                                'exit',
                                'delete'
                                )
                            )
    else :
          await message.answer(i18n.get(message.text).replace('@', f' {'вxод выполнен, регистрации нет'}'),
                                reply_markup=create_start_keyboard(i18n,
                                'exit',
                                'registration'
                                )
                            )
        

@login_router.callback_query(F.data == 'exit')
async def process_delete_press(callback: CallbackQuery,i18n, state: FSMContext):
        
        await state.clear ()
        await callback.answer()
        await callback.message.edit_text(text=i18n['/start'].replace(', @', f' {'аккаунт не удален, выxод выполнен'}'),
              reply_markup=create_start_keyboard(i18n,
                                'login',
                                'delete'
                                )
                                )

@login_router.callback_query(F.data == 'delete')
async def process_delete_press(callback: CallbackQuery, i18n):
        await callback.answer()
        await callback.message.edit_text(text=i18n['question'],
              reply_markup=create_start_keyboard(i18n,
                                'yes',
                                'no'
                                )
                                )
        

@login_router.callback_query(F.data == 'yes')
async def process_delete_press(callback: CallbackQuery,i18n, db: Database, state: FSMContext):
        await db.delete_user(
            id=callback.from_user.id
        )
        await state.clear ()
        await callback.answer()
        await callback.message.edit_text(text=i18n['/start'].replace(', @', f' {'аккаунт удален, выxод выполнен'}'),
              reply_markup=create_start_keyboard(i18n,
                                'login',
                                'registration'
                                )
                                )


@login_router.callback_query(F.data == 'no')
async def process_delete_press(callback: CallbackQuery, i18n):
        await callback.answer()
        await callback.message.edit_text(text=i18n['/start'].replace('@', f' {'аккаунт не удален, выxод не выполнен'}'),
              reply_markup=create_start_keyboard(i18n,
                                'exit',
                                'delete'
                                )
                                )

   

