import random



def roue():
    min_valeur = 1
    max_valeur = 6
    roue= random.randint(min_valeur,max_valeur)
    return roue

while True:
    joueur = input("Combien de joeur vont-il jouer au jeu ? (2 à 4) :  ")
    if joueur.isdigit():
        joueur= int(joueur)
        if 2<= joueur <=4:
            break
        else:
            print("le nombre de joueur n'est pas valid")
    else:
        print("Erreur entrée une réponde correct")

max_point = 50
score_joueur = [0 for _ in range(joueur)]

print(score_joueur)

while max(score_joueur) < max_point:

    for id_joueur in range(joueur):
        print("\nLe Tour du joueur ", id_joueur+1 ,"Commence Maintenant\n ")
        print("Ton score totale est de : " , score_joueur[id_joueur])
        score_actu = 0

        while True:
            dois_jouer = input("Veux tu lancer le dee (y) ? ")

            if dois_jouer.lower() != "y":
                break
            valeur = roue()
            if valeur == 1:
                print("Tu as lancer un 1 le tour est fichue pour toi !!!")
                score_actu= 0
                break
            else:
                score_actu += valeur
                print("Vous obtene un :",valeur)
            print("Votre score est :",score_actu)
        score_joueur[id_joueur] += score_actu
        print("Votre score totale est :",score_joueur[id_joueur])

print("Felicitation au joueur ", id_joueur ," Vous avez atteint l'objectif avec un score de ", score_joueur[id_joueur])