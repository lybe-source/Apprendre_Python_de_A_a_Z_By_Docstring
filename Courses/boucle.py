# La boucle for
# Syntaxe : 
# for element in liste:
#   print(element)
for i in [0, 1, 4, 7, 8]:
    print(i)


for lettre in "Python":
    print(lettre)


for i in range(10):
    print("Bonjour")

# La boucle while
# Syntaxe :
# while condition:
#   print("Bonjour")
i = 0
while i < 10:
    print("Salut")
    i += 1


continuer = "o"
while continuer == "o":
    print("On continue...")
    continuer = input("Voulez-vous continuer ? o/n ")


# Cette fonction devrait être kill dans les processus sous le nom "python" si elle était lancé
# Le print se ferait toutes les 10 minutes à cause du sleep(600)
#import time

#while True:
#    print("Sauvegarde en cours...")
#    time.sleep(600)


# Instruction "continue" et "break"
liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        continue
    print(element) # Paul, Pierre

liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        break
    print(element) # Rien ne s'affiche, l'instruction break fait sortir de la boucle


# List comprehension
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = []
for i in liste:
    if i > 0:
        nombres_positifs.append(i)

# Il n'y aurait aucun changement dans la liste d'origine
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = [i for i in liste] # [] (pour la liste), for i in liste (pour la boucle) et i (la donnée que l'on veut récupérer, si dans le for à la place du "i" on mettait "nombre", on devrait mettre "nombre" à la place du premier "i")
print(nombres_positifs) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Filter avec une structure conditionnelle
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = [i for i in liste if i > 0] # le if permettra de filtrer les nombres positifs
print(nombres_positifs) # [1, 2, 3, 4, 5]

# Filtrer avec une structure conditionnelle et les multiplier par 2
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombres_positifs = [i * 2 for i in liste if i > 0] # * 2 Permet de multiplier les nombres positifs par 2
print(nombres_positifs) # [2, 4, 6, 8, 10]
