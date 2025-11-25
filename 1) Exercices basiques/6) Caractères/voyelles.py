compteur_voyelles = 0
phrase = input("Ecris la phrase de ton choix.")
for i in phrase :
    print(i)
    if i in ["a", "e", "i", "o", "u", "y"] :
        compteur_voyelles += 1
print(compteur_voyelles)