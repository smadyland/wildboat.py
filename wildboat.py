import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.tree.sync()

@client.tree.command(name="ping",description="Test bot responsiveness")
async def ping(Interaction: discord.Interaction):
    await Interaction.response.send_message("Pong!")

client.run(TOKEN)
