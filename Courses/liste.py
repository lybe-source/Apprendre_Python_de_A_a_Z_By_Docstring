# Liste ou tableau : nom_liste = [250, "Python", True]
liste = [1, 2, 3, 4, 5]
langage = ["Python", "C++", "Java", ["PHP", "Symfony", "WordPress"], ["MySQL", "PostgreSQL"], ["Javascript", "React", "Angular"]]

# Afin d'ajouter un élément à la liste
# La fonction append()
# Cette fonction ne permet d'ajouter UNE seule valeur à la fois
liste.append(6)

# Pour ajouter plusieurs valeurs en une fois
# On passe les valeurs à cette fonction sous forme d'une liste
#   liste.extend([10, 25, 30])
# Si vous lui passé plusieurs valeurs sans que ça soit une liste
#   liste.extend(10, 25, 30)
#   Cela produira une erreur
liste.extend([7, 8, 9])

# Afin de supprimer un élément de la liste
# La fonction remove()
# On lui passe la valeur que l'on veut retiré de la liste, la méthode remove ne retire que la première occurrence trouvé dans la liste
# Si il y a plusieurs occurrences dans la liste, il faudra faire autant de remove() qu'il y a d'occurrences
# Ce n'est pas l'indice de l'élément que l'on veut supprimé mais bien la valeur
liste.remove(3)

print(langage[0])

# Les slices
users = ["user_01",
         "user_02",
         "user_03",
         "user_04",
         "user_05",
         "user_06"]

# La tranche affichera que le premier car on commence à l'indice 0 et le 2ème indice passé est exclusif
print(users[0:1])

# Si on veut les 2 premiers users
print(users[0:2])

# Si on veut le 2ème et le 3ème users
print(users[1:3])

# Si on veut récupérer l'entièreté de la liste
print(users[:])
# ou
print(users[0:])

# Si on veut récupérer l'entièreté de la liste sauf le dernier élément
print(users[:-1])

# Si on veut récupérer un user sur 2
print(users[::2])

# Si on veut l'user 2, 4 et 6
print(users[1::2])

# Si on veut enlevé les 2 derniers user du calcul et afficher les user avec un pas de 2 en commençant par le 2ème élément
# le premier est l'indice
# le second est la fin et est exclusif
# le troisième est le pas
print(users[1:-2:2])

# Inverser la liste
print(users[::-1])


# Les méthodes que l'on peut utiliser sur les listes
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]

# La méthode index, elle donne l'indice de l'élément qu'on lui envoi, elle ne donne que la première occurrence trouvée dans la liste
resultat = employes.index("Max") # 1
print(resultat)


# La méthode count, elle permet de compter le nombre d'occurrences de l'élément qu'on lui envoi
resultat = employes.count("Max")
print(resultat)


# La méthode sort, elle permet de trier la liste
# Il ne faut pas la sauvegarder dans une variable, elle ne retourne rien, elle modifie la liste d'origine, si on la sauvegarde dans une variable par exemple :
#   employes = employes.sort()
# employes renverra None
employes.sort()
print(employes)

# Il existe une autre méthode pour trier la liste
# Cette fonction ne modifie pas la liste d'origine
liste_trie = sorted(employes)
print(liste_trie)


# Méthode permettant d'inverser la liste
# Elle ne trie pas l'ordre alphabétique, c'est comme si on commençait au dernier indice et qu'on diminuait celui-ci jusqu'à 0
employes.reverse()
print(employes)


# Méthode permettant de supprimer un élément de la liste par rapport à son indice
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]

# Supprimer le dernier élément
element = employes.pop(-1)
print(employes)
print(element)

# Supprimer tout les éléments de la liste
employes.clear()
print(employes)


# Joindre les éléments d'une liste qui sont des chaînes de caractères
chaine = ["python", "est", "un", "langage", "incroyable"]

# Le caractère avec lequel on veut joindre les éléments de la liste, la fonction join(liste)
resultat = " - ".join(chaine)
print(resultat)

# Faire comme la fonction pprint
# Ajouter un retour à la ligne entre chaque élément de la liste
resultat = "\n".join(chaine)
print(resultat)


# Créer une liste à partir d'une chaîne de caractère
courses = "Ris, Pommes, Lait, Salade, Saumon, Beurre"

# La méthode split() si on ne lui passe aucun argument, va se spliter sur les espaces
courses = courses.split()
print(courses)

courses = "Ris, Pommes, Lait, Salade, Saumon, Beurre"
# Ici la méthode va spliter sur la , mais gardant l'espace qui suivait la ,
courses = courses.split(",")
print(courses)

courses = "Ris, Pommes, Lait, Salade, Saumon, Beurre"
# Ici la méthode va spliter sur la , et l'espace qui suivait celle-ci,
# Donc ne pas oublié l'espace afin que la liste soit la mieux possible
# Cette méthode n'écrase pas la chaîne de caractère d'origine
courses_liste = courses.split(", ")
print(courses)
print(courses_liste)

# Attention, si le caractère sur lequel nous voulons split la chaîne de caractère n'est pas présent
# Nous aurons bien une liste mais avec UN SEUL élément comprenant la chaîne de caractère d'origine
courses_liste = courses.split("-")
print(courses_liste)


# Les opérateurs d'appartenance
# in        Permet de vérifié si un élément se trouve dans une liste ou dans une chaîne de caractère
# not in    Permet de vérifié qu'un élément ne se trouve pas dans une liste ou dans une chaîne de caractère
utilisateurs = ["Paul", "Pierre", "Marie"]
if "Paul" in utilisateurs: # True
    print("Bonjour Paul, bonne vacance prolongée !")
    utilisateurs.remove("Paul")
    print("Utilisateur supprimé")

if "Java" in "Javascript":
    print("Java est dans la chaîne 'Javascript'")
elif "Java" not in "Javascript":
    print("Java n'est pas dans la chaîne 'Javascript'")


# Les liste imbriqués
liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

# Si je veux récupérer le mot "Java"
print(liste[1][0])

# Si je veux récupérer le mot "C"
print(liste[1][2][0])

# Si je veux récupérer le mot "Ruby"
print(liste[2][0])

# Si on veut juste récupérer le "P" de "Python"
print(liste[0][0])

# Si on veut juste récupérer le "o" de "Python"
print(liste[0][-2])

# Si on veut récupérer les 2 premières lettre de "Python"
print(liste[0][0:2])