print("Bienvenue sur le quizz")

player = input("Participera tu a mon quizz\n o ou n ?\n ")

if player.lower() != "o":
    quit()
#.lower() met tout en miniscule et inversement avec  .upper()
print(" Parfait jouons ;)")
point =  0
reponse = input("qui est le perso principal de dargon ball ?\n ")

if reponse.lower() == "goku":
    print("Bonne réponse (gohan devait etre le personage principal après l'arc cell normalement)")
    point +=1
else:
    print("Mauvaise Réponse revise tes classiques")

reponse = input("De quel manga vien la guilde Fairy Tail ?\n ")

if reponse.lower() == "fairy tail":
    print("Bonne réponse ")
    point += 1
else:
    print("Mauvaise Réponse la consigne donne la reponse...")

reponse = input("Quel est le manga le plus surcoté?\n ")

if reponse.lower() == "snk":
    print("Bonne réponse ")
    point += 1
else:
    print("Mauvaise Réponse c'est mon avis...")


reponse = input("Qui est le plus beau?\n ")

if reponse.lower() == "moi":
    print("Bonne réponse la confiance en sois c'est sa qu'il faut!! ")
    point += 1
else:
    print("Mauvaise Réponse Ai Plus Confience en toi !!")

reponse = input("Qui est le plus fort?\n ")

if reponse.lower() == "TOI":
    print("Bonne réponse ")
    point += 1
else:
    print("Mauvaise Réponse Abuse pas de ta confience en toi mdrr")

print("Tu as "+str(point)+" Point\n Ce qui te fait la note de "+str(point)+"/5! ")

