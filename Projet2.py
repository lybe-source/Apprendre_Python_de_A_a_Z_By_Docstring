# Calculatrice
# Demander à l'utilisateur de saisir 2 nombres
# Afficher l'addition de ces 2 nombres à l'écran
# Les phrases :
#   Entrez un premier nombre : ""
#   Entrez un deuxième nombre : ""
#   Le résultat de l'addition de "" avec "" est égal à ""
# Gestion des erreurs si l'utilisateur n'entre pas un nombre :
# Si on entre 2 lettres : (cela doit boucler si dans le cas où les input ne sont pas des nombres)
#   Veuillez entrer deux nombres valides

# Cela doit boucler tant que les input ne sont pas des nombres
# Si les 2 input sont des nombres, cela fait le calcul et affiche la phrase donnée

nombre_1 = input("Entrez un premier nombre : ")
nombre_2 = input("Entrez un deuxième nombre : ")

while True:
    if nombre_1.isdigit() and nombre_2.isdigit():
        nombre_1 = int(nombre_1)
        nombre_2 = int(nombre_2)
        break
    else:
        print("Veuillez entrer deux nombres valides")
        nombre_1 = input("Entrez un premier nombre : ")
        nombre_2 = input("Entrez un deuxième nombre : ")

print(f"Le résultat de l'addition de {nombre_1} avec {nombre_2} est égal à {nombre_1 + nombre_2}")

# Solution de la vidéo de Docstring ( https://www.youtube.com/watch?v=LamjAFnybo0 ) à 5:46:50
a = b = ""

while not (a.isdigit() and b.isdigit()):
    a = input("Entrez un premier nombre : ")
    b = input("Entrez un deuxième nombre : ")
    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides")

print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
