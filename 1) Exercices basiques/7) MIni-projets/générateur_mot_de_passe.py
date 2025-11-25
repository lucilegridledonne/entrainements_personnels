import random
import string

mot_de_passe = []
nb_tour = int(input("Combien de chiffres et de lettres veux-tu dans ton mot de passe ?"))

def creer_mdp() : 
    i = 0 
    for i in range(nb_tour) : 
        nombre = random.randint(0, 10)
        mot_de_passe.append(nombre)
    i = 0 
    for i in range(nb_tour) : 
        lettre = random.choice(string.ascii_letters)
        mot_de_passe.append(lettre)
    random.shuffle(mot_de_passe)
    return mot_de_passe

mot_de_passe = creer_mdp()

print(mot_de_passe)