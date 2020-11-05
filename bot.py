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
            print(nombre)
            print(client.salle.salles)
            if nombre < 0 or nombre >= len(client.salle.salles):
                await client.send(lang.salle_not_exists)
            else:
                old_salle = client.salle
                client.set_salle(client.salle.salles[nombre])
                await client.send(lang.patron.format(salle=client.salle))
                curseur = database.curseur().execute("""select id from clients where salle = "%s" """%(old_salle.id))
                liste = curseur.fetchall()
                for i in liste:
                    user = await bot.fetch_user(i[0])
                    try: await user.send("**%s** vient de partir vers *%s*"%(ctx.author.name, client.salle.nom_long))
                    except: pass
                curseur = database.curseur().execute("""select id from clients where salle = "%s" """%(client.salle.id))
                liste = curseur.fetchall()
                for i in liste:
                    user = await bot.fetch_user(i[0])
                    try: await user.send("**%s** vient d'arriver depuis *%s*"%(ctx.author.name, old_salle.nom_long))
                    except: pass
        except ValueError:
            await client.send(lang.give_number)
    else:
        curseur = database.curseur().execute("""select id from clients where salle = "%s" """%(client.salle.id))
        liste = curseur.fetchall()
        for i in liste:
            user = await bot.fetch_user(i[0])
            try: await user.send("**%s** a dit : %s"%(ctx.author.name, ctx.content))
            except: pass

bot.run(token) 