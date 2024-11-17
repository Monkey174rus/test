from aiogram.filters import BaseFilter
from aiogram.types import Message ,TelegramObject
from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

class Dell_25(BaseFilter):
     
    
    

    async def __call__(self, event: TelegramObject, dell,bot:Bot)-> bool:
        
        


        if dell.get('m') and dell.get('c') is not None:
            #if dell['m'] != message.message_id and dell['c'] == message.chat.id :
            try:
                await bot.edit_message_reply_markup(chat_id=dell['c'], message_id=dell['m'],reply_markup=None)
                
            except TelegramBadRequest:
                return True

        return True

        
           



