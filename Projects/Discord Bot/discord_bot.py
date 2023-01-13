import discord
import os

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
    f2 = open(os.path.join(__location__, 'log.txt'), "w") #open and write to output file
    f2.write(f"\n{message.content}") #Write to output file
    f2.close()

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith("bruh"):
        await message.channel.send("https://www.youtube.com/watch?v=TKuLxJCArmg")

client.run('NTc1MTE3NjA4ODgyNTM2NDk4.GxzB6S.MmEFcM6tU_0vQTEN4pxGVVVoE-4yQ9CsLt5gHM')
