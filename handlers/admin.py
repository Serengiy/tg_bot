from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from creat_bot import bot
from keyboards import admin_kb
from data_base import sql_db


ID = None
menu = {'/Напитки_a': 'drinks', '/Горячее_a': 'hots', "/Салаты_a": 'salads'}



class FSMAdmin(StatesGroup):
    category = State()
    photo = State()
    name = State()
    description = State()
    price = State()


async def start_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Хозяин', reply_markup=admin_kb.admin_kb_start)
    await message.delete()



async def upload_category(meesage: types.Message):
    if meesage.from_user.id == ID:
        await FSMAdmin.category.set()
        await meesage.reply('Какая категория?', reply_markup=admin_kb.admin_kb_menu)


#Начало диалога загрузки
async def upload_menu(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        global CATEGORY_d
        CATEGORY_d = message.text
        await FSMAdmin.next()
        await message.reply('Загрузи фотку')

#Ловим фотку
async def upload_pic(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('А сейчас отправь название')


#Ловим название
async def upload_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Теперь описание')


#Ловим описание
async def upload_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Ну а теперь цену')


#Ловим прайс
async def upload_price(message: types.Message, state:FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
        await sql_db.add_to_menu(state, menu[CATEGORY_d])
        await state.finish()
        await message.reply('Ok')


async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ok')


async def delete_category(message: types.Message):
    if message.from_user.id == ID:
        await message.reply('Какую категорию?', reply_markup=admin_kb.admin_kb_menu)


async def delete_item(message: types.Message):
    global CATEGORY_d
    CATEGORY_d = message.text
    if message.from_user.id == ID:
        read = await sql_db.read_data2(menu[CATEGORY_d])
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^',
                                   reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(f'Удалить {ret[1]}',
                                                                                                callback_data=f'del {ret[1]}')))


async def del_callback_run(callback_query: types.CallbackQuery):
    await sql_db.delete_command(callback_query.data.replace('del ', ''), menu[CATEGORY_d])
    await callback_query.answer(text=f'{callback_query.data.replace("del ","")} удалена', show_alert=True)


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(upload_category, commands=['Загрузить'])
    dp.register_message_handler(upload_menu, commands=['Напитки_a', 'Горячее_a', 'Салаты_a'], state=FSMAdmin.category)
    dp.register_message_handler(upload_pic,content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(upload_name, state=FSMAdmin.name)
    dp.register_message_handler(upload_description, state=FSMAdmin.description)
    dp.register_message_handler(upload_price, state=FSMAdmin.price)
    dp.register_message_handler(cancel_handler, commands='отмена', state='*')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(delete_category, commands='Удалить')
    dp.register_callback_query_handler(del_callback_run,lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands=['Напитки_a', 'Горячее_a', 'Салаты_a'])

