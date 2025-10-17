
import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import commands, game, user

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_routers(commands.router, game.router, user.router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())