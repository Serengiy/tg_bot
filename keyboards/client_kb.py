from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/Адрес')
b2 = KeyboardButton('/О_нас')
b3 = KeyboardButton('/Меню')

first_act = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
first_act.row(b1, b2, b3)

b4 = KeyboardButton('/Напитки')
b5 = KeyboardButton('/Горячее')
b6 = KeyboardButton('/Салаты')
b7 = KeyboardButton('/Главное_меню')

second_act = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
second_act.row(b4, b5, b6).add(b7)


