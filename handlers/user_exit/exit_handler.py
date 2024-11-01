from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from database import Database
from keyboards.start_inline_kb import create_start_keyboard


from aiogram.fsm.context import FSMContext


exit_router = Router()



@exit_router.message(CommandStart())
async def process_start_command_login(message: Message, i18n, db: Database):
    if await db.get_user(id=message.from_user.id) is not None:
        await message.answer(i18n.get(message.text).replace(', @', f' {'вxод не выполнен, регистрация есть'}'),
                                reply_markup=create_start_keyboard(i18n,
                                'login',
                                'delete'
                                )
                            )
    else :
          await message.answer(i18n.get(message.text).replace('@', f' {'вxод не выполнен, регистрации нет'}'),
                                reply_markup=create_start_keyboard(i18n,
                                'login',
                                'registration'
                                )
                            )


@exit_router.callback_query(F.data == 'login')
async def process_delete_press(callback: CallbackQuery, i18n, st, db: Database, state: FSMContext):
        if await db.get_user(id=callback.from_user.id) is not None:
        
            await callback.message.edit_text(text=i18n['/start'].replace('@', f' {'аккаунт есть, вxод выполнен'}'),
                reply_markup=create_start_keyboard(i18n,
                                    'exit',
                                    'delete'
                                    )
                                    )
            await state.update_data(login_completed=callback.data)
            await state.set_state(st.login_completed)
        else :
              await callback.message.edit_text(text=i18n['/start'].replace(', @', f' {'аккаунт не зарегистрирован'}'),
              reply_markup=create_start_keyboard(i18n,
                                
                                'registration'
                                )
                                )
              
        await callback.answer()


@exit_router.callback_query(F.data == 'registration')
async def process_registration_press(callback: CallbackQuery, st, i18n,  db: Database, state: FSMContext):
        await db.add_user(
            id=callback.from_user.id,
            username=callback.from_user.username

        )

        await state.update_data(login_completed=callback.data)
        await state.set_state(st.login_completed)

        await callback.answer()
        await callback.message.edit_text(text=i18n['/start'].replace('@', f' {'прошла регистрация вxод выполнен'}'),
              reply_markup=create_start_keyboard(i18n,
                                'exit',
                                'delete'
                                )
                                )
    

@exit_router.callback_query(F.data == 'delete')
async def process_delete_press(callback: CallbackQuery, i18n):
        await callback.answer()
        await callback.message.edit_text(text=i18n['question'],
              reply_markup=create_start_keyboard(i18n,
                                'yes',
                                'no'
                                )
                                )
        

@exit_router.callback_query(F.data == 'yes')
async def process_delete_press(callback: CallbackQuery,i18n, db: Database, state: FSMContext):
        await db.delete_user(
            id=callback.from_user.id
        )
        await state.update_data(login_completed=callback.data)
        await state.clear ()
        await callback.answer()
        await callback.message.edit_text(text=i18n['/start'].replace(', @', f' {'аккаунт удален, выxод выполнен'}'),
              reply_markup=create_start_keyboard(i18n,
                                'login',
                                'registration'
                                )
                                )


@exit_router.callback_query(F.data == 'no')
async def process_delete_press(callback: CallbackQuery,i18n):
        await callback.answer()
        await callback.message.edit_text(text=i18n['/start'].replace('@', f' {'аккаунт не удален, выxод не выполнен'}'),
              reply_markup=create_start_keyboard(i18n,
                                'exit',
                                'delete'
                                )
                                )
        
        

              
        