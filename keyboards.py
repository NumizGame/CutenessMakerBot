from aiogram.types import *

return_button = KeyboardButton('/back')     #button to return to the main keyboard menu

#first keyboard
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
help_but = KeyboardButton('/help')
desc_but = KeyboardButton('/description')
cute_but = KeyboardButton('/cuties')
main_keyboard.add(help_but, desc_but).add(cute_but)

#second keyboard
cute_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
kitten_but = KeyboardButton('/kitten')
puppy_but = KeyboardButton('/puppy')
sticker_but = KeyboardButton('/sticker')
cute_keyboard.add(kitten_but, puppy_but, sticker_but).add(return_button)

#common buttons for 3th, 4th and 5th keyboards
like_button = InlineKeyboardButton('👍', callback_data='like')
dislike_button = InlineKeyboardButton('👎', callback_data='dislike')

#third keyboard
kitten_keyboard = InlineKeyboardMarkup(row_width=2)
next_kitten = InlineKeyboardButton('Next kitten 😇 -->>', callback_data='next_kitten')
kitten_keyboard.add(like_button, dislike_button, next_kitten)

#fourth keyboard
puppy_keyboard = InlineKeyboardMarkup(row_width=2)
next_puppy = InlineKeyboardButton('Next puppy 😇 -->>', callback_data='next_puppy')
puppy_keyboard.add(like_button, dislike_button, next_puppy)

#fifth keyboard
sticker_keyboard = InlineKeyboardMarkup(row_width=2)
next_sticker = InlineKeyboardButton('Next cute sticker 😇 -->>', callback_data='next_sticker')
sticker_keyboard.add(like_button, dislike_button, next_sticker)