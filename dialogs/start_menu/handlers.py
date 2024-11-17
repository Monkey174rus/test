from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from database import Database
from states.start import StartSG
from states.request_openai import RequestSG

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner # type: ignore


async def button_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await callback.answer(text=i18n.button.pressed())


async def button_register(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
) -> None:
    db: Database = dialog_manager.middleware_data.get('db')
    await db.add_user(
            id=callback.from_user.id,
            username=callback.from_user.username

        )
    

async def button_yes(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
) -> None:
    db: Database = dialog_manager.middleware_data.get('db')
    await db.delete_user(
            id=callback.from_user.id
        )
    

async def dialog_locate(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
) -> None:  
    await dialog_manager.start(state=RequestSG.locate)
    