# La liste de courses
# Ajouter ou retirer des éléments à cette liste
# Afficher ce que la liste contient
# Vider le contenu de la liste
# Ca doit boucler sur la liste de choix une fois une action effectuée

#   Choississez parmi les 5 options suivantes :
#   1 : Ajouter un élément à la liste
#   2 : Retirer un élément de la liste
#   3 : Afficher la liste
#   4 : Vider la liste
#   5 : Quitter
#   👉 Votre choix : ""

# Suivant les choix que l'on fait :
# 1
#   Entrez le nom d'un élément à ajouter à la liste de courses : ""
#   L'élément "" a bien été ajouté à la liste.

# 2
#   Entrez le nom d'un élément à retirer de la liste de courses : ""
#   L'élément "" a bien été supprimé de la liste.
# Si on veut retirer un élément qui ne se trouve pas dans la liste, ce message devra être afficher :
#   L'élément "" n'est pas dans la liste.


# 3
#   Voici le contenu de votre liste :
#   1. ""
#   2. ""
# Le numéro doit être ajouté automatiquement
# Si la liste est vide, ce message devra être afficher :
#   Votre liste ne contient aucun élément.

# 4
#   La liste a été vidée de son contenu.

# 5
#   À bientôt !
# et sort de la boucle

liste = []
choice = 0

while choice >= 0 and choice <= 5:
    if choice == 1:
        increment_list = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(increment_list)
        print(f"L'élément {increment_list} a bien été ajouté à la liste.")
        print("_" * 50)
    elif choice == 2:
        decrement_list = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if not decrement_list in liste:
            print(f"L'élément {decrement_list} n'est pas dans la liste.")
            print("_" * 50)
        else:
            liste.remove(decrement_list)
            print(f"L'élément {decrement_list} a bien été supprimé de la liste.")
            print("_" * 50)
    elif choice == 3:
        if not liste:
            print("Votre liste ne contient aucun élément.")
            print("_" * 50)
        else:
            print("Voici le contenu de votre liste :")
            for index, element in enumerate(liste):
                print(str(index + 1) + ". " + element)
            print("_" * 50)
    elif choice == 4:
        liste.clear()
        print("La liste a été vidée de son contenu.")
        print("_" * 50)
    elif choice == 5:
        print("À bientôt !")
        print("_" * 50)
        break
    else:
        print("Veuillez choisir une option valide...")
        print("_" * 50)

    print("Choississez parmi les 5 options suivantes :")
    print("1 : Ajouter un élément à la liste")
    print("2 : Retirer un élément de la liste")
    print("3 : Afficher la liste")
    print("4 : Vider la liste")
    print("5 : Quitter")
    choice = input("👉 Votre choix : ")
    choice = int(choice)