import asyncio
import subprocess

from inline_keyboards import ikb

from aiogram import Bot, Dispatcher, F
from aiogram import types
from aiogram.types import FSInputFile
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram.client.telegram import TelegramAPIServer

from config import TOKEN

session = AiohttpSession(api=TelegramAPIServer.from_base('http://127.0.0.1:8081/'))
bot = Bot(token=TOKEN, session=session)
dp = Dispatcher()

HELP_COMMAND = """
start - начало работы
help - список команд
zip - сжать файл/файлы в один архив
unzip - разархивировать zip архив
pdf - конвертировать файл/файлы в один pdf файл
qr - создать qr-code
"""

storage: MemoryStorage = MemoryStorage()


# class FSMFillForm(StatesGroup):
#     # Создаем экземпляры класса State, последовательно
#     # перечисляя возможные состояния, в которых будет находиться
#     # бот в разные моменты взаимодейтсвия с пользователем
#     fill_name = State()  # Состояние ожидания ввода имени
#     fill_age = State()  # Состояние ожидания ввода возраста
#     fill_gender = State()  # Состояние ожидания выбора пола
#     upload_photo = State()  # Состояние ожидания загрузки фото
#     fill_education = State()  # Состояние ожидания выбора образования
#     fill_wish_news = State()  # Состояние ожидания выбора получать ли новости


@dp.message(Command("qr"))
async def generate_qr(message: types.Message):
    await message.answer("Выберейте тип данных, который Вы хотите закодировать.", reply_markup=ikb)
    # await state.set_state(FSMFillForm.fill_name)


# @dp.callback_query()
# async def get_callback(callback: types.CallbackQuery):
#     if callback.data == "url":
#         await callback.message.answer("Отправь ссылку на ресурс.")
#     if callback.data == "text":
#         await callback.message.answer("Отправь текстовое сообщение")
#     if callback.data == "email":
#         await callback.message.answer("Отправь электронный адрес")
#     if callback.data == "event":
#         await callback.message.answer("Отправь место события")
#         await callback.message.answer("Отправь время и дату события")


@dp.message(Command("zip"))
@dp.message(lambda message: message.text == 'Сжать файл')
async def doc_info(message: types.Message):
    await message.answer("Отправьте файл/файлы одним сообщением")


@dp.message(Command("pdf"))
@dp.message(lambda message: message.text == "Собрать фотографии в pdf")
async def photo_info(message: types.Message):
    await message.answer("Отправьте фото/фотографии одним сообщением")


@dp.message(Command("unzip"))
@dp.message(lambda message: message.text == 'Разархивировать файл')
async def doc_info(message: types.Message):
    await message.answer("Отправьте zip архив")


@dp.message(lambda message: message.content_type == 'photo')
async def photo_handler(message: types.Message):
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    subprocess.run("python3 pdf.py", shell=True)
    file = FSInputFile("data/doc.pdf", filename="result.pdf")
    await bot.send_document(message.from_user.id, file)


@dp.message(lambda message: message.content_type == 'document')
async def document_hander(message: types.Message):
    file_id = message.document.file_id
    file = await bot.get_file(file_id)
    subprocess.run("python3 zip.py", shell=True)
    file = FSInputFile("data/archive.zip", filename="result.zip")
    await bot.send_document(message.from_user.id, file)


@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(HELP_COMMAND)


@dp.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.answer("Привет! Отправь команду /help, чтобы узнать что умеет этот бот")


@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
