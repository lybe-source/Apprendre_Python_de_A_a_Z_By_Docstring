# Opérateurs mathématique
# + - * /
print(5 + 3) # 8
print(3 - 2) # 1
print(4 * 5) # 20
print(6 / 2) # 3.0
print("Hello" + " World")
print("Python" * 3)

# % (Modulo) // (Division entière) ** (Puissance)
print(10 % 2) # 0
print(6 % 4) # 2
print(10 // 2) # 5
print(10 / 3) # 3.3333333333333335
print(10 // 3) # 3
print(2 ** 4) # 16

# Opérateurs d'assignation
i = j = 0
i = i + 1
j += 1
i -= 1
i *= 1
i /= 1
i %= 1
i //= 1
i **= 1
k = 5
k += 10
print(k)

# Opérateurs de comparaison
# > (plus grand que) < (plus petit que) >= (plus grand ou égal à) <= (plus petit ou égal à) == (égal à) != (différent de)

# La différence entre "is" et "==", "is" vérifie l'adresse utilisé par l'objet en mémoire
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # true
print(a is b) # false, parce que l'objet a n'est pas le même que b en mémoire, renverra true seulement si l'adresse en mémoire est la même pour les 2 objets
print(id(a))
print(id(b))
c = 10
d = 10
print(c is d) # true, parce que les nombres pour ces variables sont entre -5 et 256, python injecte les nombres dans cet intervale en mémoire, ils auront donc la même adresse mémoire
print(id(c))
print(id(d))
