from database.models import User
from sqlalchemy.ext.asyncio import AsyncSession

class Database:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, id: int, username:str) -> None:
        user = await self.session.get(User, id)
        if not user:
            user = User(
                id=id,
                username=username
            )
            self.session.add(user)
        await self.session.commit()
    

    async def get_user_data(self, id: int, username:str) -> User:
        user = await self.session.get(User, id, username)
        return user




