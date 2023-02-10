import discord
import requests
import random
import datetime
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#dictionary of breeds
cat_urls = {
    "cat": "https://api.thecatapi.com/v1/images/search?limit=1",
    "munchkin": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=munc",
    "scottish fold": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=sfol",
    "russian blue": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=rblu",
    "tonkinese": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=tonk",
    "shadow": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=bomb",
}
dog_urls = {
    "dog": "https://api.thedogapi.com/v1/images/search?limit=1",
    "scout": "https://api.thedogapi.com/v1/images/search?limit=1&breed_id=50",
    "walter": "https://api.thedogapi.com/v1/images/search?limit=1&breed_id=61",
}

#status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="cute cat videos"))

#api keys
for cat, url in cat_urls.items():
    cat_urls[cat] = f"{url}&api_key=API_KEY_HERE"

for dog, url in dog_urls.items():
    dog_urls[dog] = f"{url}&api_key=API_KEY_HERE"

async def send_embedded_image(message, breed_name, breed_url):
    try:
        response = requests.get(breed_url)
        response.raise_for_status()
        data = response.json()
        breed_image_url = data[0]["url"]
        color = random.randint(0, 16777215)
        embed = discord.Embed(color=color)
        embed.set_image(url=breed_image_url)
        await message.channel.send(f"here is a {breed_name}:", embed=embed)
    except requests.exceptions.RequestException as e:
        await message.channel.send("An error occured, please try again later.")
        print(f"RequestException: {e}")

#commands
@client.event
async def on_message(message):
    breed_commands = {
        "!cat": ("cat", cat_urls["cat"]),
        "!dog": ("dog", dog_urls["dog"]),
        "!scout": ("border collie", dog_urls["scout"]),
        "!walter": ("bull terrier", dog_urls["walter"]),
        "!munchkin": ("munchkin", cat_urls["munchkin"]),
        "!shadow": ("black cat", cat_urls["shadow"]),
        "!scottish fold": ("scottish fold", cat_urls["scottish fold"]),
        "!russian blue": ("russian blue", cat_urls["russian blue"]),
        "!tonkinese": ("tonkinese cat", cat_urls["tonkinese"]),
    }
    if message.content in breed_commands:
        breed_name, breed_url = breed_commands[message.content]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("command_log.txt", "a") as file:
            file.write(f"Time: {now}, User ID: {message.author.id}, Command: {message.content}\n")
            print(f"User ID: {message.author.id}, Date: {datetime.datetime.now()}, Command: {message.content}")
        await send_embedded_image(message, breed_name, breed_url)
    if message.content.startswith('!help'):
        color = random.randint(0, 16777215)
        embed = discord.Embed(title="!help", description="here is a list of the animal commands i can do", color=color)
        embed.add_field(name="Commands", value=mhelp)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("command_log.txt", "a") as file:
            file.write(f"Time: {now}, User ID: {message.author.id}, Command: {message.content}\n")
            print(f"User ID: {message.author.id}, Date: {datetime.datetime.now()}, Command: {message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith('!cathelp'):
        color = random.randint(0, 16777215)
        embed = discord.Embed(title="!cathelp", description="here is a list of cat breed commands i can do", color=color)
        embed.add_field(name="Commands", value=chelp)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("command_log.txt", "a") as file:
            file.write(f"Time: {now}, User ID: {message.author.id}, Command: {message.content}\n")
            print(f"User ID: {message.author.id}, Date: {datetime.datetime.now()}, Command: {message.content}")
        await message.channel.send(embed=embed)
    if message.content.startswith('!doghelp'):
        color = random.randint(0, 16777215)
        embed = discord.Embed(title="!doghelp", description="here is a list of dog breed commands i can do", color=color)
        embed.add_field(name="Commands", value=dhelp)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("command_log.txt", "a") as file:
            file.write(f"Time: {now}, User ID: {message.author.id}, Command: {message.content}\n")
            print(f"User ID: {message.author.id}, Date: {datetime.datetime.now()}, Command: {message.content}")
        await message.channel.send(embed=embed)
    elif message.content.startswith('!shiba'):
        response = requests.get("https://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true")
        response.raise_for_status()
        data = response.json()
        breed_image_url = data[0]
        color = random.randint(0, 16777215)
        embed = discord.Embed(color=color)
        embed.set_image(url=breed_image_url)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("command_log.txt", "a") as file:
            file.write(f"Time: {now}, User ID: {message.author.id}, Command: {message.content}\n")
            print(f"User ID: {message.author.id}, Date: {datetime.datetime.now()}, Command: {message.content}")
        await message.channel.send(f"here is a shibu inu:", embed=embed)

#main help
mhelp = """
‎ 
**main commands!!**
> `!cat` [generates a random cat picture]
> `!dog` [generates a random dog picture]

***do `!cathelp` or `!doghelp` for a list of breeds!***
"""

#cat help
chelp = """
‎ 
**different cat breeds!!**
> `!shadow`
> `!munchkin`
> `!scottish fold`
> `!russian blue`
> `!tonkinese`
"""

#dog help
dhelp = """
‎ 
**different dog breeds!!**
> `!shiba`
> `!scout`
> `!walter`
"""

client.run('token')
