"""
Code principal du jeu
"""

import os
import time
from carte import Carte

####################### VARIABLES #########################################
cartes = []

#######################  FONCTIONS ########################################

def myprint(mess):                              # fonction print avec sleep
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


myprint("###########  JEU DU LABYRINTHE #################\n")

for nom_fichier in os.listdir("cartes"):        # recherche de fichiers dans le dossier cartes
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            try:
                carte = Carte(nom_carte, contenu)   # instanciation des cartes de classe Carte
            except:
                print("Erreur de lecture de carte")
            else:
                cartes.append(carte)        # remplissage de la liste carte avec les objets carte instanciés

# On affiche les cartes existantes
myprint("Voici les labyrinthes disponibles, lequel choisissez vous?  :")
for content, carte in enumerate(cartes):
    print(f"  {content+1} - {carte.nom}")


labyrinthe = False                  # choix du labyrinthe
while labyrinthe == False:
    choice = input("Quel parcours choisissez vous? : ")
    try:
        choice = int(choice)
    except:
        ValueError('Erreur de format de choix')
    else:
        if choice < 1 or choice > len(cartes):
            print("Pardon?")
            continue
        carte = cartes[choice -1]
        print(f"carte choisie {carte}\n")
    break

game = True
while game:
    entry = input(" --|> ")
    if entry == "q":
        print("Fin de partie, au revoir")
        game = False
    if entry == "help":
        with open("README.md", "r") as fichier:
            content = fichier.read()
            myprint(f"\n{content}")
    
    


