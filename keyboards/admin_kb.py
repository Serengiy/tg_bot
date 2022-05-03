from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


b1 = KeyboardButton('/Загрузить')
b2 = KeyboardButton('/Удалить')

admin_kb_start = ReplyKeyboardMarkup().add(b1).add(b2)

b3 = KeyboardButton('/Напитки_a')
b4 = KeyboardButton('/Горячее_a')
b5 = KeyboardButton('/Салаты_a')

admin_kb_menu = ReplyKeyboardMarkup().add(b3).add(b4).add(b5)
