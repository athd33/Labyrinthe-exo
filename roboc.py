import os
import time
from carte import *

class Robot:
    """
    Classe définissant le robot et ses déplacements dans la carte. L'initialistation permet de récupérer les position
    de tous les éléments de la carte
    """
    def __init__(self, chaine ):
        self.chaine = chaine

      
                   

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
                print(self.robot)            
        elif direction == "S":
                print(self.robot)         
        elif direction == "E":
                print(self.robot)         
        elif direction == "O":
                print(self.robot)         
        return self.mapp