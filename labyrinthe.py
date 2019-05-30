
import os
from carte import *
from fonctions import *
from roboc import *
############ VARIABLES ###################
game = True
choice = False
general_commands = ["Q", "HELP"]

############ PROGRAMME PRINCIPAL #################


print("Début du jeu")

instance_map()

choose_map()

while choice != True:
    entry = input("> ")
    entry = entry.upper()
    
    if entry == "Q":
        print("Fin de jeu, au revoir")
        exit(0)
    elif entry == "HELP":
        with open("README.md", "r") as doc:
            content = doc.read()
            print(content)
    else:
        entry = int(entry)
        if entry < 1 or entry > len(cartes):
            print("Choix invalide")
        else:
            carte = cartes[entry -1]
            content = str(carte)                      # conversion de carte en str pour la passer dans la classe Labyrinthe
            labyrinthe_Online = Carte_Online(content)    # création de l'objet carte_choisie de classe Labyrinthe
            choice = True


player = Robot(labyrinthe_Online) # instanciation de player, objet de classe Robot avec la liste de chaines en parametre

print(labyrinthe_Online)
    
while game:                     # commandes en jeu
    entry_lower = input(">")
    entry = entry_lower.upper()
    print(entry)
    if entry == "Q":
        print("Fin de partie")
        exit(0)
    
    elif entry == "HELP":
        with open("README.md", "r") as doc:
            content = doc.read()
            print(content)
    else:
        print(player.deplacer(entry)) # utilisation de la méthode deplacer de la classe Robot instanciée avec player
        print(player)