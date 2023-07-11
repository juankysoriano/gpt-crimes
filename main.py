import logging
import os

import openai
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

from engine.game import CrimeGame

logging.basicConfig(level=logging.DEBUG)
load_dotenv()
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

bot = Bot(token=telegram_bot_token)
openai.api_key = openai_api_key
dp = Dispatcher(bot)
game = CrimeGame()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    intro_text = game.intro()
    await message.bot.send_message(
        message.chat.id, intro_text, parse_mode="Markdown"
    )

    scene = await game.new_story()

    await _display_story(message, scene)


async def _display_story(message: types.Message, scene):
    actions = scene["display"]["available_actions"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*actions)
    text = scene["display"]["text"]
    current_scene = scene["display"]["taken_actions"]
    total_scenes = scene["display"]["total_actions"]
    percentage = (current_scene / total_scenes) * 100
    await message.bot.send_message(
        message.chat.id,
        f"*Progress*: {percentage}%\n\n{text}",
        parse_mode="Markdown",
        reply_markup=keyboard,
    )

    await message.bot.send_photo(
        message.chat.id, scene["display"]["image"], reply_markup=keyboard
    )


@dp.message_handler(commands=["restart"])
async def reset(message: types.Message):
    game.restart()
    await start(message)


@dp.message_handler(content_types=types.ContentType.TEXT)
async def take_option(message: types.Message):
    scene = await game.take_option(message.text)

    await _display_story(message, scene)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
