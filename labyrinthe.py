"""Ce module contient la classe Labyrinthe."""


ligne = []
entries = ["N", "S", "E", "O", "Q", "HELP"]

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
      
        if self.direction ==  "":          # TEST : pour récupérer la position du robot
            for index_x, x in enumerate(self.grille):
                for index_y, y in enumerate(x):         # parcours des éléments et indexation du robot et de la sortie
                    if y == "X":
                        robot = (index_x, index_y)
                        print(robot)
                        #print(mapp)    a voir pour ajout ici..
        if self.direction == "U":
            for index_x, x in enumerate(self.grille):
                for index_y, y in enumerate(x):         # parcours des éléments et indexation du robot et de la sortie
                    if y == "U":
                        robot = (index_x, index_y)

        if self.direction == "N":
            print("DIRECTION NORD")

        elif self.direction == "S":
            print(robot)
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

        return {self.mapp}




