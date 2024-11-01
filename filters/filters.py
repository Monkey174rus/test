from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject

class User_Login(BaseFilter):

    async def __call__(self,  event: TelegramObject, state_us) -> bool:

        if state_us is not None:
            return True
        return False


