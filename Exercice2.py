# Le vérificateur de mot de passe
# L'utilisateur entre un mot de passe
# On va vérifié si le mot de passe est valide

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

mdp_assez_long = "Votre mot de passe est assez long."
mdp_only_number = "Votre mot de passe ne contient que des nombres."

# Si le mdp est vide
if mdp == "":
    print(mdp_trop_court.upper())
# Si le mdp est inférieur à 8 caractères
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
# Si le mdp ne contient que des nombres
elif mdp.isdigit():
    print(mdp_only_number)
else:
    print(mdp_assez_long)
    print("Inscription terminée.")