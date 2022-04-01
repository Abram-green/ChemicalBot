from aiogram import Bot, types
from aiogram.types import InputFile
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from prik import priks

import ast

TOKEN = 'Телеграм бот токен. Получить можно у @BotFather'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button_reference = KeyboardButton('📕 Справка')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
keyboard.add(button_reference)

reference = """Справка:
Я принимаю общие (C2H2, C2H5OH, C3H6O) формулы и возвращаю название соединения.
Распознаю такие типы соединений как: 
Алканы, 
Циклоалканы,
Алкены, 
Циклоалкены,
Алкины, 
Алкадиены, 
Альдегиды, 
Кетоны, 
1,2,3-атомные первичные спирты, 
Карбоновые кислоты. 
"""

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Люблю приколы в химии")
    await message.answer(reference, reply_markup=keyboard)

@dp.message_handler(commands=['reference'])
async def process_reference_command(message: types.Message):
    await message.answer(reference, reply_markup=keyboard)

@dp.message_handler()
async def on_message(message: types.Message):
    r = priks(message.text)
    if message.text == "📕 Справка":
        await message.answer(reference, reply_markup=keyboard)
    elif type(r) == tuple:
        for i in r:
            await message.reply(i.capitalize())
    elif type(r) == str:
        await message.reply(r.capitalize())
    else:
        await message.reply("Я не знаю такой формулы😢", reply_markup=keyboard   )


if __name__ == '__main__':
    executor.start_polling(dp)