"""Ce module contient la classe Labyrinthe."""


ligne = []

class Labyrinthe:

    """Classe représentant un labyrinthe."""
    
    def __init__(self, chaine):
        self.chaine = chaine
        self.content = self.chaine.split("\n")
        self.grille = []
        self.mapp = ""
        

        for lignes in self.content:     # création de la grille pour récupérer les coordonnées
            ligne.append(list(lignes))
        for letter in ligne:
            self.grille.append(letter)

    def __repr__(self):                 # méthode qui affiche la carte sous forme de grille 
        """
        Méthode qui créé la carte a afficher 
        """
        for i in self.grille:
            self.mapp += '\n'
            for x in i:
                self.mapp += x
        return f"{self.mapp}"


    def deplacer(self, direction):      # méthode permettant de gérer les déplacements
        """
        Méthode qui procède au déplacement du robot
        """
       
        self.direction = direction
        obstacles = []                      # contient la liste des positions des murs "O"
        portes = []                         # contient la liste des portes 
        #recuperation des positions
        for index_x, x in enumerate(self.grille):
            for index_y, y in enumerate(x):         # parcours des éléments et indexation du robot et de la sortie
                if y == "X":
                    robot = (index_x, index_y)      # récupération de la position de robot dans un tuple
                elif y == "U":
                    sortie = (index_x, index_y)     # récupération de la position de la sortie dans un tuple
                elif y == ".":
                    porte = (index_x, index_y)      # récupération de la position des portes dans une liste
                    portes.append(porte)
                elif y == "O":                      # récupération de la position des murs dans une liste
                    mur = (index_x, index_y)
                    obstacles.append(mur)   
                else:
                    pass


        if self.direction == "N":
            print(robot)
            print("DIRECTION NORD")
            robotliste = list(robot)    # conversion de la position du robot de tuple à liste
            robotliste[0] = robot[0] -1 # modification de la valeur de robot en liste
            robot = tuple(robotliste)   # reconversion de robot en tuple pour vérif avec if in
            print(robot)
            return robot

        elif self.direction == "S":
            print("DIRECTION SUD")

        elif self.direction == "S":
            print("DIRECTION SUD")

        elif self.direction == "E":
            print("DIRECTION EST")


        elif self.direction == "O":
            print("DIRECTION OUEST")

        elif self.direction == "Q":
            print("Fin de partie, au revoir")
            exit(0)

        elif self.direction == "HELP":
            with open("README.md", "r") as fichier:
                content = fichier.read()
                print(content)





