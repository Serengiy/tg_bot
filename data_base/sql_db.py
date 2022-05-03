import sqlite3 as sq
from creat_bot import bot
from keyboards import client_kb


def start_db():
    global base, cur
    base = sq.connect('cafe_na_solnishke.db')
    cur = base.cursor()
    if base:
        print('Data base is ok')
    base.execute('CREATE TABLE IF NOT EXISTS drinks(img TEXT, name TEXT, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS salads(img TEXT, name TEXT, description TEXT, price TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS hots(img TEXT, name TEXT, description TEXT, price TEXT)')
    base.commit()


async def read_data(message, category):
    for i in cur.execute(f'SELECT * FROM {category}'):
        await bot.send_photo(message.from_user.id, i[0] ,f'\nНазвание{i[1]}\nОписание: {i[2]}\nЦена:{i[3]}',
                               reply_markup=client_kb.second_act)



async def read_data2(category):
    return cur.execute(f'SELECT * from {category}')


async def add_to_menu(state, category):
    async with state.proxy() as data:
        cur.execute(f'INSERT INTO {category} VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()


async def delete_command(data, category):
    cur.execute(f'DELETE FROM {category} WHERE name == ?', (data,))
    base.commit()

