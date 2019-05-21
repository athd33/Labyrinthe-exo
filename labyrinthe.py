"""Ce module contient la classe Labyrinthe."""


ligne = []

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, chaine):
        self.chaine = chaine
        self.content = self.chaine.split("\n")
        self.grille = []

        for lignes in self.content:     # création de la grille pour récupérer les coordonnées
            ligne.append(list(lignes))
        for letter in ligne:
            self.grille.append(letter)

    def __repr__(self):                 # méthode qui affiche la carte sous forme de grille (comment remettre en liste...?)
        return f"{self.grille}"


    def position(self, element):
        """
        Méthode pour récupérer les position d'un élément
        """
        self.element = element
        if element ==  "X":
            for index_x, x in enumerate(self.grille):
                for index_y, y in enumerate(x):         # parcours des éléments et indexation du robot et de la sortie
                    if y == "X":
                        robot = (index_x, index_y)
                        position  = robot
        if element == "U":
            for index_x, x in enumerate(self.grille):
                for index_y, y in enumerate(x):         # parcours des éléments et indexation du robot et de la sortie
                    if y == "U":
                        robot = (index_x, index_y)
                        position = robot

        
        return f"position : {position}"





