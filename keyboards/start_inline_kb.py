from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder




def create_start_keyboard(i18n,*buttons: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    
    kb_builder = InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kb_builder.row(*[InlineKeyboardButton(
        text=i18n.get(button) if button in i18n else button,
        callback_data=button) for button in buttons]
    )
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()