def trouver_minimum(a, b) : 
    if a < b : 
        resultat = a
    else : 
        resultat = b
    return resultat

a = int(input("Donne un premier chiffre"))
b = int(input("Donne un autre chiffre"))
reponse = trouver_minimum(a, b)
print(f"{reponse} est le plus petit")