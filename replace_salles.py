import os

#   é         è         ê         à         ù
#'["\u00e9", "\u00e8", "\u00ea", "\u00e0", "\u00f9"]'
REPLACE = [("Ã©", "\\u00e9"),("Ã¨", "\\u00e8"),("Ãª", "\\u00ea"),("Ã ", "\\u00e0"),("Ã¹", "\\u00f9"),
           ("Ã´", "\\u00f4")]

def modifier_salles(filename):
    lire_dossier(filename)

def modifier_fichier(filename):
    with open(filename,'r') as fichier:
        content = fichier.read()
    for replace in REPLACE:
        content = content.replace(*replace)
    with open(filename, 'w') as fichier:
        fichier.write(content)

def lire_dossier(filename):
    for file in os.listdir(filename):
        if os.path.isdir(filename+"/"+file):
            lire_dossier(filename+"/"+file)
        elif os.path.isfile(filename+"/"+file) and file.endswith(".json"):
            modifier_fichier(filename+"/"+file)

if __name__ == "__main__":
    print("Modification...")
    modifier_salles("salles")
    print("Terminé !")