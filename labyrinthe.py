"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}
        self.obstacles = obstacles
    
    #def __repr__(self, robot, obstacles):
        #fonction à compléter pour l'affichage de la carte