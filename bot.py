from gestionnaire import monde
import discord
import lang
import os

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
    clients.append(Client(user))

bot = discord.Client()

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_message(ctx):
    if not type(ctx.channel) == discord.DMChannel:
        return
    if ctx.content.lower() == "bonjour":
        await ctx.channel.send("Bonjour !\nJe vais commencer à te conter ton RP...\nVoici les commandes :\n  regarder pour voir où tu es\n  aller <nombre> pour aller dans une pièce")
    elif ctx.content.lower() == "regarder":
        client = get_client(ctx.author)
        await ctx.channel.send(lang.patron.format(salle=client.salle))
    elif ctx.content.lower().startswith("aller "):
        client = get_client(ctx.author)
        try:
            nombre = int(ctx.content[6:])
            if not nombre >= 0 and nombre < len(client.salle.salles):
                await ctx.channel.send("Tu ne peux pas aller dans cette salle, elle n'existe pas !")
            else:
                client.salle = client.salle.salles[nombre]
                await ctx.channel.send(lang.patron.format(salle=client.salle))
        except ValueError:
            await ctx.channel.send("Il faut donner un nombre !")

bot.run(os.getenv("token"))    