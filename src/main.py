import os

from bot.client import create_bot
import asyncio
from routers import * # вместо * вписать конкретно класс
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

async def main():
    bot = create_bot()

    # загрузка роуетров по типу user.setup(bot)

    await bot.start(TOKEN)

#
if __name__ == "__main__":
    asyncio.run(main())