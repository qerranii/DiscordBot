import discord
from discord.ext import commands


def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    bot = commands.Bot(
        command_prefix='!',
        intents=intents,
        help_command=None  # Можно кастомный
    )

    @bot.event
    async def on_ready():
        print(f'Бот {bot.user} запущен!')
        print(f'На {len(bot.guilds)} серверах')

    return bot