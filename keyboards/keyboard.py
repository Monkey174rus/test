from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder



# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text='yes_button')
button_no = KeyboardButton(text='no_button')

# Инициализируем билдер для клавиатуры с кнопками "Давай" и "Не хочу!"
yes_no_kb_builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с аргументом width=2
yes_no_kb_builder.row(button_yes, button_no, width=2)

# Создаем клавиатуру с кнопками "Давай!" и "Не хочу!"
yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------
def start_kb (i18n):
    # Создаем кнопки игровой клавиатуры
    button_1 = KeyboardButton(text=i18n.get('start'))
    #button_2 = KeyboardButton(text='scissors')
    #button_3 = KeyboardButton(text='paper')

    # Создаем игровую клавиатуру с кнопками "Камень 🗿",
    # "Ножницы ✂" и "Бумага 📜" как список списков
    start = ReplyKeyboardMarkup(
        keyboard=[[button_1]],
        resize_keyboard=True
        )
    return start