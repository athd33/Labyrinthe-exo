"""
Code principal du jeu
"""

import os
import time
from carte import Carte
from labyrinthe import Labyrinthe

####################### VARIABLES #########################################
cartes = []
entries = ["N", "S", "E", "O", "Q", "HELP", "ROBOT"]
game = True
labyrinthe = False

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
                cartes.append(carte)                # remplissage de la liste carte avec les objets carte instanciés

                                                    # On affiche les cartes existantes
myprint("Voici les labyrinthes disponibles, lequel choisissez vous?  :")
for content, carte in enumerate(cartes):
    print(f"  {content+1} - {carte.nom}")


while labyrinthe == False:                          # choix du labyrinthe
    choice = input("Quel parcours choisissez vous? : ")
    choice = choice.upper()
    try:
        choice = int(choice)
    except:
        ValueError('Erreur de format de choix')
        continue
    else:            
        if choice < 1 or choice > len(cartes):
            print("Pardon?")
            continue       
        else:  
            carte = cartes[choice -1]
            content = str(carte)                      # conversion de carte en str pour la passer dans la classe Labyrinthe
            labyrinthe_Online = Labyrinthe(content)    # création de l'objet carte_choisie de classe Labyrinthe
    break

print(labyrinthe_Online)




while game:  
    entry = input(" --|> ")
    entry = entry.upper() # passe en majuscule les entrées
    if entry not in entries:
        print("Commande introuvable, tapez 'help' pour obtenir de l'aide")
    else:
        labyrinthe_Online.deplacer(entry) # la méthode deplacer de la classe labyrinthe gere les entrees pour les déplacements
        os.system("clear")
        print(labyrinthe_Online)

