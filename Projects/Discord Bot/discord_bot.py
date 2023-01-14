import discord
import os
import config
from discord.ext.commands import Bot
from random import choice

advice = ["Eat your vegetables", "Stay away from drugs", "Beat up your teacher"]

# Doing some stuff so that it diddles files from the same directory where this file is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

intents = discord.Intents.default()
intents.message_content = True #This has to be checked off on https://discord.com/developers/applications/ - "Bot" tab

client = discord.Client(intents=intents)
#bot = Bot(intents=intents)
#client=commands.Bot(command_prefix=".")

#text_channel_list = []
#for server in client.servers:
    #for channel in server.channels:
        #if channel.type == 'Text':
            #text_channel_list.append(channel)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(135806531672211456)
    await channel.send("*momBOT online*")

@client.event
async def on_message(message):
    if message.author != client.user:
        # Reading file in directory
        f = open(os.path.join(__location__, 'bad_words.txt'), "r") # Open and read input file
        for i in f:
            if i in message.content:
                message.reply("yeet")
                print(i)
        f.close()
    
    # Writing chatlog to log.txt
    f2 = open(os.path.join(__location__, 'log.txt'), "a", encoding="utf-8") #open and write to output file, encoding added to allow emojis
    f2.write(f"{str(message.author)}: {str(message.author.name)} : {str(message.content)}\n") #Write to output file
    f2.close()

    
    if message.author == client.user:
        return
    

    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/advice'):
        await message.reply(f"momBOT advice: {choice(advice)}")
    
    if message.content.startswith("bruh"):
        await message.channel.send("https://www.youtube.com/watch?v=TKuLxJCArmg")

    if message.content.startswith("we") or message.content.startswith("We"):
        await message.channel.send('..finish')
    
    if message.content.startswith("each") or message.content.startswith("Each"):
        await message.channel.send("..other's sentences")

    

client.run(config.bot_token)
