from aiogram.utils import executor
from creat_bot import dp
from handlers import clients, others, admin
from data_base import sql_db


async def on_startup(_):
    sql_db.start_db()
    print('the bot is on')


clients.register_handlers_client(dp)
admin.register_handler_admin(dp)
others.register_handler_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
