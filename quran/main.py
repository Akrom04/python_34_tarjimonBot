from aiogram import Dispatcher, Bot, executor,types
from aiogram.types import Message
import logging
from quran.quran import suralar_qaytar

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6124176529:AAGk0oSpRuthBndQVuMHeSeWY5IR6w_o8hg")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def salomlash(message: types.Message):
    await message.answer("Assalomu Aleykom!!!!\nSura raqamini kiriting")


@dp.message_handler()
async def quran(message: types.Message):

    sura = message.text
    try:
        if sura.isnumeric():
            suralar=suralar_qaytar(sura)
            for sura in suralar['chapter']:
                await message.answer(f"Sura:{sura['chapter']}\nOyat: {sura['verse']}\n{sura['text']}")
        elif '/' in sura:
            suralar=suralar_qaytar(sura)
            await message.reply(f"Text: {suralar  ['text']}")
    except:
        await message.reply("Bunday sura mavjud emas????")


    # oyat=message.text
    # oyat1 = quran(sura)
    # natija2 = oyat1['chapter']
  
    # for i in natija2:
    #     await message.answer(f"chapter: {i['chapter']},\nverse {i['verse']},\n\ntext: {i['text']}")
        


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
