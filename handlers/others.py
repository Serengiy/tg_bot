import json
import string

from aiogram import types
from aiogram.dispatcher import Dispatcher
from creat_bot import bot, dp

s = 'dadadads'

async def mat_cheking(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Мат в чате запрещен')
        await message.delete()



def register_handler_other(dp: Dispatcher):
    dp.register_message_handler(mat_cheking)

