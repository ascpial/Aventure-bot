class Piece(object):
    def __init__(self, id, nom, nom_long, description, apercu, salles, image_url=None):
        self.id = id
        self.nom = nom
        self.nom_long = nom_long
        self.description = description
        self.apercu = apercu
        self.salles = salles
        self.image_url = image_url
    def __repr__(self):
        return self.nom
    def start(self):
        liste = []
        for nom in self.salles:
            liste.append(monde[nom])
        self.salles = liste

class Couloir(Piece):
    nom = "Couloir"
    nom_long = "le couloir"
    def __init__(self, id, description, apercu, information, salles, image_url=None):
        self.id = id
        self.description = description
        self.apercu = apercu
        self.information = information
        self.salles = salles
        self.image_url=image_url
    def __repr__(self):
        return self.nom + " " + self.information

monde = {"balcon":Piece("balcon","Balcon", "le balcon", "Le balcon surplombait la compagne. En bois, assez robuste mais aussi grossier, il s'agit du genre de balcon qui inspire confiance. Malgrès ses barrières mal ajustées, tu te sens en sécuritée même avec plusieurs dizaines de mètres de dénivelé en dessous de toi.",
                        "Le balcon a l'air rassurant, assez solide.", ["hall"], "https://cdn.discordapp.com/attachments/773592639734808657/773606887811579955/2020-11-04_18.57.16.png")}
monde["hall"]=Piece("hall", "Hall", "le hall d'entrée", """Le hall d'entrée a trois porte : une pour aller sur le balcon, deux autres pour aller dans deux couloirs. Cette pièce, de taille modeste, donne sur le balcon, fait étonnant puisqu'il s'agit en général de la pièce qui donne sur le porche...""",
                     "Le hall d'entrée, placé bizarement après le balcon, donne sur deux autres portes.", ["balcon", "couloir_ss", "couloir_chambres"], "https://cdn.discordapp.com/attachments/773592639734808657/773607184876568617/2020-11-04_18.58.32.png")
monde["couloir_ss"] = Couloir("couloir_ss", "C'est un couloir étroit et court qui mène vers une échelle descendant en dessous de la maison. Il donne aussi sur le hall.",
                              "Le couloir mène sur une échelle qui descend et au hall.",
                              "du sous sol", ["hall", "cave"])
monde["couloir_chambres"] = Couloir("couloir_chambres", "Le cloir, relativement long, donne au fond sur deux portes. Il donne aussi sur le hall.",
                                     "Le couloir donne sur deux portes et sur le hall.",
                                     "des chambres",
                                     ["hall", "cuisine", "chambre"])
monde["cave"] = Piece("cave", "Cave", "la cave", "La cave est très sombre. Vous distinguez tout de même qu'elle est très petite et plutôt sec, avec des tonneaux au sol.",
                      "La petite cave est très sombre et plutôt sèche.", ["couloir_ss"], "https://cdn.discordapp.com/attachments/773592639734808657/773607002349240340/2020-11-04_18.57.49.png")
monde["cuisine"] = Piece("cuisine", "Cuisine", "la cuisine", "Enfin cuisine, parlons en : il s'agit d'une marmite dans une cheminée. Il n'y a même pas de nourriture...",
                         "La cuisine se résume à une marmite dans une cheminée...", ["couloir_chambres"], "https://cdn.discordapp.com/attachments/773592639734808657/773607521969635328/2020-11-04_18.59.45.png")
monde["chambre"] = Piece("chambre", "Chambre", "la chambre", "La chambre, avec un lit aux draps bruns et une lanterne sur la table de chevet contient un coffre. IL doit s'agir de la pièce la plus lumineuse de la maison, car la lanterne éclaire beacoups.",
                         "La chambre contient un lit en un coffre.", ["couloir_chambres"], "https://cdn.discordapp.com/attachments/773592639734808657/773607622254395463/2020-11-04_19.00.17.png")

for piece in monde.values():
    piece.start()