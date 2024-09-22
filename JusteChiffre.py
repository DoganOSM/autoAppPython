import random
#random.range(0, 100) -> chiffre au hasard de 1 à 100 sans inclure le 100
#
#r = random.randrange(-5,11)#-5 a 10 PAS 11!!
#print(r)

#a l'inverse si on veut avoir 11 inclus
#b = random.randint(-5,11)#-5 a 10 PAS 11!!
#print(b)
joueur= input("Etes vous prêt à tenter de trouver le numéro Gagnant ?\n Oui ou non ?")
if joueur.lower() == ("oui"):
    print(" Bon Courage !")
    plusgrand_nombre = input("Tapez donc le maximum de la fourchette de nombre !")
    if plusgrand_nombre.isdigit():
        plusgrand_nombre = int(plusgrand_nombre)#si le choix du joueur n'est pas un nombre on le transforme en nombre

        if plusgrand_nombre <= 0 :
            print("Prochaine fois un nombre plus grand que zero !!")
            quit()
    else:
        print("Taper un nombre la prochaine fois")
        quit()
    chiffre_a_deviner = random.randint(0,plusgrand_nombre)
    tentative = 0
    while True:
        tentative +=1
        choix_du_j = input(" Il est temps de deviner !\n Votre choix ?")
        if choix_du_j.isdigit():
            choix_du_j = int(choix_du_j)  # si le choix du joueur n'est pas un nombre on le transforme en nombre
        else:
            print("Taper un nombre la prochaine fois")
            continue
        if choix_du_j == chiffre_a_deviner :
            print("Tu est donc l'élu !!! Tu est le goat ")
            break
        elif choix_du_j > chiffre_a_deviner:
            print("C'est moins -_-")
        else:
            print("C'est plus -_-")
print("T'a réussi en",tentative,"tentatives")

