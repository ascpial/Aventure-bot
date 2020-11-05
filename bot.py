import discord
import lang
import os
from my_token import token
from utils import *
from database import *

bot = discord.Client()

database = Database("base.db", bot)

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_message(ctx):
    if not type(ctx.channel) == discord.DMChannel:
        return
    if ctx.author == bot.user: return
    client = await database.get_client(ctx.author.id)
    if client == None:
        await ctx.channel.send(lang.intro)
        print("Pas registré !")
    elif ctx.content.lower() in lang.regarder:
        await ctx.channel.send(lang.patron.format(salle=client.salle))
    elif startswith(ctx.content.lower(), lang.aller):
        try:
            nombre = int(ctx.content[6:])
            if not nombre >= 0 and nombre < len(client.salle.salles):
                await client.send(lang.salle_not_exists)
            else:
                client.set_salle(client.salle.salles[nombre])
                await client.send(lang.patron.format(salle=client.salle))
        except ValueError:
            await client.send(lang.give_number)

bot.run(token) 