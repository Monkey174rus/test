from aiogram.fsm.state import State, StatesGroup


class RequestSG(StatesGroup):
    locate = State()
    