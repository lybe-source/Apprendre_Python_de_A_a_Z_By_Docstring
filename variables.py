a = 5
b = 10
c = a + b
aa = a
print(c) # 15
print(aa) # 5
a = a + 1
print(aa) # 5

id(a)

# Affectations simples
# nom = objet
c = 5
d = 8
a = "Bonjour"

# Affectations parallèles
c, d = 5, 8
a, b = b, a
a, b, c, d, e, f = 1, 2, 3, 4, 5, 6

# Affectations multiples
a = b = c = 5

# Les règles à suivre 
# pour nommer une variable

# Ne peut pas commencer par un chiffre
# Ne peut pas contenir d'espaces
# Ne peut contenir que des caractères alpha-numériques (A-z, 0-9) et l'underscore (_)
# Certains mots sont réservés (print, True, break, ...)

# Exemple de variables dont une erreur de syntaxe pourrait se produire :
# 75Paris       Commence par un chiffre
# Site-Web      Contient un tiret (-)
# #lien video   Contient un dièse (#) et un espace
# True          Utilise un mot réservé

# Pour les utiliser tout de même, il faudrait faire quelques modifications :
# Paris75
# Site_Web
# lienVideo
# true

# Les conventions de nommage de variables
# Nommer les variables en minuscule et séparé chaque mots par un underscore
# paris_75
# site_web
# lien_video
# true

print("Conversion de type de variable")
a = 5
b = "10"
b = int(b)
print(a + b)
c = "15"
int(c)
print(type(b))
print(type(c))

nombre = input("Entrez un nombre : ")
print(nombre)
print(type(nombre))
nombre = int(nombre)
print(type(nombre))