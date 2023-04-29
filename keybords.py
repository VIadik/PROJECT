from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_hi = KeyboardButton('Привет! 👋')
button_archive = KeyboardButton('Сжать файл')
button_pdf = KeyboardButton('Собрать фото в pdf')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
greet_kb.add(button_archive)
greet_kb.add(button_pdf)
