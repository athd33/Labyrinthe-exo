import os
import time
from carte import *

class Robot:
    """
    Classe définissant le robot et ses déplacements dans la carte. L'initialistation permet de récupérer les position
    de tous les éléments de la carte
    """
    def __init__(self, labyrinthe_Online ):     #classe instanciée avec la classe carte en paramètre
        self.labyrinthe_Online = labyrinthe_Online


    def __repr__(self):
        """
        Méthode d'affichage de la carte
        """    
        self.grilleToList = []
        grille = self.grille

        for i in grille:   # pour tous les elements de self.grille
            self.grilleToList.append(''.join(i)) # remplissage de mappToDisplay avec les elements sans espace    
        self.mappToDisplay = "\n".join(self.grilleToList)
        return f"{self.mappToDisplay}"



    def deplacer(self, direction):   # méthode pour les déplacements du robot
        entries = ["N", "S", "E", "O"]
        robot = self.labyrinthe_Online.robot
        self.grille = self.labyrinthe_Online.grille
        mapp = self.labyrinthe_Online.mappToDisplay
        Rx = robot[0]
        Ry = robot[1]

        if direction == "N":
            if self.grille[Rx][Ry -1] == "O":
                print("mur")
            else:
                robot[1] -= 1
                self.grille[Rx][Ry] = "X"
                self.grille[Rx][Ry +1] = " " 
