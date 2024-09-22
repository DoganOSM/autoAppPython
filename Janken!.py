import random

victoire_joueur= 0
w_pc = 0
egalite= 0
choix = ["pierre","feuille","ciseau"]

while True:
    janken_joueur = input(" Tape Pierre/Feuille/Ciseau ou q pour quitter : \n    ").lower()
    if janken_joueur == "q":
        break
    if janken_joueur not in choix:
        continue#envoi au debut de la boucle
    nbr_rand = random.randint(0,2)# de zero a 2 donc 0,1,2 -> pierre 0 feuille 1 ciseau 2
    choix_pc = choix[nbr_rand]#le choix correspond au numero des element de la liste

    print("Le PC joue ", choix_pc, "!")

    if janken_joueur == "pierre" and choix_pc == "ciseau":
        print("Victoire!")
        victoire_joueur += 1

    elif janken_joueur == "feuille" and choix_pc == "pierre":
        print("Victoire!")
        victoire_joueur += 1

    elif janken_joueur == "ciseau" and choix_pc == "feuille":
        print("Victoire!")
        victoire_joueur += 1
    elif janken_joueur == choix_pc:
        print("egalite contre un pc niveau 1 la honte ")
        egalite += 1
    else:
        print("Argh Chaud!")
        w_pc += 1

print("Tu as gagne", victoire_joueur, " fois.")
print("Le pc ", w_pc, " Fois.")
print("Vous Avez fait égalité ",egalite, " fois")
