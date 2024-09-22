nom = input("Tapez votre nom : ")
print("Bienvenue", nom, "dans cette aventure !")

reponse = input(
    "Vous êtes sur un chemin de terre, il se termine et vous pouvez aller à gauche ou à droite. Dans quelle direction voulez-vous aller ? ").lower()

if reponse == "gauche":
    reponse = input(
        "Vous arrivez à une rivière, vous pouvez marcher autour ou nager à travers. Tapez 'marcher' pour contourner et 'nager' pour traverser à la nage : ").lower()

    if reponse == "nager":
        print("Vous avez nagé à travers et avez été mangé par un alligator.")
    elif reponse == "marcher":
        print("Vous avez marché pendant de nombreux kilomètres, vous êtes à court d'eau et vous avez perdu.")
    else:
        print("Option non valide. Vous perdez.")

elif reponse == "droite":
    reponse = input(
        "Vous arrivez à un pont, il a l'air branlant, voulez-vous le traverser ou revenir en arrière (traverser/revenir) ? ").lower()

    if reponse == "revenir":
        print("Vous faites demi-tour et vous perdez.")
    elif reponse == "traverser":
        reponse = input(
            "Vous traversez le pont et rencontrez un étranger. Voulez-vous lui parler (oui/non) ? ").lower()

        if reponse == "oui":
            print("Vous parlez à l'étranger et il vous donne de l'or. Vous GAGNEZ !")
        elif reponse == "non":
            print("Vous ignorez l'étranger, il est offensé et vous perdez.")
        else:
            print("Option non valide. Vous perdez.")
    else:
        print("Option non valide. Vous perdez.")

else:
    print("Option non valide. Vous perdez.")

print("Merci d'avoir essayé", nom)
