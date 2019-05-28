import os
import time
from carte import *

####################### VARIABLES #########################################
grille = []
murs = []
portes = []
#######################  FONCTIONS ########################################


class Robot:
    """
    Classe définissant le robot et ses déplacements dans la carte. L'initialistation permet de récupérer les position
    de tous les éléments de la carte
    """
    def __init__(self, chaine ):
        self.chaine = chaine
        self.robot = []
        self.obstacles = []
        self.portes = []
        self.sortie = []
        for index_x, x in enumerate(self.chaine):
            for index_y, y in enumerate(x):
                if y == "X":
                    self.robot = [index_x, index_y]        # récupération de la position de robot dans une liste
                elif y == "U":
                    self.sortie = [index_x, index_y]     # récupération de la position de la sortie dans une liste
                elif y == ".":
                    self.porte = [index_x, index_y]      # récupération de la position des portes dans une liste
                    self.portes.append(self.porte)
                elif y == "O":                      # récupération de la position des murs dans une liste
                    mur = [index_x, index_y]
                    self.obstacles.append(mur)   
                else:
                    pass
                   

    def __repr__(self):
        self.mapp = ""
        for i in self.chaine:
            self.mapp += '\n'
            for x in i:
                self.mapp += x
        return f"{self.mapp}"

    def deplacer(self, direction):
        entries = ["N", "S", "E", "O"]

        if direction not in entries:
            print("Direction inconnue")
        else:
            print("direction OK")