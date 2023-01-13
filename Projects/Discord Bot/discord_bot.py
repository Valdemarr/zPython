import discord
import os
import config

# Doing some stuff so that it diddles files from the same directory where this file is
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

intents = discord.Intents.default()
intents.message_content = True #This has to be checked off on https://discord.com/developers/applications/ - "Bot" tab

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    #await message.channel.send("Big momma's baaaaaack")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Writing result to file in directory - GOOD FOR LOGGING
    f2 = open(os.path.join(__location__, 'log.txt'), "a") #open and write to output file
    f2.write(f"{message.content}\n") #Write to output file
    f2.close()

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith("bruh"):
        await message.channel.send("https://www.youtube.com/watch?v=TKuLxJCArmg")

client.run(config.bot_token)
