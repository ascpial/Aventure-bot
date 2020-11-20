import json
import os

#   é         è         ê         à         ù
#'["\u00e9", "\u00e8", "\u00ea", "\u00e0", "\u00f9"]'

def get(object, indice):
    try:
        return object[indice]
    except KeyError:
        return None

class Salles(object):
    def __init__(self):
        self.liste = []
    def append(self, objet):
        self.liste.append(objet)
    def __getitem__(self, id):
        for salle in self.liste:
            if salle.id == id:
                return salle
        raise KeyError
    def __iter__(self):
        return iter(self.liste)
    def create(self):
        for salle in self.liste:
            salle.create(self)

class Salle(object):
    def __init__(self, filename):
        infos = json.loads(open(filename, 'r').read())
        self.id = filename
        self.nom = get(infos, "nom")
        self.nom_long = get(infos, "dnom")
        self.description = get(infos, "description")
        self.apercu = get(infos, "pdescription")
        self.image_url = get(infos, "image")
        self.salles = get(infos, "salles")
        self.ready = False
    def __repr__(self):
        return self.nom
    def create(self, liste):
        salles = []
        for salle in self.salles:
            salles.append(liste[salle])
        self.salles = salles
        self.ready = True

def creer_salles(filename,liste):
    lire_dossier(filename, liste)

def lire_fichier(filename, liste):
    liste.append(Salle(filename))

def lire_dossier(filename, liste):
    for file in os.listdir(filename):
        if os.path.isdir(filename+"/"+file):
            lire_dossier(filename+"/"+file, liste)
        elif os.path.isfile(filename+"/"+file) and file.endswith(".json"):
            lire_fichier(filename+"/"+file, liste)