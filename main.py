from collections import defaultdict

from pyrogram import Client, filters
from pyrogram.types import Message,  CallbackQuery,InputMediaPhoto

import buttons
import config
import keyboards
from custom_filters import button_filter, inline_button_filter
from random_cat import get_random_cat


bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="my_cool_bot",
)

@bot.on_message(filters=filters.command("help") | button_filter(buttons.help_button))
async def help_command(client: Client, message: Message):
    commands = await bot.get_bot_commands()
    text_commands = ""
    for command in commands:
        text_commands += f"/{command.command} - {command.description}\n"
    await message.reply(f"Список доступных команд:\n{text_commands}")


@bot.on_message(filters=filters.command("start") | button_filter(buttons.back_button))
async def start_command(client: Client, message: Message):
    await message.reply(
        "Привет! Я бот, который умеет считать и показывать время.\n"
        f"Нажми на кнопку {buttons.help_button.text} для получения списка команд.",
        reply_markup=keyboards.main_keyboard
    )


@bot.on_message(filters=filters.command("transport") | button_filter(buttons.cats_button))
async def cats_command(client: Client, message: Message):
    cat = get_random_cat()
    await client.send_photo(
        chat_id=message.chat.id,
        photo=cat,
        reply_markup=keyboards.cats_inline_keyboard,
    )

@bot.on_callback_query(filters=inline_button_filter(buttons.cat_random_inline_button))
async def cats_random_inline_button_callback(client: Client, query: CallbackQuery):
    cat = get_random_cat()
    await query.message.edit_media(
        media=InputMediaPhoto(cat),
        reply_markup=keyboards.cats_inline_keyboard,
    )


bot.run()