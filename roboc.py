import os
import time
from carte import *

####################### VARIABLES #########################################
entries = ["N", "S", "E", "O"]
grille = []
robot = []

#######################  FONCTIONS ########################################


class Robot:
    """
    Classe définissant le robot et ses déplacements dans la carte
    """
    def __init__(self, chaine ):
        self.chaine = chaine
     
            

    def __repr__(self):
        self.mapp = ""
        for i in self.chaine:
            self.mapp += '\n'
            for x in i:
                self.mapp += x
        return f"{self.mapp}"