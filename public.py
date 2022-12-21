# DO NOT MESS WITH CODE UNTILL LINE 7 OR THE BOT WILL NOT START

import requests
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# cat & cat breed example
cat_urls = {
    "cat": "https://api.thecatapi.com/v1/images/search?limit=1",
    "maine coon": "https://api.thecatapi.com/v1/images/search?limit=1&breed_id=mcoo",
}

# dog & dog breed example
dog_urls = {
    "dog": "https://api.thedogapi.com/v1/images/search?limit=1",
    "shiba": "https://api.thedogapi.com/v1/images/search?limit=1&breed_id=222",
}

# cat api key
for cat, url in cat_urls.items():
    cat_urls[cat] = f"{url}&api_key=REPLACE_WITH_API_KEY"

# dog api key
for dog, url in dog_urls.items():
    dog_urls[dog] = f"{url}&api_key=REPLACE_WITH_API_KEY"

# help commands data (what will be in the help command)
cathelp ="""
add anything here.. it will be your help command
make sure to add newlines (its a multiline string)
"""

# status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ANYTHING_U_WANT_IT_TO_SAY"))
    # .playing, .watching .streaming .listening are all valid options

@client.event
async def on_message(message):
# dog and cat commands
    if message.content == "!cat":
        response = requests.get(cat_urls["cat"])
        data = response.json()
        cat_url = data[0]["url"]
        embed = discord.Embed()
        embed.set_image(url=cat_url)
        await message.channel.send(embed=embed)

    if message.content == "!dog":
        response = requests.get(dog_urls["dog"])
        data = response.json()
        cat_url = data[0]["url"]
        embed = discord.Embed()
        embed.set_image(url=cat_url)
        await message.channel.send(embed=embed)
#dog breed
    if message.content == "!shiba":
        response = requests.get(dog_urls["shiba"])
        data = response.json()
        cat_url = data[0]["url"]
        embed = discord.Embed()
        embed.set_image(url=cat_url)
        await message.channel.send(embed=embed)

# cat breed
    if message.content == "!maine coon":
        response = requests.get(cat_urls["maine coon"])
        data = response.json()
        cat_url = data[0]["url"]
        embed = discord.Embed()
        embed.set_image(url=cat_url)
        await message.channel.send(embed=embed)

# the actual help command itself
    if message.content.startswith('!help'):
        embed = discord.Embed(title="!help", description="Here is a list of commands I can do‎ ‎ ‎ ‎ ‎ ‎" + "*farts cutely*")
        embed.add_field(name="Commands", value=cathelp)
        await message.channel.send(embed=embed)

# add your bots token here or it will not run obviously..
client.run('YOUR_BOT_TOKEN')