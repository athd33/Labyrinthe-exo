# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import time
from carte import Carte

# On charge les cartes existantes
cartes = []


def myprint(mess):
    time.sleep(1)
    print(mess)




for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter


myprint("Bienvenu au jeu du labirynthe :")
myprint("\nVoici les cartes disponibles :")

# On affiche les cartes existantes
for nom_fichier in os.listdir("cartes"):
    myprint(f"\n- Carte --> {nom_fichier[:-4]}: \n ")
    print(contenu)

choix = input("\nVeuillez choisir une carte : ")


# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
