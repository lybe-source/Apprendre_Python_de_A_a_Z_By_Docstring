import sys

LISTE = []

MENU = """Choississez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
    user_choice = ""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("Veuillez choisir une option valide...")

    if user_choice == "1": # Ajouter un élément
        item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        LISTE.append(item)
        print(f"L'élement {item} a bien été ajouté à la liste.")
    elif user_choice == "2": # Retirer un élément
        item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'élément {item} a bien été supprimé de la liste.")
        else:
            print(f"L'élément {item} n'est pas dans la liste.")
    elif user_choice == "3": # Afficher la liste
        if LISTE:
            print("Voici le contenu de votre liste :")
            for i, item in enumerate(LISTE, 1): # Le 1 permet de dire que l'on veut commencer à l'indice 1 donc i prendra la valeur de 1 à la première itération de la boucle
                print(f"{i}. {item}")
        else:
            print("Votre liste ne contient aucun élément.")
    elif user_choice == "4": # Vider la liste
        LISTE.clear()
        print("La liste a été vidée de son contenu.")
    elif user_choice == "5": # Quitter
        print("À bientôt !")
        sys.exit() # Permet de sortir du script lorsque l'on est dans un script en ligne de commande

    print("-" * 50)