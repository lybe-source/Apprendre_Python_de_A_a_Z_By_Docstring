# Concaténation et f-string
a = "bonjour"
b = "tout"
c = "le"
d = "monde"
print(a + " " + b + " " + c + " " + d)
e = 18
print("Vous avez " + str(e) + " ans")

# les f-string
prenom = "Paul"
print(f"Bonjour {prenom} !") # Bonjour Paul

f = 5
g = 10
print(f"La multiplication de {f} par {g} est égale à {f * g}") # La multiplication de 5 par 10 est égale à 50

# La méthode format
prenom = "Pierre"
age = 36
phrase = f"J'ai {age} ans" # f-string
phrase_2 = "J'ai {} ans".format(age) # méthode format
print(phrase)
print(phrase_2)
phrase = "Je m'appelle {0} et j'ai {1} ans, {year} ce n'est pas très agé".format(prenom, year=age) # {0} {1} etc serait les indice des variables passé à la méthode format

protocole = "https://"
nom_du_site = "Docstring"
extension = "fr"

# Avec l'opérateur +
url = protocole + "www." + nom_du_site + "." + extension

# Avec la méthode format
url = "{}www.{}.{}".format(protocole, nom_du_site, extension)
url = "{protocole}www.{domaine}.{extension}".format(protocole=protocole, domaine=nom_du_site, extension="fr")

# Avec les f-string
url = f"{protocole}www.{nom_du_site}.{extension}"


# À quel moment la méthode format est encore utile après la version 3.8 de python
prenom = "Jean"
# phrase = f"Bonjour {prenom}, cette semaine vous avez regardé {nombre} vidéos." # nombre n'est pas défini, avec les f-string, chaque variables doivent être définie et disponible tout de suite
BONJOUR = "Bienvenue {prenom}, vous avez regardé {nombre_videos} vidéos cette semaine."
AU_REVOIR = "À bientôt {prenom} !"