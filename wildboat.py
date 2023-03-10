import requests
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

@client.tree.command(name="raccoon", description="Get a random raccoon fact and image")
async def raccoon(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/raccoon")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Raccoon Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")

client.run(TOKEN)
