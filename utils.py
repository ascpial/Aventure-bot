import lang
import discord

def startswith(string, liste):
    for i in liste:
        if string.startswith(i): return True
    return False
def del_commande(string, liste):
    for i in liste:
        if string.startswith(i):
            string = string[len(i):]
            return string
def get_embed(client):
    salle = client.salle
    embed = discord.Embed(title=salle.nom, description=lang.embed_description.format(salle.nom_long))
    if salle.image_url != None: embed.set_image(url=salle.image_url)
    for i, salle_ in enumerate(client.salle.salles):
        embed.add_field(name=lang.field_description%(i, salle_.nom), value=salle_.apercu)
    return embed