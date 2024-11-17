from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format,Const
from aiogram_dialog.widgets.kbd import Button,Row, Start, Cancel,SwitchTo 

from dialogs.start_menu.getters import get_hello, account, question, recommendation
from dialogs.start_menu.handlers import button_click, button_register, button_yes, dialog_locate
from states.start import StartSG
from states.request_openai import RequestSG

start_dialog = Dialog(
    Window(
            Format('{hello_user}'),
            Row(
                Start(Format('{button_start}'),
                    id='button_start',
                    state=StartSG.recommendation),
                Button(Format('{button_register}'),
                    id='button_register',
                    on_click=button_register,
                    when='button_status'
                    ),
                Start(Format('{button_control}'),
                    id='button_control',
                    when='button_status_reg',
                    state=StartSG.account),
                    
            ),

            getter=get_hello,
            state=StartSG.start,
        ),

    Window(
            Format('{account_text}'),
            Row(
                Cancel(Const('◀️'),
                    id='button_exit',
                    ),
                Start(Format('{button_delete}'),
                    id='button_delete',
                    state=StartSG.question

                    ),
                    
            ),

            getter=account,
            state=StartSG.account,
        ),

    Window(
            Format('{question_text}'),
            Row(
                Start(Format('{button_yes}'),
                    id='button_yes',
                    on_click=button_yes,
                    state=StartSG.start
                    ),
                Cancel(Format('{button_no}'),
                    id='button_no'
                    ),
                    
            ),

            getter=question,
            state=StartSG.question,
        ),
    Window(
            Format('{recommendation_text}'),
            Row(
                Start(Format('{button_yes}'),
                    id='button_yes',
                    on_click=button_click,
                    state=StartSG.start
                    ),
                Cancel(Format('{button_no}'),
                    id='button_no',
                    on_click=button_click
                    ),
                when='button_status_reg',          
            ),
            Row(
                SwitchTo(Format('{button_prod}'),
                    id='button_prod',
                    on_click=dialog_locate,
                    state=RequestSG.locate
                    ),
                Button(Format('{button_register}'),
                    id='button_register',
                    on_click=button_register),
                when='button_status',
                

            ),

            getter=recommendation,
            state=StartSG.recommendation,
        ),
)