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
# cat
@client.tree.command(name="cat", description="Get a random cat image")
async def cat(Interaction: discord.Interaction):
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Cat Image", color=discord.Color.blurple())
        embed.set_image(url=data[0]["url"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# dog
@client.tree.command(name="dog", description="Get a random dog image")
async def dog(Interaction: discord.Interaction):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Dog Image", color=discord.Color.blurple())
        embed.set_image(url=data["message"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# shiba
@client.tree.command(name="shiba", description="Get a random shiba image")
async def shibe(Interaction: discord.Interaction):
    response = requests.get("http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Shiba Inu Image", color=discord.Color.blurple())
        embed.set_image(url=data[0])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# raccoon
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
# panda
@client.tree.command(name="panda", description="Get a random panda fact and image")
async def panda(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/panda")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Panda Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# koala
@client.tree.command(name="koala", description="Get a random koala fact and image")
async def koala(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/koala")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Koala Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# kangaroo
@client.tree.command(name="kangaroo", description="Get a random kangaroo fact and image")
async def kangaroo(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/kangaroo")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Kangaroo Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# fox
@client.tree.command(name="fox", description="Get a random fox fact and image")
async def kangaroo(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/fox")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Fox Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# red panda
@client.tree.command(name="red-panda", description="Get a random red panda fact and image")
async def kangaroo(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/red_panda")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Red Panda Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
# bird
@client.tree.command(name="bird", description="Get a random bird fact and image")
async def kangaroo(Interaction: discord.Interaction):
    response = requests.get("https://some-random-api.ml/animal/bird")
    if response.status_code == 200:
        data = response.json()
        embed = discord.Embed(title="Random Bird Fact", description=data["fact"], color=discord.Color.blurple())
        embed.set_image(url=data["image"])
        await Interaction.response.send_message(embed=embed)
    else:
        await Interaction.response.send_message("Failed to fetch data from the API")
client.run(TOKEN)
