from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.markdown import hbold, hlink

import json
import os
import time

from utils import get_brands
from models import get_models
from details import get_detail

bot = Bot(token='5927159558:AAFslDjCx3gFsP9lUFtpoQFDVDw8ZdmPxzc', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):

    start_buttons = get_brands()
    keyboard = InlineKeyboardMarkup(row_width=2) # row_width

    for model in start_buttons:
        btn = InlineKeyboardButton(text=model, callback_data=model)
        keyboard.add(btn)

    await message.answer('Выберете марку', reply_markup=keyboard)

@dp.callback_query_handler()
async def models_callback(callback: types.CallbackQuery):
    if callback.data in get_brands():

        brand = callback.data
        models = get_models(brand.lower())

        keyboard = InlineKeyboardMarkup()

        for model in models:
            value = model.split()
            value = value[-1].lower()
            # print(value)
            btn = InlineKeyboardButton(text=model, callback_data=value)
            print(btn)
            keyboard.add(btn)

        await bot.send_message(chat_id= '5650732610',text='Выберите модель', reply_markup=keyboard)
        


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()