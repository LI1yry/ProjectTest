from pyrogram.types import KeyboardButton, InlineKeyboardButton

from pyrogram import emoji

# Общие кнопки
back_button = KeyboardButton(f"{emoji.BACK_ARROW} Назад")

# Кнопки главного меню
time_button = KeyboardButton(f"{emoji.ALARM_CLOCK} Время")
help_button = KeyboardButton(f"{emoji.WHITE_QUESTION_MARK} Помощь")
settings_button = KeyboardButton(f"{emoji.GEAR} Настройки")
search_films_button = KeyboardButton(f"{emoji.SUN_BEHIND_CLOUD} Выбор фильма")

# Кнопки настроек
random_films_button = KeyboardButton(f"{emoji.CITYSCAPE} Рандомный фильм")

cats_button = KeyboardButton(f"{emoji.BUS} Транспорты")

cat_random_inline_button = InlineKeyboardButton(f"{emoji.CAT} Случайный транспорт", callback_data="cat_random")