# Le nombre entré par l'utilisateur est-il plus grand ou égal à 18?
# age >= 18

# Le nom d'utilisateur entré est-il dans la base de donnée du site?
# nom_utilisateur in liste_utilisateurs

# Le mot de passe de l'utilisateur contient-il au moins 8 caractères?
# len(mot_de_passe) > 8

# if condition:
#   code

age = int(input("Quel âge avez-vous ? : "))
langage = "Python"
utilisateur = "admin"

if age >= 18:
    print("Vous êtes majeur !")
    if langage == "Python":
        print("Vous pouvez rentrer")
    elif langage == "python":
        print("Il nous est impossible de vous laissez entrer !")
elif age < 18:
    print("Vous êtes mineur")

if utilisateur == "admin":
    print("Accès autorisé !")
elif utilisateur == "root":
    print("Accès autorisé !")
else:
    print("Accès refusé...")

print("Le script est terminé")

# print("Bonjour")
#   print("Comment ça va?")
# Cela apportera une erreur indentation car la 2ème ligne est indenté mais n'est pas rattaché à une condition,


# Les ternaires
age = 20
majeur = True if age >= 18 else False
# Cela ne fonctionne que pour les structures conditionnelles if else, si il y a une structure conditionnelles if elif else, cela ne fonctionnerait pas


# Les opérateurs logique
# and, or, not
# Python évalue ces opérateurs dans un ordre particulier :
#   and
#   or
#   

# Il y a tout de même un moyen de modifier l'ordre de priorité des opérateurs logique avec les parantèses :
# 5 > 2 and (5 < 10 or 5 > 15)
#           (TRUE or FALSE)
#           ( TRUE )
# TRUE  and (TRUE)
# TRUE

# TRUE and TRUE = TRUE
# TRUE and FALSE = FALSE
# FALSE and TRUE = FALSE
# FALSE and FALSE = FALSE

# TRUE or TRUE = TRUE
# TRUE or FALSE = TRUE
# FALSE or TRUE = TRUE
# FALSE or FALSE = FALSE

# if utilisateur == "admin":
#   if mot_de_passe == "admin":
#       print("Accès autorisé")
mot_de_passe = "admin"

if utilisateur == "admin" and mot_de_passe == "admin":
    print("Accès autorisé")

# 5 > 2 and 5 < 10 and 5 > 15
# True and True and False
# Comme il y a un False, la condition sera fausse

# 5 > 2 and 5 < 10 or 5 > 15
# True and True or False
# Cela reviendrai à dire : True or False
# Avec le or, il suffit qu'une seule condition soit True pour que la condition soit vraie

# not True = False
# not False = True
if not utilisateur == "admin":
    print("Accès refusé...")