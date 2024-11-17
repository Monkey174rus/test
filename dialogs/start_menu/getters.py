from typing import TYPE_CHECKING

from aiogram import html
from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner
from database import Database


if TYPE_CHECKING:
    from locales.stub import TranslatorRunner # type: ignore


async def get_hello(
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        db: Database,
        event_from_user: User,
        **kwargs,
        ) -> dict[str, str]:

        if await db.get_user(id=event_from_user.id) is not None:
                status=True
        else: status=False
        
        username = html.quote(event_from_user.full_name)
        return {"hello_user": i18n.hello.user(username=username),
                "button_start": i18n.button.start(),
                "button_register": i18n.button.register(),
                "button_control": i18n.button.control(),
                "button_status_reg" : status,
                "button_status" : not status
                
            }


async def account (
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        db: Database,
        event_from_user: User,
        **kwargs,
        ) -> dict[str, str]:
       
       return {"account_text": i18n.account.text(),
               "button_delete": i18n.button.delete()    
       }

async def question (
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        db: Database,
        event_from_user: User,
        **kwargs,
        ) -> dict[str, str]:
       
       return {"question_text": i18n.question.text(),
               "button_yes": i18n.button.yes(), 
               "button_no": i18n.button.no()   
       }

async def recommendation (
        dialog_manager: DialogManager,
        i18n: TranslatorRunner,
        db: Database,
        event_from_user: User,
        **kwargs,
        ) -> dict[str, str]:
       status=False
       if await db.get_user(id=event_from_user.id) is not None:
                text=i18n.recommendation_yes.text()
                status=True
       else: text=i18n.recommendation_no.text()


       return {"recommendation_text": text,
               "button_yes": i18n.button.yes(), 
               "button_no": i18n.button.no(),
               "button_register": i18n.button.register(),
               "button_status_reg" : status,
               "button_status" : not status,
               "button_prod" : i18n.button.prod(),

       }




