"""Ce module contient la classe Labyrinthe."""


labyrinthe = []
ligne = []

class Labyrinthe:
    
	"""Classe permettant de créer et d'afficher le Labyrinthe"""
	def __init__(self, chaine):
		self.chaine = chaine
		self.structure = 0
	
	def indexation(self, chaine):
    """Création de la grille permettant le retrouver les éléments par index"""
        self.chaine = chaine
	    carte_en_cours = []
        lignes = []
		for ligne in chaine:   #pour chaque ligne dans la chaine de caractères
			for letter in ligne: # pour chaque lettre dans les lignes				
				if letter != '\n':  #si la lettre est n'est pas un retour à la ligne
					ligne.append(letter)  # on ajoute la lettre à la liste de lignes			                                
			carte_en_cours.append(lignes) #On ajoute la ligne à la liste du niveau		
		self.grille = carte_en_cours
	
	def afficher(self, fenetre):
		"""Méthode pout afficher la grille créée avec la méthode indexation"""		
		mur = "O"
		robot = "X"
		sortie = "U"
				
		num_ligne = 0
		for ligne in self.grille: #pour chaque ligne dans la grille générée			
			coordonnee = 0
			for letter in ligne:
				#On calcule la position réelle en pixels
				x = num_case * nombre_lettres
				y = num_ligne * nombre_lettres
				if letter == 'O':		   
					mur = (x,y)
				elif letter == 'X':		   
					robot = (x,y)
				elif sprite == 'S':		  
					sortie =(x,y)
				num_case += 1
			num_ligne += 1
