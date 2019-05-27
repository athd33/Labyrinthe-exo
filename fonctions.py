import os
from carte import *


################### VARIABLES ####################

cartes = []


###################### FONCTIONS ####################

def init_score():                               # recherche d'anciens scores
    try:
        with open("data", "rb") as fichier:
            record = pickle.Unpickler(fichier)
            score = record.load()
    except:
        score = {}
        print("\nVous n'avez pas de partie en cours, alors bienvenue!")
    return score

def instance_map():
    for nom_fichier in os.listdir("cartes"):        # recherche de fichiers dans le dossier cartes
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-4].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                try:
                    carte = Carte(nom_carte, contenu)   # instanciation des cartes de classe Carte
                except:
                    print("Erreur de lecture de carte")
                else:
                    cartes.append(carte)                # remplissage de la liste carte avec les objets carte instanciés


def choose_map():                                       # fonction pour afficher le nom des cartes
    print("Voici les labyrinthes disponibles, lequel choisissez vous?  :")
    for content, carte in enumerate(cartes):
        print(f"  {content+1} - {carte.nom}")