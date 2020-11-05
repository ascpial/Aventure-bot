class Piece(object):
    def __init__(self, nom, nom_long, description, apercu, salles):
        self.nom = nom
        self.nom_long = nom_long
        self.description = description
        self.apercu = apercu
        self.salles = salles
    def __repr__(self):
        return self.nom
    def start(self):
        self.salles_str = ""
        for numero, salle in enumerate(self.salles):
            self.salles_str += str(numero)+" : "+salle.nom+"\n"
        self.salles_str = self.salles_str[:-1]

class Couloir(Piece):
    nom = "Couloir"
    nom_long = "le couloir"
    def __init__(self, description, apercu, information, salles):
        self.description = description
        self.apercu = apercu
        self.information = information
        self.salles = salles
    def __repr__(self):
        return self.nom + " " + self.information

monde = {"balcon":Piece("Balcon", "le balcon", "Le balcon surplombait la comapagne. En bois, assez robuste mais aussi grossier, il s'agit du genre de balcon qui inspire confiance. Malgrès ses barrières mal ajustées, on se sent en sécuritée même avec plusieurs dizaines de mètres de dénivelé en dessous de nous.",
                        "Le balcon a l'air rassurant, assez solide.", [])}
monde["hall"]=Piece("Hall", "le hall d'entrée", """Le hall d'entrée avait trois porte : une pour aller sur le balcon, deux autres pour aller dans deux couloirs. Cette pièce, de taille modeste, donne sur le balcon, fait étonnant puisqu'il s'agit en général de la pièce qui donne sur le porche...""",
                     "Le hall d'entrée, placé bizarement après le balcon, donne sur deuwsutre portes.", [monde["balcon"]])
monde["couloir_ss"] = Couloir("C'est un couloir étroit et court qui mène vers une échelle descendant en dessous de la maison. Il donne aussi sur le hall.",
                              "Le couloir mène sur une échelle qui descend et au hall.",
                              "du sous sol",
                              [monde["hall"]])
monde["couloir_chambres"] = Couloir("Le cloir, relativement long, donne au fond sur deux portes. Il donne aussi sur le hall.",
                                     "Le couloir donne sur deux portes et sur le hall.",
                                     "des chambres",
                                     [monde["hall"]])
monde["cave"] = Piece("Cave", "la cave", "La cave est très sombre. Vous distinguez tout de même qu'elle est très petite et plutôt sec, avec des tonneaux au sol.",
                      "La petite cave est très sombre et plutôt sèche.", [monde["couloir_ss"]])
monde["cuisine"] = Piece("Cuisine", "la cuisine", "Enfin cuisine, parlons en : il s'agit d'une marmite dans une cheminée. Il n'y a même pas de nourriture...",
                         "La cuisine se résume à une marmite dans une cheminée...", [monde["couloir_chambres"]])
monde["chambre"] = Piece("Chambre", "la chambre", "La chambre, avec un lit aux draps bruns et une lanterne sur la table de chevet contient un coffre. IL doit s'agir de la pièce la plus lumineuse de la maison, car la lanterne éclaire beacoups.",
                         "La chambre contient un lit en un coffre.", [monde["couloir_chambres"]])
monde["balcon"].salles.append(monde["hall"])
monde["hall"].salles.append(monde["couloir_ss"])
monde["hall"].salles.append(monde["couloir_chambres"])
monde["couloir_ss"].salles.append(monde["cave"])
monde["couloir_chambres"].salles.append(monde["cuisine"])
monde["couloir_chambres"].salles.append(monde["chambre"])

for piece in monde.values():
    piece.start()