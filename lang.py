intro="""Bonjour !
Je vais commencer à te conter ton RP...
Voici les commandes :
```
  regarder       : voir où tu es
  aller <nombre> : aller dans une pièce```
"""
patron = """```
Tu es dans {salle.nom_long} ({salle.nom}).
{salle.apercu}
Tu peux aller dans :
{salle.salles_str}
```
"""
give_number = "Il faut donner un nombre !"
salle_not_exists = "Tu ne peux pas aller dans cette salle, elle n'existe pas !"

regarder = ["regarder", "voir"]
aller = ["aller ", "bouge ", "déplacer "]
embed_description = "Vous êtes dans {}."
field_description = "%i : %s"
partir = "**%s** vient de partir vers *%s*"
arriver = "**%s** vient d'arriver depuis *%s*"
dit = "**%s** a dit : %s"