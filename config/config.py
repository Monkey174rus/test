from environs import Env

from dataclasses import dataclass


@dataclass
class TgBot:
    token: str

@dataclass
class Db:
    name: str
    user: str
    password: str
    port: int
    host: str

    def __post_init__(self):
        self.url = f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}'

@dataclass
class Redis:
    host: str
    port: int
    num_db: int
    username: str
    password: str

    def __post_init__(self):
                self.url = f'redis://{self.username}:{self.password}@{self.host}:{self.port}/{self.num_db}'
@dataclass
class Config:
    tg_bot: TgBot
    db: Db
    redis: Redis

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()
    return Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN')
        ),
        redis=Redis(
            host=env('REDIS_HOST'),
            port=env('REDIS_PORT'),
            num_db=env('REDIS_NUM_DB'),
            username=env('REDIS_USERNAME'),
            password=env('REDIS_PASSWORD')
        ),
        db=Db(
            host=env('DB_HOST'),
            name=env('DATABASE'),
            user=env('DB_USER'),
            password=env('DB_PASSWORD'),
            port=env('DB_PORT')
        )

    )