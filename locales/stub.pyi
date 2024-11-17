from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    hello: Hello
    button: Button
    account: Account
    no: No

    @staticmethod
    def question() -> Literal["""Вы уверены что хотите удалить аккаунт?"""]: ...


class Hello:
    @staticmethod
    def user(*, username) -> Literal["""Привет, { $username }.

Это бот, в котором ты можешь 
получить рекомендации от ИИ.

Чтобы посмотреть список доступных
команд - набери /help"""]: ...


class Button:
    @staticmethod
    def register() -> Literal["""Регистрация"""]: ...

    @staticmethod
    def start() -> Literal["""Начать"""]: ...

    @staticmethod
    def control() -> Literal["""Aккаунт"""]: ...

    @staticmethod
    def delete() -> Literal["""Удалить аккаунт"""]: ...

    @staticmethod
    def login() -> Literal["""Войти"""]: ...

    @staticmethod
    def exit() -> Literal["""Выйти"""]: ...

    @staticmethod
    def yes() -> Literal["""Да"""]: ...

    @staticmethod
    def no() -> Literal["""Нет"""]: ...

    @staticmethod
    def pressed() -> Literal["""Вы нажали на кнопку"""]: ...


class Account:
    @staticmethod
    def text() -> Literal["""bla bla bla"""]: ...


class No:
    @staticmethod
    def copy() -> Literal["""Данный тип апдейтов не поддерживается методом send_copy"""]: ...

