from typing import TYPE_CHECKING

from aiogram import html
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from database import Database

if TYPE_CHECKING:
    from locales.stub import TranslatorRunner # type: ignore


async def get_request(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        db: Database,
        event_from_user: User,
        **kwargs,
        ) -> dict[str, str]:

        
        username = html.quote(event_from_user.full_name)
        
        return {"hello_user": i18n.hello.user(username=username),
                "request_locate": i18n.request.locate(),
                "button_register": i18n.button.register(),
                "button_control": i18n.button.control(),
                
            }