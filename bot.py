import os
import openai
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests
from io import BytesIO
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message


# Set up Telegram bot
bot = Bot(token='5722175251:AAGac_Wtg6oJVLBJNuTLLLl7a8TBLJtsoQY')
dispatcher = Dispatcher(bot)


openai.api_key = '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'


# Handle incoming messages
@dispatcher.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    # Send a response message
    await bot.send_message(chat_id=message.chat.id, text='Hello! Im GPT chat bot.Ask me something!!')


# Handle incoming messages
@dispatcher.message_handler()
async def handle_message(message: types.Message):
    # Send a response message
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    await bot.send_message(chat_id=message.chat.id, text=response.choices[0].text)


# Define a message handler for the /image command
@dispatcher.message_handler(commands=["image"])
async def generate_image(message: Message):
    # Get user input from the message
    user_input = " ".join(message.text.split()[1:])

    # Generate image using GPT-3 API
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input + "\nGenerate an image of the above text:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    )

    # Get image URL from GPT-3 API response
    image_url = response.choices[0].text.strip()

    # Download image from URL
    image_bytes = BytesIO(requests.get(image_url).content)

    # Send image to user
    await bot.send_photo(chat_id=message.chat.id, photo=image_bytes, caption="Here is your generated image!")


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dispatcher)
