hello = "Bonjour"
wold = "bonjour tout le monde"
print(hello.upper()) # Modifie la chaîne de caractère pour la mettre en majuscule
print(hello.lower()) # Modifie la chaîne de caractère pour la mettre en minuscule
print(wold.capitalize()) # Permet de modifier la première lettre de la chaîne de caractère afin de la mettre en majuscule
print(wold.title()) # Permet de mettre la première lettre de chaque mot en majuscule


# Modifier ou remplacer des caractères
print(hello.replace("jour", "soir")) # Permet de modifier la chaîne de caractère, le premier paramètre et ce que l'on veut modifier et le second par quoi nous voulons le modifier
print(hello + " " + hello.replace("jour", "soir"))
print("Bonjour bonjour".replace("jour", "soir"))
print("Bonjour bonjour".replace(" ", "").replace("jour", "soir"))

# Suppression de caractères
hey = " bonjour "
hey_esp = " bon jour "
print(hey.strip())
print(hey_esp.strip())
print(hey.strip(" ujor")) # La fonction va annalysé la chaîne de caractère en commençant par le début, il y a un espace donc il sera supprimé, il n'y a pas de b dans les caractères spécifié dans strip donc il ne sera pas supprimé, et le traitement s'arrête donc, il reprend en commençant par la fin, il y a un r, u, o, j donc ils seront supprimé, il n'y a pas de n donc le traitement s'arrête, il n'y a pas d'importance dans l'ordre des caractères spécifié dans la méthode strip
print(hey.rstrip(" ujor")) # Pareil que pour la méthode strip, cependant celle-ci ne fera qu'en commençant par la fin de la chaîne de caractère jusqu'à trouvé un caractère qui ne se trouve pas dans la chaîne de caractère
print(hey.lstrip(" ujor")) # Pareil que pour la méthode strip, cependant celle-ci ne fera que le début de la chaîne de caractère

# Séparer et joindre
a = "1, 2, 3, 4, 5"
liste = a.split(", ")
print(a)
print(liste)
b = ", ".join(liste)
print(b)
c = "-".join(['1', '2', '3'])
print(c)
liste2 = ['1', '2', '3']
print(type(liste2[0]))
liste2_0 = int(liste2[0])
print(type(liste2_0))
print(int(liste2[0]) + 3)

# Remplir de zéro
a = "9"
a.zfill(4) # Mettra 3 zéro au début de la chaîne de caractère
print(a)

# Les méthodes "is"
bonjour = "bonjour"
print(bonjour.islower()) # true
monde = "Bonjour tout le monde"
print(monde.istitle()) # false
print(a.isdigit()) # true, la chaîne de caractère de la variable "a" est composée que de chiffre

# Compter les occurrences dans une chaîne de caractère
jour = " le jour"
a = bonjour + jour
print(a.count("jour")) # 2, bon"jour" le "jour"
print(a.count(" jour")) # 1, bonjour le" jour"

# Trouver une chaîne de caractère ou une suite de caractère
print(a.find("jour")) # 3, parce que la première occurrence du mot jour démarre à l'index 3 de la chaîne de caractère
print(a.index("jour")) # 3, pareil que la précédente
print(a.find("soir")) # -1, la chaîne de caractère "soir" n'a aucune occurrence dans la chaîne de caractère initiale
# print(a.index("soir")) # ValueError: substring not found
print(a.rfind("jour")) # 11, pareil que pour find, cependant cela démarre à la fin de la chaîne de caractère, le r de jour est situé à l'index 11 donc la méthode répond 11

# Chercher au début et à la fin
image = "image.png"
print(image.endswith(".png")) # true
print(image.endswith("png")) # true
print(image.endswith("jpg")) # false
print(image.startswith("image")) # true
print(image.startswith("video")) # false


# Calculer la longueur d'une chaîne de caractère ou la taille d'une liste
len("Python") # 6, le nombre de caractères de la chaîne de caractère
len([1, 2, 3]) # 3, le nombre d'élément dans la liste


# Arrondir un nombre décimale au nombre entier le plus proche
round(2.2) # 2
round(2.7) # 3


# Récupérer la valeur min et la valeur max à l'intérieur d'une structure de donnée
min([1, 2, 3]) # Donnera le min = 1
max([1, 2, 3]) # Donnera le max = 3
# Peut aussi être utiliser sur des chaîne de caractère
min("abc") # a
max("abc") # c


# Récupérer la somme des éléments dans une liste
sum([10, 10, 10]) # 30
# sum([10, 10, "Python"]) # TypeError : unsupported operand type for +: 'int' and 'str'


# Créer une liste de nombre allant de 0 à un nombre indiqué dans la fonction -1
range(5) # [0, 1, 2, 3, 4]
# On peut lui spécifié un départ
range(2, 5) # [2, 3, 4]