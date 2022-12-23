import discord
import requests
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#dog && cat links
cat_urls = {
    "cat": "https://api.thecatapi.com/v1/images/search?limit=1",
    "maine coon": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=mcoo",
}
dog_urls = {
    "dog": "https://api.thedogapi.com/v1/images/search?limit=1",
    "shiba": "https://api.thedogapi.com/v1/images/search?limit=1&breed_id=222",
}

#api keys
for cat, url in cat_urls.items():
    cat_urls[cat] = f"{url}&api_key=API_KEY"

for dog, url in dog_urls.items():
    dog_urls[dog] = f"{url}&api_key=API_KEY"

#contents of the !help command
cathelp ="""
**main animals**
> !cat [generates a random cat picture]
> !dog [generates a random dog picture]
> !bird [generates a random bird picture]
**different dog breeds!!**
> !shiba
**different cat breeds!!**
> !maine coon
"""

#status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="how to get treats"))
    print('Watching status set to "free treats simulator" successfully.')

#listening for the !{breed} commands
@client.event
async def on_message(message):
    breed_commands = {
        "!cat": ("cat", cat_urls["cat"]),
        "!dog": ("dog", dog_urls["dog"]),
        "!shiba": ("Shiba Inu", dog_urls["shiba"]),
        "!maine coon": ("Maine Coon", cat_urls["maine coon"]),
    }
    #cat && dog commands
    if message.content in breed_commands:
        breed_name, breed_url = breed_commands[message.content]
        response = requests.get(breed_url)
        data = response.json()
        breed_image_url = data[0]["url"]
        color = random.randint(0, 16777215)
        embed = discord.Embed(color=color)
        embed.set_image(url=breed_image_url)
        await message.channel.send(f"Here is a {breed_name}:", embed=embed)

    #bird command
    if message.content == "!bird":
        color = random.randint(0, 16777215)
        embed = discord.Embed(color=color)
        response = requests.get("https://shibe.online/api/birds?count=1&urls=true&httpsUrls=false")
        data = response.json()
        bird_url = data[0]
        embed.set_image(url=bird_url)
        await message.channel.send(f"Here is a bird:", embed=embed)

    #help command
    elif message.content.startswith('!help'):
        color = random.randint(0, 16777215)
        embed = discord.Embed(title="!help", description="Here is a list of commands I can do...... ***farts cutely***", color=color)
        embed.add_field(name="Commands", value=cathelp)
        await message.channel.send(embed=embed)


# add your bot token here
client.run('TOKEN')