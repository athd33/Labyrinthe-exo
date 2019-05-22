


labyrinthe = []
ligne = []

with open('facile.txt', 'r') as fichier:
    chaine = fichier.read()

content = chaine.split("\n")
print(chaine)

###############################  CREATION DU LABYRINTHE AVEC IMBRICATION DE LISTES ################################
for lignes in content:
    ligne.append(list(lignes))
for letter in ligne:
    print(f"letter :{letter}")
    labyrinthe.append(letter)


print(f"labyrinthe{labyrinthe}")

################################ RECUPERATION DES COORDONNES DANS UN TUPLE  #########################################

for index_x, x in enumerate(labyrinthe):
    for index_y, y in enumerate(x):
        if y == "X":
            robot = (index_x, index_y)
        if y == "U":
            sortie = (index_x, index_y)
            
"""

print(f"robot : {robot}")            # affiche (3,8) la position de X

print(f"labyrinthe[3][8] : {robot}") # affiche X

print(f"sortie : {sortie}")

"""


print(f"position robot :{robot}")


print(f"robot {robot}")