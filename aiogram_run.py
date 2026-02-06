import asyncio
from create_bot import bot, dp
from handlers.start import start_router
from handlers.work_with_db import db_router, db_object
from handlers.user_info import info_router

async def main():
    try:
        db_object.create_user_table()
        dp.include_routers(start_router, db_router, info_router)
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        db_object.close()

if __name__ == '__main__':
    asyncio.run(main())