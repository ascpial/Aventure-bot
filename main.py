import discord
import lang
import os
from configuration import TOKEN
from utils import *
from database import Database
import salles_gestionnaire

import logging
import logging.config
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(levelname)s - %(name)s - %(asctime)s - %(message)s')

bot = discord.Client()

database = Database("/var/database/aventure.db", bot)

@bot.event
async def on_ready():
    print("ready")
    await bot.change_presence(activity=discord.Game(name="Envois moi un MP"))

@bot.event
async def on_message(ctx):
    if not type(ctx.channel) == discord.DMChannel:
        return
    if ctx.author == bot.user: return
    client = await database.get_client(ctx.author)
    if client == None:
        await ctx.channel.send(lang.intro)
        database.create_user(ctx.author)
        logging.info(f"User id {ctx.author.id} join")
        return
    elif ctx.content.lower().strip() in lang.regarder:
        embed = await get_embed(client)
        await ctx.channel.send(embed = embed)
        logging.info(f"User Id {client.user_id} seen in {client.salle.id}")
    elif startswith(ctx.content.lower().strip(), lang.aller):
        try:
            nombre = int(del_commande(ctx.content, lang.aller))
            if nombre < 0 or nombre >= len(client.salle.salles):
                await client.send(lang.salle_not_exists)
            else:
                old_salle = client.salle
                client.set_salle(client.salle.salles[nombre])
                logging.info(f"User Id {client.user_id} moved from {old_salle.id} to {client.salle.id}")
                embed = await get_embed(client)
                await client.send(embed=embed)
                async for i in joueurs_in(old_salle, database):
                    try: await i.send(lang.partir%(ctx.author.name, client.salle.nom_long))
                    except: pass
                async for i in joueurs_in(client.salle, database):
                    try: await i.send(lang.arriver%(ctx.author.name, old_salle.nom_long))
                    except: pass
        except ValueError:
            await client.send(lang.give_number)
    elif startswith(ctx.content, lang.statut):
        statut = del_commande(ctx.content, lang.statut)
        client.set_statut(statut)
    elif ctx.content in lang.statut_reset:
        client.set_statut("")
    elif ctx.content == "reload" and ctx.author.id == 638313144241881093:
        monde_reload = salles_gestionnaire.Salles()
        salles_gestionnaire.creer_salles("salles", monde_reload)
        monde_reload.create()
        database.monde = monde_reload
    else:
        async for user in joueurs_in(client.salle, database):
            try: await user.send(lang.dit%(ctx.author.name, ctx.content))
            except: pass
        logging.info(f"User Id {client.user_id} send \"{ctx.content}\" in {client.salle.id}")

bot.run(TOKEN)