
from aiogram.fsm.state import State, StatesGroup


class StartSG(StatesGroup):
    start = State()
    account = State ()
    question = State()
    recommendation = State ()