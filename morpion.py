from tkinter import *
import random

def prochain_tour(ligne, colonne):

    global joueur

    if boutons[ligne][colonne]['text'] == "" and verifier_gagnant() is False:

        if joueur == joueurs[0]:

            boutons[ligne][colonne]['text'] = joueur

            if verifier_gagnant() is False:
                joueur = joueurs[1]
                label.config(text=(joueurs[1] + " à toi de jouer"))

            elif verifier_gagnant() is True:
                label.config(text=(joueurs[0] + " gagne"))

            elif verifier_gagnant() == "Égalité":
                label.config(text="Égalité !")

        else:

            boutons[ligne][colonne]['text'] = joueur

            if verifier_gagnant() is False:
                joueur = joueurs[0]
                label.config(text=(joueurs[0] + " à toi de jouer"))

            elif verifier_gagnant() is True:
                label.config(text=(joueurs[1] + " gagne"))

            elif verifier_gagnant() == "Égalité":
                label.config(text="Égalité !")


def verifier_gagnant():

    for ligne in range(3):
        if boutons[ligne][0]['text'] == boutons[ligne][1]['text'] == boutons[ligne][2]['text'] != "":
            boutons[ligne][0].config(bg="green")
            boutons[ligne][1].config(bg="green")
            boutons[ligne][2].config(bg="green")
            return True

    for colonne in range(3):
        if boutons[0][colonne]['text'] == boutons[1][colonne]['text'] == boutons[2][colonne]['text'] != "":
            boutons[0][colonne].config(bg="green")
            boutons[1][colonne].config(bg="green")
            boutons[2][colonne].config(bg="green")
            return True

    if boutons[0][0]['text'] == boutons[1][1]['text'] == boutons[2][2]['text'] != "":
        boutons[0][0].config(bg="green")
        boutons[1][1].config(bg="green")
        boutons[2][2].config(bg="green")
        return True

    elif boutons[0][2]['text'] == boutons[1][1]['text'] == boutons[2][0]['text'] != "":
        boutons[0][2].config(bg="green")
        boutons[1][1].config(bg="green")
        boutons[2][0].config(bg="green")
        return True

    elif espaces_vides() is False:

        for ligne in range(3):
            for colonne in range(3):
                boutons[ligne][colonne].config(bg="yellow")
        return "Égalité"

    else:
        return False


def espaces_vides():

    espaces = 9

    for ligne in range(3):
        for colonne in range(3):
            if boutons[ligne][colonne]['text'] != "":
                espaces -= 1

    if espaces == 0:
        return False
    else:
        return True


def nouvelle_partie():

    global joueur

    joueur = random.choice(joueurs)

    label.config(text=joueur + " à toi de jouer")

    for ligne in range(3):
        for colonne in range(3):
            boutons[ligne][colonne].config(text="", bg="#F0F0F0")


fenetre = Tk()
fenetre.title("Tic-Tac-Toe")
joueurs = ["x", "o"]
joueur = random.choice(joueurs)
boutons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=joueur + " à toi de jouer", font=('consolas', 40))
label.pack(side="top")

bouton_reset = Button(text="redémarrer", font=('consolas', 20), command=nouvelle_partie)
bouton_reset.pack(side="top")

cadre = Frame(fenetre)
cadre.pack()

for ligne in range(3):
    for colonne in range(3):
        boutons[ligne][colonne] = Button(cadre, text="", font=('consolas', 40), width=5, height=2,
                                         command=lambda ligne=ligne, colonne=colonne: prochain_tour(ligne, colonne))
        boutons[ligne][colonne].grid(row=ligne, column=colonne)

fenetre.mainloop()
