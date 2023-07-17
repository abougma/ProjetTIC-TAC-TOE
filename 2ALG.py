import random

def menu():
    while True:
        print("---------- MENU TIC TAC TOE ----------")
        print("1. Jouer")
        print("2. Règles du jeu")
        print("3. Afficher le Hall of Fame")
        print("4. Quitter")

        choice = input("Entrer votre choix : ")
        
        if choice == '1':
             execute()
        elif choice == '2':
             rule()
        elif choice == '3':
             display_hall_of_fame()
        elif choice == '4':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")
                            

def hall_of_fame(grille):
    print("---------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(grille[i][j], end=" | ")
        print("\n---------")

def execute():
        symboles = ["X", "O"]
        grille = [[" " for _ in range(3)] for _ in range(3)]

        print("Le jeu commence !")
        name1 = input("Nom du joueur 1 : ")
        name2 = input("Nom du joueur 2 : ")

        while True:
            first_player = random.choice([name1, name2])
            print("Le joueur", first_player, "commence !")

            print("Le joueur 1 ", name1, " son symbole est 'X'")
            print("Le joueur 2 ", name2, " son symbole est 'O'")

            current_player = first_player
            current_symbol = symboles[0]

            while True:
                print("Tour du joueur", current_player)
                ligne = int(input("Choisissez la ligne (1, 2, 3) : "))
                colonne = int(input("Choisissez la colonne (1, 2, 3) : "))

                if 1 <= ligne <= 3 and 1 <= colonne <= 3:
                    if grille[ligne - 1][colonne - 1] == " ":
                        grille[ligne - 1][colonne - 1] = current_symbol
                        hall_of_fame(grille)

                        # Vérifier si le joueur a gagné ou s'il y a un match nul
                        if winner(grille, current_symbol):
                            print("Le joueur", current_player, "a gagné !")
                            break
                        elif draw(grille):
                            print("Match nul !")
                            break

                        # Changer de joueur et de symbole
                        if current_symbol == symboles[0]:
                            current_symbol = symboles[1]
                            current_player = name2
                        else:
                            current_symbol = symboles[0]
                            current_player = name1
                    else:
                        print("Cette case est déjà occupée")
                else:
                    print("Coordonnées invalides. Veuillez choisir des coordonnées dans les limites du plateau (1 à 3)")

            play_again = input("Voulez-vous jouer à nouveau ? (Oui/Non) ")
            if play_again.lower() == "non":
                break
            else:
                grille = [[" " for _ in range(3)] for _ in range(3)]
def rule():
        print("Deux joueurs s'affrontent dans un jeu au tour par tour sur une grille 3x3 (3 lignes et 3 colonnes).")
        print("Le Joueur 1 utilise le symbole 'X' tandis que le Joueur 2 utilise le symbole 'O'.")
        print("Les joueurs doivent placer leurs symboles dans une case vide de la grille en entrant les coordonnées correspondantes.")
        print("Les joueurs jouent tour à tour en plaçant un symbole à chaque tour.")
        print("Le but du jeu est d'aligner trois symboles identiques horizontalement, verticalement ou en diagonale.")
        print("Si aucun joueur ne parvient à aligner 3 symboles identiques lorsque la grille est remplie, la partie se termine par un match nul.")
        print("À la fin de la partie, les gagnants seront enregistrés dans notre 'Hall of Fame' !")

def display_hall_of_fame():
        grille = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "O", "X"]
        ]
        hall_of_fame(grille)


def winner(grille, symbole):
    # Vérification des lignes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == symbole:
            return True

    # Vérification des colonnes
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] == symbole:
            return True

    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True

    return False

def draw(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return False
    return True

menu()
