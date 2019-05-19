



labyrinthe = []
ligne = []


with open('facile.txt', 'r') as fichier:
    chaine = fichier.read()

content = chaine.split("\n")
print(chaine)

###############################  CREATION DU LABYRINTHE AVEC IMBRICATION DE LISTES ################################
for x in content:
    ligne.append(list(x))
for e in ligne:
    print(e)
    labyrinthe.append(e)

print(labyrinthe)

################################ RECUPERATION DES COORDONNES DANS UN TUPLE  #########################################

for index_x, x in enumerate(labyrinthe):
    for index_y, y in enumerate(x):
        if y == "X":
            robot = (index_x, index_y)

print(robot)
print(labyrinthe[3][8])




