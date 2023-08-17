# Le nombre mystère
#   ✨ Le jeu du nombre Mystère ✨
# Le nombre d'essai maximum est de 5

# Il doit boucler sur les textes suivants
#   Il te reste nombre_essai_restant essais
#   Devine le nombre : ""

# Si on entre autre chose qu'un nombre :
#   Veuillez entrer un nombre valide.

# Si le nombre mystère est plus petit que le nombre entrer :
#   Le nombre mystère est plus petit que ""
# Le nombre d'essai doit diminuer

# Si le nombre mystère est plus grand que le nombre entrer :
#   Le nombre mystère est plus grand que ""
# Le nombre d'essai doit diminuer

# Si on trouve le nombre mystère :
#   Bravo ! Le nombre mystère était bien le_nombre_mystere
#   Tu as trouvé le nombre en nombre_essai essai

# Si le nombre d'essai atteint 0 :
#   Dommage ! Le nombre mystère était le_nombre_mystere
#   Fin du jeu.

import random
import sys

NUMBER_MYSTERE = random.randint(0, 100)
NUMBER_MYSTERE = str(NUMBER_MYSTERE)
RANGE = range(100)
TRY = 5
REST = 1
print(NUMBER_MYSTERE)

print("✨ Le jeu du nombre Mystère ✨")

while TRY > 0: # Tant que TRY est STRICTEMENT supérieur à 0
    user_choice = ""
    while user_choice != NUMBER_MYSTERE or TRY >= 1: # Tant que user_choice est différent de NUMBER_MYSTERE
        if TRY < 2:
            essais = "essai"
        else:
            essais = "essais"

        print(f"Il te reste {TRY} {essais}")
        user_choice = input("Devine le nombre : ")

        if not user_choice.isdigit(): # Si user_choice n'est pas un nombre
            print("Veuillez entrer un nombre valide.")
        elif user_choice > NUMBER_MYSTERE: # Si user_choice est supérieur à NUMBER_MYSTERE
            print(f"Le nombre mystère est plus petit que {user_choice}")
            TRY -= 1
            REST += 1
        elif user_choice < NUMBER_MYSTERE: # Si user_choice est inférieur à NUMBER_MYSTERE
            print(f"Le nombre mystère est plus grand que {user_choice}")
            TRY -= 1
            REST += 1
        elif user_choice == NUMBER_MYSTERE: # Si user_choice est égal à NUMBER_MYSTERE
            if REST < 2:
                essais = "essai"
            else:
                essais = "essais"
            print(f"Bravo ! Le nombre mystère était bien {NUMBER_MYSTERE}")
            print(f"Tu as trouvé le nombre en {REST} {essais}")
            sys.exit()
        elif TRY == 0: # Si TRY est égal à 0
            sys.exit()
            
print(f"Dommage ! Le nombre mystère était {NUMBER_MYSTERE}")
print("Fin du jeu.")
