import random

choisi = random.randint(0,5)
print("Essaye de deviner quel nombre j'ai choisi entre 0 et 5")
essai = int(input())

while essai != choisi : 
    if essai > choisi : 
        print("Trop haut !")
        essai = int(input())
    elif essai < choisi : 
        print("Trop bas !")
        essai = int(input())          
print("Bien joué !")    
