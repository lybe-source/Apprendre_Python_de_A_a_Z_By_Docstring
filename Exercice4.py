# Afficher 10 utilisateurs
i = 1
user = "Utilisateur"

while i < 11:
    print(user + " " + str(i))
    i += 1

# Solution de la vidéo de Docstring ( https://www.youtube.com/watch?v=LamjAFnybo0 ) à 5:35:23
for i in range(10):
    print(f"Utilisateur {i+1}")

# Solution de la vidéo à 5:36:42
for i in range(1, 11):
    print(f"Utilisateur {i}")