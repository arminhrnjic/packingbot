import discord

import json

with open('config.json') as json_file:
    data = json.load(json_file)
    TOKEN=data['token']

client=discord.Client()

prefix='?'


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author != client.user:
        print(message.author.id, message.author)
    
    if message.content.startswith(prefix+'pack'):
        await message.channel.send(str(message.author) + ' needs a pack @everyone')
        await message.add_reaction('\U0001F199')
        await message.add_reaction('\U00002705')
    if message.content.startswith(prefix+'help'):
        await message.channel.send("""Type ?pack *amount* on the #packing chanell to ask for a pack.
If someone asks for a pack, click :up: reaction to notify him 
that you posted pack on gm.""")

client.run(TOKEN)