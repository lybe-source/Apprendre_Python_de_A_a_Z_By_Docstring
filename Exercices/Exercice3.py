# Intitulés des exercices :

# Exercice 1:
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = []

for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)

print(nombres_pairs) # [44, 4, 38]

# ----------------------------------------------------------------------------- #
# Exercice 2:
nombres = range(-10, 10)
nombres_positifs = []

for i in nombres:
    if i >= 0:
        nombres_positifs.append(i)

print(nombres_positifs) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ----------------------------------------------------------------------------- #
# Exercice 3:
nombres = range(5)
nombres_doubles = []

for i in nombres:
    nombres_doubles.append(i * 2)

print(nombres_doubles) # [0, 2, 4, 6, 8]

# ----------------------------------------------------------------------------- #
# Exercice 4:
nombres = range(10)
nombres_inverses = []

for i in nombres:
    if i % 2 == 0:
        nombres_inverses.append(i)
    else:
        nombres_inverses.append(-i)

print(nombres_inverses) # [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

# ----------------------------------------------------------------------------- #

# Réponses :
# Exercice 1:
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]

print(nombres_pairs) # [44, 4, 38]

# Exercice 2:
nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]

print(nombres_positifs) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exercice 3:
nombres = range(5)
nombres_doubles = [i * 2 for i in nombres]

print(nombres_doubles) # [0, 2, 4, 6, 8]

# Exercice 4:
nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]

print(nombres_inverses) # [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

# ----------------------------------------------------------------------------- #

# Correction:
# Les 4 exercices sont pareils dans la solution de la vidéo de Docstring sur youtube ( https://www.youtube.com/watch?v=LamjAFnybo0 ) à 5:29:44
# Ce qu'il faut retenir est que lorsque l'on a un else, la condition se retrouve au début