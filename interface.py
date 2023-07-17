import tkinter as tk
from tkinter import messagebox
import random

def toggle_fullscreen(window):
    state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not state)

def show_rules():
    rules_text = """
Deux joueurs s'affrontent dans un jeu au tour par tour sur une grille 3x3 (3 lignes et 3 colonnes).
Le Joueur 1 utilise le symbole 'X' tandis que le Joueur 2 utilise le symbole 'O'.
Les joueurs doivent placer leurs symboles dans une case vide de la grille en cliquant sur les boutons correspondants.
Les joueurs jouent tour à tour en plaçant un symbole à chaque tour.
Le but du jeu est d'aligner trois symboles identiques horizontalement, verticalement ou en diagonale.
Si aucun joueur ne parvient à aligner 3 symboles identiques lorsque la grille est remplie, la partie se termine par un match nul.
    """
    messagebox.showinfo("Règles du jeu", rules_text)

def quit_game():
    window.destroy()

def play():
    symboles = ["X", "O"]
    grille = [[" " for _ in range(3)] for _ in range(3)]

    name1 = entry_name1.get()
    name2 = entry_name2.get()

    if not name1 or not name2:
        messagebox.showwarning("Erreur", "Veuillez entrer les noms des deux joueurs.")
        return

    first_player = random.choice([name1, name2])
    label_turn.config(text="Tour de " + first_player)

    current_player = first_player
    current_symbol = symboles[0]

    def place_symbol(row, col):
        if grille[row][col] == " ":
            grille[row][col] = current_symbol
            buttons[row][col].config(text=current_symbol)

            if winner(grille, current_symbol):
                label_turn.config(text="Le joueur " + current_player + " a gagné !")
                disable_buttons()
            elif draw(grille):
                label_turn.config(text="Match nul !")
                disable_buttons()
            else:
                change_player()

    def change_player():
        nonlocal current_player, current_symbol

        if current_player == name1:
            current_player = name2
            current_symbol = symboles[1]
        else:
            current_player = name1
            current_symbol = symboles[0]

        label_turn.config(text="Tour de " + current_player)

    def disable_buttons():
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(state=tk.DISABLED)

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

    # Création de la grille de boutons
    buttons = []
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(main_frame, text=" ", font=("Arial", 40), width=5, height=2,
                               command=lambda r=row, c=col: place_symbol(r, c))
            button.grid(row=row+4, column=col, padx=10, pady=10)
            button_row.append(button)
        buttons.append(button_row)

    button_play.config(state=tk.DISABLED)
    button_rules.config(state=tk.DISABLED)
    button_quit.config(state=tk.DISABLED)

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry("800x600")

# Barre de menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Menu Options
menu_options = tk.Menu(menu_bar, tearoff=0)
menu_options.add_command(label="Plein écran", command=lambda: toggle_fullscreen(window))
menu_options.add_command(label="Redimensionnable", command=lambda: window.attributes("-fullscreen", False))
menu_bar.add_cascade(label="Options", menu=menu_options)

# Menu Aide
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="Règles du jeu", command=show_rules)
menu_bar.add_cascade(label="Aide", menu=menu_help)

# Conteneur principal
main_frame = tk.Frame(window)
main_frame.pack(expand=True, padx=20, pady=20)

# Titre
label_title = tk.Label(main_frame, text="Tic Tac Toe", font=("Arial", 24, "bold"))
label_title.grid(row=0, column=0, columnspan=3)

# Entrée des noms des joueurs
label_name1 = tk.Label(main_frame, text="Nom Joueur 1:", font=("Arial", 16))
label_name1.grid(row=1, column=0, sticky="E")
entry_name1 = tk.Entry(main_frame, font=("Arial", 16))
entry_name1.grid(row=1, column=1, padx=10, sticky="W")

label_name2 = tk.Label(main_frame, text="Nom Joueur 2:", font=("Arial", 16))
label_name2.grid(row=2, column=0, sticky="E")
entry_name2 = tk.Entry(main_frame, font=("Arial", 16))
entry_name2.grid(row=2, column=1, padx=10, sticky="W")

# Bouton Jouer
button_play = tk.Button(main_frame, text="Jouer", font=("Arial", 16), command=play)
button_play.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
