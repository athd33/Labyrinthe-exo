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
    
            robotliste = list(robot)    # conversion de la position du robot de tuple à liste
            r0 = robotliste[0]-1
            r1 = robotliste[1]
            econtrol = self.grille[r0][r1]                  #variable qui va servir au controle de la valeur de la future position    

            if econtrol == 'U':
                print("SORTIE")


            if econtrol != "O":                                             # vérification de la position suivante
                self.grille[robotliste[0]][robotliste[1]] = " "             # réafectation de valeur sur la position de robot (libère la position)
                robotliste[0] = robot[0] -1                                 # modification de la valeur de robot en liste
                robot = tuple(robotliste)                                   # reconversion de robot en tuple pour vérif avec if in
                self.grille[robotliste[0]][robotliste[1]] = "X"             # nouvelle position du robot


        elif self.direction == "S":
            robotliste = list(robot)    # conversion de la position du robot de tuple à liste
            r0 = robotliste[0]+1
            r1 = robotliste[1]
            econtrol = self.grille[r0][r1]                  #variable qui va servir au controle de la valeur de la future position    

            if econtrol == 'U':
                print("SORTIE")


            if econtrol != "O":                                             # vérification de la position suivante
                self.grille[robotliste[0]][robotliste[1]] = " "             # réafectation de valeur sur la position de robot (libère la position)
                robotliste[0] = robot[0] +1                                 # modification de la valeur de robot en liste
                robot = tuple(robotliste)                                   # reconversion de robot en tuple pour vérif avec if in
                self.grille[robotliste[0]][robotliste[1]] = "X"             # nouvelle position du robot
            

        elif self.direction == "E":
            robotliste = list(robot)    # conversion de la position du robot de tuple à liste
            r0 = robotliste[0]
            r1 = robotliste[1]+1
            econtrol = self.grille[r0][r1]                  #variable qui va servir au controle de la valeur de la future position    

            if econtrol == 'U':
                print("SORTIE")

            if econtrol != "O":                                             # vérification de la position suivante
                self.grille[robotliste[0]][robotliste[1]] = " "             # réafectation de valeur sur la position de robot (libère la position)
                robotliste[1] = robot[1] +1                                 # modification de la valeur de robot en liste
                robot = tuple(robotliste)                                   # reconversion de robot en tuple pour vérif avec if in
                self.grille[robotliste[0]][robotliste[1]] = "X"             # nouvelle position du robot
            
        elif self.direction == "O":
            robotliste = list(robot)    # conversion de la position du robot de tuple à liste
            r0 = robotliste[0]
            r1 = robotliste[1]-1
            econtrol = self.grille[r0][r1]                  #variable qui va servir au controle de la valeur de la future position    
            
            if econtrol == 'U':
                print("SORTIE")

            if econtrol != "O":                                             # vérification de la position suivante
                self.grille[robotliste[0]][robotliste[1]] = " "             # réafectation de valeur sur la position de robot (libère la position)
                robotliste[1] = robot[1] -1                                 # modification de la valeur de robot en liste
                robot = tuple(robotliste)                                   # reconversion de robot en tuple pour vérif avec if in
                self.grille[robotliste[0]][robotliste[1]] = "X"             # nouvelle position du robot
            

        elif self.direction == "Q":         # sauvegarde à faire
            print("Fin de partie, au revoir")
            exit(0)

        elif self.direction == "HELP":          # affiche le texte de présentation 
            with open("README.md", "r") as fichier:
                content = fichier.read()
                print(content)





