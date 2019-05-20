"""Ce module contient la classe Labyrinthe."""


labyrinthe = []
ligne = []


class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, chaine):
        self.chaine = chaine
        content = self.chaine.split("\n")
                                        #création de l'imbrication de liste
        for x in content:
            ligne.append(list(x))
        for e in ligne:
            labyrinthe.append(e)

      
    def __repr__(self):                 # m"thode pour afficher le labyrinthe en cours
        return f"\n{self.chaine}"



    def deplacement(self):
                                                      # indexation des éléments dans les listes 
                                                    
        robot = []
        mur = []
        porte = []
        
        for index_x, x in enumerate(labyrinthe):
            for index_y, y in enumerate(x):
                if y == "X":
                    robot = (index_x, index_y)
                if y == "O":
                    mur = (index_x, index_y)
                if y == ".":
                    porte = (index_x, index_y)

        print(robot)                            # retourne la position de robot
 








