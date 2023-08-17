# Jeu de rôle
# Règles du jeu :
# Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.
#   Le jeu comporte 2 joueurs: vous et un ennemi.
#   Vous commencez tous les 2 avec 50 points de vie.
#   Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vies.
#   L'ennemie ne dispose d'aucune potion.
#   Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
#   Votre attaque inflige à l'ennemi des dégats aléatoires compris entre 5 et 10 points de vie.
#   L'attaque de l'ennemi vous inflige des dégats aléatoires compris entre 5 et 15 points de vie.
#   Lorsque vous utilisez une potion, vous passez le prochain tour.

# Déroulé de la partie
# Lorsque vous lancez le script, vous devez demander à l'utilisateur s'il souhaite attaquer ou utiliser une potion:
#   "Souhaitez-vous attaquer (1) ou utilisez une potion (2) ? "
# Cette phrase sera demandée à l'utilisateur au début de chaque tour.
# 👉 Si l'utilisateur choisi la première option (1), vous infligez des points de dégat à l'ennemi.
# Ces points seront compris entre 5 et 10 et déterminés aléatoirement par le programme.
# 👉 Si l'utilisateur choisi la deuxième option (2), vous prenez une potion.


# Si l'utilisateur entre un choix erroné ou une chaine de caractère, cela doit redemander la phrase si il veut attaquer ou utiliser une potion
# Si l'utilisateur décide d'attaquer :
#   Vous avez infligé degat_aleatoire points de dégats à l'ennemi ⚔️
#   L'ennemi vous a infligé degat_aleatoire points de dégats ⚔️
#   Il vous reste nombre_HP points de vie.
#   Il reste nombre_HP points de vie à l'ennemi.
#   ---------------------------------------------
#   Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?

# Si l'utilisateur décide d'utiliser une potion :
#   Vous récupérer hp_aleatoire_potion points de vie ❤️ (nombres_potions_restante 🧪 restantes)
#   L'ennemi vous a infligé degat_aleatoire points de dégats ⚔️
#   Il vous reste nombre_HP points de vie.
#   Il reste nombre_HP points de vie à l'ennemi.
#   ------------------------------------------------
#   Vous passez votre tour...
#   L'ennemi vous a infligé degat_aleatoire points de dégats ⚔️
#   Il vous reste nombre_HP points de vie.
#   Il reste nombre_HP points de vie à l'ennemi.
#   ------------------------------------------------
#   Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?

# Si l'utilisateur décide d'utiliser une potion alors qu'il n'en a plus :
#   Vous n'avez plus de potions...
#   Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?

# Si les points de vie de l'ennemi atteignent 0 :
#   Vous avez infligé degat_aleatoire points de dégats à l'ennemi ⚔️
#   Tu as gagné 💪
#   Fin du jeu.

# Si les points de vie du joueur atteignent 0 :
#   Vous avez infligé degat_aleatoire points de dégats à l'ennemi ⚔️
#   L'ennemi vous a infligé degat_aleatoire points de dégats ⚔️
#   Tu as perdu ☠️
#   Fin du jeu.

from random import randint

player = ""
enemy = "Barb"

HP_PLAYER = 50
HP_ENEMY = 50

POTIONS_COUNT = 3 # Récupération de points de vie entre 15 et 50 par potion
# attaque_player entre 5 et 10
# attaque_enemy entre 5 et 15

# Lorsque j'utilise une potion, l'ennemi m'attaque, je passe le tour suivant et l'ennemi me réattaque

print("✨ Jeu de rôle ✨")

while HP_PLAYER > 0 or HP_ENEMY > 0:
    user_choice = input("Souhaitez-vous attaquer (1) ou utilisez une potion (2) ? ")

    if not user_choice.isdigit():
        continue

    user_choice = int(user_choice)

    if user_choice < 1 or user_choice > 2:
        continue

    elif user_choice == 1:
        random_damage_player = randint(5, 10)
        print(f"Vous avez infligé {random_damage_player} points de dégats à l'ennemi ⚔️")
        HP_ENEMY -= random_damage_player
        random_damage_enemy = randint(5, 15)
        print(f"L'ennemi vous a infligé {random_damage_enemy} points de dégats ⚔️")
        HP_PLAYER -= random_damage_enemy
        print(f"Il vous reste {HP_PLAYER} points de vie.")
        print(f"Il reste {HP_ENEMY} points de vie à l'ennemi.")
        print("-" * 50)
    else:
        if POTIONS_COUNT > 0:
            random_life_points = randint(15, 50)
            HP_PLAYER += random_life_points
            POTIONS_COUNT -= 1
            print(f"Vous récupérer {random_life_points} points de vie ❤️ ({POTIONS_COUNT} 🧪 restantes)")
            for i in range(2):
                if i == 1:
                    print("Vous passez votre tour...")
                random_damage_enemy = randint(5, 15)
                print(f"L'ennemi vous a infligé {random_damage_enemy} points de dégats ⚔️")
                HP_PLAYER -= random_damage_enemy
                print(f"Il vous reste {HP_PLAYER} points de vie.")
                print(f"Il reste {HP_ENEMY} points de vie à l'ennemi.")
                print("-" * 50)
        else:
            print("Vous n'avez plus de potions...")
            continue

if HP_ENEMY <= 0:
    print(f"Vous avez infligé {random_damage_player} points de dégats à l'ennemi ⚔️")
    print("Tu as gagné 💪")
elif HP_PLAYER <= 0:
    print(f"Vous avez infligé {random_damage_player} points de dégats à l'ennemi ⚔️")
    print(f"L'ennemi vous a infligé {random_damage_enemy} points de dégats ⚔️")
    print("Tu as perdu ☠️")

print("Fin du jeu.")