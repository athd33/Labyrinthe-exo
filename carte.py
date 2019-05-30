
"""Ce module contient les classes relatives aux Cartes du jeu ainsi que leurs affichages."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.chaine = chaine

    def __repr__(self):
        return f"{self.chaine}\n"
            

class Carte_Online:
    """
    Objet définissant la carte à afficher en cours de partie
    """
    def __init__(self, chaine):
        self.chaine = chaine
        self.lignes = self.chaine.split("\n")
        self.grille = []                # chaine destructuree , chaque element est disponible
        self.obstacles = []
        self.sortie = []

        for ligne in self.lignes:   # boucle permettant de destructurer
            self.grille.append([c for c in ligne])

        for index_x, x in enumerate(self.lignes):           # indexation des éléments de la carte
                    for index_y, y in enumerate(x):
                        if y == "X":
                            self.robot = [index_x, index_y]        # récupération de la position de robot dans une liste
                        elif y == "U":
                            self.sortie = [index_x, index_y]     # récupération de la position de la sortie dans une liste
                        elif y == ".":
                            self.porte = [index_x, index_y]      # récupération de la position des portes dans une liste
                        elif y == "O":                      # récupération de la position des murs dans une liste
                            self.mur = [index_x, index_y]
                            self.obstacles.append(self.mur)   
                        else:
                            pass

    def __repr__(self):
        """
        Méthode d'affichage de la carte
        """    
        self.grilleToList = []

        for i in self.grille:   # pour tous les elements de self.grille
            self.grilleToList.append(''.join(i)) # remplissage de mappToDisplay avec les elements sans espace
    
        self.mappToDisplay = "\n".join(self.grilleToList)

        return self.mappToDisplay