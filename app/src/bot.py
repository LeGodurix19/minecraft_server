import asyncio
from actionsCommand.statusServer import statusServer
from db_init import init_db
from functions import executeCommand
import discord
from discord.ext import tasks
import os
import docker

# Initialisation du client Docker
client = docker.from_env()

# Initialisation du client Discord
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

# Récupération du token depuis les variables d'environnement
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

if not DISCORD_TOKEN:
    raise ValueError("Le token Discord n'est pas défini. Assurez-vous que la variable d'environnement DISCORD_TOKEN est correctement définie.")

@bot.event
async def on_ready():
    init_db()
    await bot.change_presence(activity=discord.CustomActivity(name="Dev by @legodurix"))
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    await executeCommand(message, client, bot)

bot.run(DISCORD_TOKEN)