
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
        self.content = self.chaine.split("\n")
        self.lignes = []
        self.grille = []

        for i in self.content:
            self.lignes.append(str(i))
        
                                            # méthode qui affiche la carte sous forme de grille 
    def __repr__(self):
        """
        Méthode d'affichage de la carte
        """    
        self.mapp = ""
        for i in self.lignes:
            self.mapp += '\n'
            for x in i:
                self.mapp += x
        return f"{self.mapp}"
    