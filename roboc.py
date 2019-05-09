# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import time
from carte import Carte

# On charge les cartes existantes


####################### VARIABLES #########################################
cartes = []

#######################  FONCTIONS ########################################

def myprint(mess):          #### fonction print avec sleep
    time.sleep(1)
    print(mess)


def init_score():                               # recherche d'anciens scores
    myprint("\nVoyons....")
    try:
        with open("data", "rb") as fichier:
            record = pickle.Unpickler(fichier)
            score = record.load()
    except:
        score = {}
        print("\nVous n'avez pas de partie en cours, alors bienvenue!")
    return score









####################### PROGRAMME ###########################################


for nom_fichier in os.listdir("cartes"):        ###### recherche de fichiers dans le dossier cartes
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter

myprint("\nBienvenu au jeu du labirynthe :")
name = input("\nQuel est votre nom? : ")        # récupération du nom d'utilisateur
name = name.lower()

score = init_score()

myprint(f"\nOk {name}, on va pouvoir commencer !")
myprint("\nVoici les cartes disponibles :")


for nom_fichier in os.listdir("cartes"):            # Présentation des cartes
    myprint(f"\n- Carte --> {nom_fichier[:-4]}: \n ")
    print(contenu)

choix = input("\nVeuillez choisir une carte : ")
choix = choix.lower()+".txt"

compilation = os.listdir("cartes")      # compilation est une liste des noms de cartes disponibles

if choix in compilation:                # vérification du choix dans la liste des cartes disponibles
    print("OK")
else:
    print("Pas dedans")

    