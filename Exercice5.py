# Afficher un mot à l'envers avec une boucle
mot = "Python"
# L'exercice doit afficher :
# n
# o
# h
# t
# y
# P

for i in "".join(reversed(mot)):
    print(i)

# Solution dans la vidéo de Docstring ( https://www.youtube.com/watch?v=LamjAFnybo0 ) à 5:38:27
mot = "Python"
# print(list(reversed(mot)))
for lettre in reversed(mot):
    print(lettre)
