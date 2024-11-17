from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format,Const
from aiogram_dialog.widgets.kbd import Button,Row, Start, Cancel, RequestLocation
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram.enums import ContentType
from aiogram_dialog.widgets.input import MessageInput

from dialogs.request_openai.getters import get_request 
from dialogs.request_openai.handlers import button_click, message_handler
from states.request_openai import RequestSG

request_dialog = Dialog(
    Window(
            Format('{request_locate}'),
            MessageInput(func=message_handler,
                        content_types=ContentType.ANY,
            ),
            Row(
                RequestLocation(Const(" Send location")),
            ),
            markup_factory=ReplyKeyboardFactory(resize_keyboard=True),

            getter=get_request,
            state=RequestSG.locate,
        )
)