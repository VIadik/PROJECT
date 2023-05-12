from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib_url = InlineKeyboardButton(text="url", callback_data="url")
ib_text = InlineKeyboardButton(text="text", callback_data="text")
ib_email = InlineKeyboardButton(text="email", callback_data="email")
ib_event = InlineKeyboardButton(text="event", callback_data="event")

ikb: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[ib_url],
                     [ib_text],
                     [ib_email],
                     [ib_event]])
