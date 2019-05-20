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

                                        # indexation des éléments dans les listes
        for index_x, x in enumerate(labyrinthe):
            for index_y, y in enumerate(x):
                if y == "X":
                    robot = (index_x, index_y)

    def __repr__(self):

        return f"\n{self.chaine}"
 








