import asyncio
import logging
from handlies import router
from aiogram import Bot, Dispatcher
from config import TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from data.mosels import async_main
from aiogram.types import BotCommand
from middleeware import MediaMiddlewareCountClick


bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.callback_query.middleware.register(MediaMiddlewareCountClick())
async def set_commands(bot: Bot):
    commands = [BotCommand(command='start', description='😁Начать'),]
    await bot.set_my_commands(commands)

async def main():
    dp.include_router(router)
    await set_commands(bot)
    await async_main()
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")