import random
import string

chars =  "  " + string.punctuation + string.digits + string.ascii_letters

chars =  list(chars)
cle = chars.copy()

random.shuffle(cle)

#print(f"chars : {chars}")
#print(f"cle : {cle}")
########################ENCRYPTION##############################################33
texte_entree = input("Entrée un texte ")
texte_chiffre = ""

for letter in texte_entree:
    index = chars.index(letter)#on prend la position des lettre dans la liste chars
    texte_chiffre += cle[index]#on prend l'élement dans la mm position dans liste cle

print(f"message original  : {texte_entree}")
print(f"message original  : {texte_chiffre}")

####################DECRIPTION################################
texte_chiffreB = input("Entrée un texte crypte ")
texte_sortie = ""

for letter in texte_chiffreB:
    index = cle.index(letter)#on prend la position des lettre dans la liste chars
    texte_sortie += chars[index]#on prend l'élement dans la mm position dans liste cle

print(f"message original  : {texte_chiffreB}")
print(f"message original  : {texte_sortie}")
