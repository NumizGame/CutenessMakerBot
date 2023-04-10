from aiogram import *
from config import *
from keyboards import *
from random import *
from asyncio import *

bot = Bot(token)
dispatcher = Dispatcher(bot)

async def on_startup(_):
    print('I am ready!!!')

help_text = '''
<b>▪️/start - starts the bot
▪️/help - shows you some info about bot's commands
▪️/description - shows you bot's description
▪️/back - returns you to the main keyboard menu
▪️/cuties - opens the keyboard, where you can choose a random kitten or a puppy
▪️/kitten - shows you a random kitten 🐈
▪️/puppy - shows you a random puppy 🐕
▪️/sticker - sends you a random cute sticker 🥰
</b>
'''


@dispatcher.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, '<b>Hi ! 😇</b>', parse_mode='HTML', reply_markup=main_keyboard)
    await message.delete()

@dispatcher.message_handler(commands=['help'])
async def help(message):
    await bot.send_message(message.chat.id, help_text, parse_mode='HTML')
    await message.delete()

@dispatcher.message_handler(commands=['description'])
async def description(message):
    await bot.send_message(message.chat.id, 'The Cutest bot in the world!!!🌏 It likes kittens, puppies and cute stickers 🥹')
    await message.delete()

@dispatcher.message_handler(commands=['cuties'])
async def open_cute_keyboard(message):
    await bot.send_message(message.chat.id, 'Here you are! 🥰', reply_markup=cute_keyboard)
    await message.delete()

@dispatcher.message_handler(commands=['back'])
async def return_to_main_menu(message):
    await bot.send_message(message.chat.id, '<em>Opening new keyboard...</em>', parse_mode='HTML')
    await sleep(1)
    await bot.send_message(message.chat.id, 'All is ready! 😚', reply_markup=main_keyboard)
    await message.delete()

@dispatcher.message_handler(commands=['kitten'])
async def send_kitten(message):
    await bot.send_photo(message.chat.id, kittens_urls[choice(range(10))], reply_markup=kitten_keyboard, caption=f'What a little cute kitten! 💗')
    await message.delete()

@dispatcher.message_handler(commands=['puppy'])
async def send_puppy(message):
    await bot.send_photo(message.chat.id, puppies_urls[choice(range(10))], reply_markup=puppy_keyboard, caption=f'What a little cute puppy! 💗')
    await message.delete()

@dispatcher.message_handler(commands=['sticker'])
async def send_stick(message):
    await bot.send_sticker(message.chat.id, stickers_urls[choice(range(10))], reply_markup=sticker_keyboard)
    await message.delete()

likes = 0
dislikes = 0
current_mes = ''    #current message

@dispatcher.callback_query_handler()
async def reaction_handler(callback):
    global likes, dislikes, current_mes
    if current_mes != callback.message.message_id:  #if the message has changed
        current_mes = callback.message.message_id   #here we swap current message with new
        likes = 0
        dislikes = 0

    #likes/dislikes checker
    if callback.data == 'like' and likes == 0:
        likes += 1      #if you press a 'like', the 'dislike' is removed
        dislikes = 0
        await callback.answer('Oh, it is so cute 🥹')
    elif callback.data == 'dislike' and dislikes == 0:
        dislikes += 1   #if you press a 'dislike', the 'like' is removed
        likes = 0
        await callback.answer('Oh, I\'m sorry, you didn\'t like the picture 😞')

    #next kitten/puppy handler
    elif callback.data == 'next_kitten':
        await bot.send_photo(callback.message.chat.id, kittens_urls[choice(range(10))], reply_markup=kitten_keyboard, caption=f'What a little cute kitten! 💗')

    elif callback.data == 'next_puppy':
        await bot.send_photo(callback.message.chat.id, puppies_urls[choice(range(10))], reply_markup=puppy_keyboard, caption=f'What a little cute puppy! 💗')

    elif callback.data == 'next_sticker':
        await bot.send_sticker(callback.message.chat.id, stickers_urls[choice(range(10))], reply_markup=sticker_keyboard)

    else:
        await callback.answer('Sorry, but you have already voted 😔')

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)