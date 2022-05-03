from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


TOKEN = '5184934459:AAG-6_Ktr_PZcws8_M_fuQRHFpj-XVN7hfs'
storage = MemoryStorage()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

