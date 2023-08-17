# import nom_du_module
# nom_du_module.nom_fonction()
# Le . permet de dire que la fonction appartient au module

# Le module random
import random

# nombre entier random entre le premier nombre donné et le second nombre donné inclus
r = random.randint(0, 1)
print(r)

# nombre décimaux random entre le premier nombre donné et le second nombre donné inclus
r = random.uniform(0, 1)
print(r)

# nombre entier entre 0 et le nombre donné, celui-ci est exclusif, cela veut dire qu'il ne sera jamais inclus
r = random.randrange(999)
print(r)

# nombre entier entre 0 et 100 inclus, avec un pas de 10, cela veut dire qu'il sera toujours une dizaine, exemple : 80, 40, 50, 10, 100, etc
r = random.randrange(0, 101, 10)
print(r)

# Le module os
import os

chemin = "/Users/s3iir/Desktop/Python/"
# Création d'un dossier
dossier = os.path.join(chemin, "dossier")
print(dossier)

if not os.path.exists(dossier):
    # Il existe la fonction mkdir aussi mais si on veut créer une structure avec des sous-dossier, il y aurait une erreur car mkdir ne sait le faire
    os.makedirs(dossier)

# Création d'un dossier et d'un sous-dossier
dossier2 = os.path.join(chemin, "dossier2", "test")
print(dossier2)
# exist_ok=True est pareil que de faire la condition if
os.makedirs(dossier2, exist_ok=True)
print("Dossiers créés")
if os.path.exists(dossier2):
    os.removedirs(dossier2)
    print("Dossiers supprimés")


# Comment savoir ce qui peut être fait avec un module
# La fonction dir()
# Cela donne une liste de fonction que l'on peut utiliser avec le module
print(dir(random))

# La fonction help()
# Pas besoin de l'appeler dans un print()
# Ne pas ajouter les paranthèse à la fin de la fonction pour laquelle on veut de l'aide car on ne veut pas appeler la fonction mais juste indiquer à help() quelle fonction on veut afficher
help(random.randint)

# La fonction pprint du module pprint
from pprint import pprint
# pprint() à contrario de print() permet un affichage plus lisible d'une liste
pprint(dir(random))