from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from aiogram.types import  Update

from aiogram import Bot



class DellMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]], 
        event: TelegramObject,
        data: Dict[str, Any] 
    ) -> Any:
        up : Update= data.get('event_update')
        
        dell = data.get('_dell')
        data['dell'] = dell 

        
        #print('dell',dell)

        #print('middleware',up.message.message_id)
        #print('middleware',up.message.chat.id)

        mess_dell = {}
        #mess_dell['m'] = up.message.message_id
        #mess_dell['c'] = up.message.chat.id
        #print (data)
       
        data['mess_dell'] = mess_dell

      
        

        
        
        return await handler(event, data)
       