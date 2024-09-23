


mdpPrincipale = input("Quel est le mots de passe principale ?")


def voir():
    with open('mptsdepasse.txt','r') as f:
        for line in f.readline():
            data = line.rstrip()
            nom , mdp =data.split("|")
            ''' Si jamais je ne veux pas lires les char tels que "\n" faire -> print(line.rstrip()) 
                data.split retourn une liste separent les élément a partir de la chose en parametre'''
            print("Nom user : " + nom + "Mots de passe user : " + mdp )

def ajouter():
    nom = input("Le nom du compte : ")
    mdp= input("Mots de pass du compte : ")

    with  open('motsdepasse.txt','a') as f:
        f.write(nom +" | "+mdp + "\n")
    '''le mots with permet qu'après l'ouverture le fichier text puisse se refermenrer dirrectement 
    a= append ecrit a la fin du fichier
    w= ecrit sur un nv fichier si il existe deja l'efface et ecrit sur un nv
    r= lire le fichier'''

while True:
    mode = input("Voulez vous ajoutez un mots de passe ou voir ceux existant (voir , ajouter) , appuyer sur q pour quitter")
    if mode == "voir":
        voir()
    if mode == "ajouter":
        ajouter()
    if mode == "q":
        quit()
    else:
        print("erreur dans le mode choisi ")
        continue