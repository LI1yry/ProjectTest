from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

import buttons

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.time_button, buttons.search_films_button],
        [buttons.help_button, buttons.settings_button, buttons.cats_button],
    ],
    resize_keyboard=True,
)

settings_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [buttons.random_films_button, buttons.back_button],
    ],
    resize_keyboard=True,
)

cats_inline_keyboard = InlineKeyboardMarkup(
    [
        [buttons.cat_random_inline_button]
    ],
)