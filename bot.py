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
    client = await database.get_client(ctx.author)
    if client == None:
        await ctx.channel.send(lang.intro)
        database.create_user(ctx.author)
        return
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
    else:
        curseur = database.curseur().execute("""select id from clients where salle = "%s" """%(client.salle.id))
        liste = curseur.fetchall()
        for i in liste:
            print(i)
            await bot.get_user(i[0]).send("**%s** a dit : %s"%(ctx.author.name, ctx.content))

bot.run(token) 