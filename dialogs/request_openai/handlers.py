from typing import TYPE_CHECKING

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from database import Database
from states.request_openai import RequestSG
from aiogram_dialog.widgets.input import MessageInput


if TYPE_CHECKING:
    from locales.stub import TranslatorRunner # type: ignore


async def button_click(
    callback: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager
) -> None:
    i18n: TranslatorRunner = dialog_manager.middleware_data.get('i18n')
    await callback.answer(text=i18n.button.pressed())

async def message_handler(
        message: Message,
        widget: MessageInput,
        dialog_manager: DialogManager) -> None:
        await message.send_copy(message.chat.id)




