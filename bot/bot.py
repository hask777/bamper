from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
# from main import collect_data
import json
import os
import time

from models import get_models

bot = Bot(token='5927159558:AAFslDjCx3gFsP9lUFtpoQFDVDw8ZdmPxzc', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):

    with open('br_list.json', 'r', encoding='utf-8') as f:
        br = json.load(f)

    start_buttons = br

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(*start_buttons)    

    await message.answer('Выберете марку', reply_markup=keyboard)

with open('br_list.json', 'r', encoding='utf-8') as f:
    mds = json.load(f)
    print(mds)

@dp.message_handler(Text(equals=mds))
async def get_md(message: types.Message):

    brand = message.text
   
    models_buttons = get_models(brand.lower())

    print(get_models(brand.lower()))

    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(*models_buttons)    

    await message.answer('Выберете модель', reply_markup=keyboard)

@dp.message_handler()
async def get_discount_knifes(message: types.Message):
    await message.answer('Выберете запчасть')

def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()