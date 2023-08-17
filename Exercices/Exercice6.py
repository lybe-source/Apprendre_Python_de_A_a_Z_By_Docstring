# Sortir d'une boucle while
# Enoncé :
#continuer = "o"
#while continuer == "o":
#    print("On continue !")
#    input("Voulez-vous continuer ? o/n ")

continuer = "o"
while continuer == "o":
    print("On continue !")
    continuer = input("Voulez-vous continuer ? o/n ")

# Solution dans la vidéo de Docstring ( https://www.youtube.com/watch?v=LamjAFnybo0 ) à 5:42:37
# La même que moi (Beaucoup plus logique que la solution suivante)
# Solution vu à 5:44:02
continuer = "o"
while continuer == "o":
    print("On continue !")
    resultat = input("Voulez-vous continuer ? o/n ")
    if resultat != "o":
        break
