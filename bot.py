import subprocess
import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.bot.api import TelegramAPIServer

from config import TOKEN
from keybords import greet_kb

logging.basicConfig(level=logging.INFO)
local_server = TelegramAPIServer.from_base('http://127.0.0.1:8081/')
bot = Bot(token=TOKEN, server=local_server)
dp = Dispatcher(bot)


@dp.message_handler(commands=["zip"])
@dp.message_handler(Text("Сжать файл"))
async def doc_info(message: types.Message):
    await message.answer("Отправьте файл <= 20 Mb (пока)")


@dp.message_handler(commands=["pdf"])
@dp.message_handler(Text("Собрать фото в pdf"))
async def photo_info(message: types.Message):
    await message.answer("Отправьте файлы")


@dp.message_handler(commands=["unzip"])
@dp.message_handler(Text("Разархивировать файл"))
async def doc_info(message: types.Message):
    await message.answer("Отправьте zip архив <= 20 Mb (пока)")


@dp.message_handler(content_types=['photo'])
async def photo_handler(message: types.Message):
    print("photo")
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)


@dp.message_handler(content_types=['document'])
async def echo(message: types.Message):
    print("document")
    file_id = message.document.file_id
    file = await bot.get_file(file_id)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=greet_kb)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    # bot.log_out()
    executor.start_polling(dp)
