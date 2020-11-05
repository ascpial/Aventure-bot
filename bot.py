from gestionnaire import monde
import discord
import lang
import os
from my_token import token

class Client(object):
    def __init__(self, user):
        self.user_id = user.id
        self.salle = monde["balcon"]

clients = []

def get_client(user):
    id = user.id
    for i in clients:
        if i.user_id == id:
            return i
    return None

bot = discord.Client()

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_message(ctx):
    if not type(ctx.channel) == discord.DMChannel:
        return
    client = get_client(ctx.author)
    if client == None:
        await ctx.channel.send(lang.intro)
        clients.append(Client(ctx.author))
    elif ctx.content.lower() in lang.regarder:
        client = get_client(ctx.author)
        await ctx.channel.send(lang.patron.format(salle=client.salle))
    elif ctx.content.lower().startswith("aller "):
        try:
            nombre = int(ctx.content[6:])
            if not nombre >= 0 and nombre < len(client.salle.salles):
                await ctx.channel.send(lang.salle_not_exists)
            else:
                client.salle = client.salle.salles[nombre]
                await ctx.channel.send(lang.patron.format(salle=client.salle))
        except ValueError:
            await ctx.channel.send(lang.give_number)

bot.run(TOKEN)    