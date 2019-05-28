import os
import time
from carte import *

####################### VARIABLES #########################################
grille = []
murs = []
portes = []
index_x = 0
index_y = 0
#######################  FONCTIONS ########################################


class Robot:
    """
    Classe définissant le robot et ses déplacements dans la carte. L'initialistation permet de récupérer les position
    de tous les éléments de la carte
    """
    def __init__(self, chaine ):
        self.chaine = chaine
        self.robot = []
        obstacles = []
        portes = []
        self.sortie = []
        self.grille = []
        
        for index_x, x in enumerate(self.chaine):
            for index_y, y in enumerate(x):
                if y == "X":
                    self.robot = [index_x, index_y]        # récupération de la position de robot dans une liste
                    self.grille += "X"
                elif y == "U":
                    self.sortie = [index_x, index_y]     # récupération de la position de la sortie dans une liste
                elif y == ".":
                    porte = [index_x, index_y]      # récupération de la position des portes dans une liste
                    portes.append(porte)
                elif y == "O":                      # récupération de la position des murs dans une liste
                    mur = [index_x, index_y]
                    obstacles.append(mur)   
                else:
                    pass
                   

    def __repr__(self):   # méthode d'affichage de la carte
        self.mapp = ""
        for i in self.chaine:
            self.mapp += '\n'
            for x in i:
                self.mapp += x
        return f"{self.mapp}"

        

    def deplacer(self, direction):   # méthode pour les déplacements du robot
        entries = ["N", "S", "E", "O"]

        if direction not in entries:
            print("Direction inconnue")
        elif direction == "N":
                self.robot[index_y] -= 1    
                print(self.robot)            
        elif direction == "S":
                self.robot[index_y] += 1
                print(self.robot)         
        elif direction == "E":
                self.robot[index_x] += 1
                print(self.robot)         
        elif direction == "O":
                self.robot[index_x] -= 1
                print(self.robot)         
        return self.mapp