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
async def get_embed(client):
    salle = client.salle
    embed = discord.Embed(title=salle.nom, description=lang.embed_description.format(salle.nom_long, salle.description))
    if salle.image_url != None: embed.set_image(url=salle.image_url)
    for i, salle_ in enumerate(client.salle.salles):
        embed.add_field(name=lang.field_description%(i, salle_.nom), value=salle_.apercu)
    curseur = client.database.curseur().execute("""select name, statut from clients where salle="%s" """%(client.salle.id))
    liste = curseur.fetchall()
    connectes = []
    for i in liste:
        if i[1] != "":
            connectes.append(lang.connectes_statut%(i[0], i[1]))
        else:
            connectes.append(i[0])
    embed.add_field(name=lang.connectes, value='\n'.join(connectes))
    return embed