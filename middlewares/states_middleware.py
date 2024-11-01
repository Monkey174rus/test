from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.fsm.context import FSMContext





class StatesMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
        event: TelegramObject,
        data: Dict[str, Any] 
    ) -> Any:
        
        state: FSMContext = data.get('state')
        current_state = await state.get_state()

        data['state_us'] = current_state
        
        result = await handler(event, data)
        return result


    





    