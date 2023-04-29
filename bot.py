from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_hi = KeyboardButton('Привет! 👋')
button_archive = KeyboardButton('Сжать файл ')
button_pdf = KeyboardButton('Собрать фото в pdf')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
greet_kb.add(button_archive)
greet_kb.add(button_pdf)

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['photo', 'document'])
async def doc_handler(message: types.Message):
    if document := message.document:
        await document.download()
        await bot.send_document(message.from_user.id, ('archive.zip', open("files/archive.zip", "rb")))


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup=greet_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
