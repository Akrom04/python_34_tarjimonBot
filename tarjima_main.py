from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import Message
import logging
from translate import tarjima


logging.basicConfig(level=logging.INFO)
bot = Bot(token="6124176529:AAGk0oSpRuthBndQVuMHeSeWY5IR6w_o8hg")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def salomlash(message: types.Message):
    await message.answer("Assalomu Aleykom!!!!\nSo'zni kiriting")


@dp.message_handler()
async def tarjima1(message: types.Message):

    text=message.text

    await message.reply(tarjima(text))
   

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)