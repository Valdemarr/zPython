import discord
import os
import config
from discord.ext.commands import Bot
from random import choice
import lists

# Doing some stuff so that it diddles files from the same directory where this file is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

#Necessary Discord setup stuff
intents = discord.Intents.default()
intents.message_content = True #This has to be checked off on https://discord.com/developers/applications/ too - "Bot" tab
client = discord.Client(intents=intents)

@client.event #Start event i guess
async def on_ready(): #Which event
    print(f'We have logged in as {client.user}')

    channel = client.get_channel(1063887939219767376) #The channel to send message to
    await channel.send("*momBOT online*")

@client.event
async def on_message(message):
    if message.author != client.user:
        for i2 in lists.bad_words:
            if i2 in message.content:
                await message.reply(lists.bad_words_reply[0].format(message.author.name)) #This doesn't work yet
    
    # Writing chatlog to log.txt
    f2 = open(os.path.join(__location__, 'log.txt'), "a", encoding="utf-8") #open and write to output file, encoding added to allow emojis
    f2.write(f"{str(message.author)}: {str(message.content)}\n") #Write to output file
    f2.close()

    
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/advice'):
        await message.reply(f"{message.author.name} {choice(lists.advice)}")
    
    if message.content.startswith("bruh"):
        await message.channel.send("https://www.youtube.com/watch?v=TKuLxJCArmg")

    if message.content.startswith("we") or message.content.startswith("We"):
        await message.channel.send('..finish')
    
    if message.content.startswith("each") or message.content.startswith("Each"):
        await message.channel.send("..other's sentences")

    if message.content.startswith("/recall"):
        pass

client.run(config.bot_token) #Runs using token from config.py
