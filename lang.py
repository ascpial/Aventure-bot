intro="""Bonjour !
Tu vas pouvoir commencer à RP !
Avant de commencer, voici les commandes :
```
  regarder       : voir où tu es
  aller <nombre> : aller dans une pièce```
Il y a aussi un tchat entre les joueurs, tu peux leurs parler normalement s'ils sont le même lieu que toi.
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
embed_description = "Vous êtes dans {}.\n{}"
field_description = "%i : %s"
partir = "**%s** vient de partir vers *%s*"
arriver = "**%s** vient d'arriver depuis *%s*"
dit = "**%s** a dit : %s"
connectes = "Joueurs dans cet endroit :"
statut = ["statut ", "je fait "]
statut_reset = ["reset_statut", "statut"]
connectes_statut = "%s : %s"