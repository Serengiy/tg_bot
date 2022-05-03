from aiogram import types
from aiogram.dispatcher import Dispatcher
from creat_bot import bot
from keyboards import client_kb
from data_base import sql_db


menu = {'/Напитки': 'drinks', '/Горячее': 'hots', "/Салаты": 'salads'}


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=client_kb.first_act)
        await message.delete()
    except:
        await message.reply('Общение с ботом в лс напишите ему\nhttps://t.me/Cafe_na_solnishke_bot')


async def cafe_address(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь ты увидишь адреса', reply_markup=client_kb.first_act)


async def cafe_about(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здесь ты увидишь информацию о нас', reply_markup=client_kb.first_act)


async def cafe_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот что у нас есть', reply_markup=client_kb.second_act)


async def cafe_category_menu(message: types.Message):
    CATEGORY = message.text
    await sql_db.read_data(message, menu[CATEGORY])


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'Главное_меню'])
    dp.register_message_handler(cafe_address, commands=['Адрес'])
    dp.register_message_handler(cafe_about, commands=['О_нас'])
    dp.register_message_handler(cafe_menu, commands=['Меню'])
    dp.register_message_handler(cafe_category_menu, commands=['Напитки', 'Горячее', 'Салаты'])