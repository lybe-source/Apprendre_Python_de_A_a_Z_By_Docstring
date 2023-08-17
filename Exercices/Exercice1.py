# Concaténer des variables
# a = "J'ai une classe de " + 30 + " élèves" # J'ai une classe de 30 élèves
# b = 10 + " + " + "5" + " est égal à " + 15 # 10 + 5 est égal à 15
# c = 10 + "5" # 15
# d = "L'addition de 10 + 5 est égal à " + 10 + 5 # L'addition de 10 + 5 est égal à 15

# Solutions
a = "J'ai une classe de " + str(30) + " élèves" # J'ai une classe de 30 élèves
b = str(10) + " + " + "5" + " est égal à " + str(15) # 10 + 5 est égal à 15
c = 10 + int("5") # 15
d = "L'addition de 10 + 5 est égal à " + str(10 + 5) # L'addition de 10 + 5 est égal à 15

print(a)
print(b)
print(c)
print(d)