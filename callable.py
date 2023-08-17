# La fonction callable() permet de dire si un objet est appelable ou non
# Un exemple d'un objet appelable est os.makedirs()
# Un module n'est pas appelable
# Un indice sur l'appelabilité d'un objet est si on peut ou non mettre des paranthèse après celui-ci
# On ne peut pas faire par exemple os() mais on peut faire os.makedirs()

import pprint

print(callable(pprint)) # False

from pprint import pprint

print(callable(pprint)) # True, car ici c'est la fonction pprint et non le module

import os

print(callable(os.name)) # False, car cela est une chaîne de caractère disant sur quel os on se trouve
print(os.name) # NT

# print(os.name()) # Cela enverrai une erreur de type : TypeError: 'str' object is not callable
