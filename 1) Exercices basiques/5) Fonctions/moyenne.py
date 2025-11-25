def trouver_moyenne(a, b):
    moyenne = (a + b)/2
    return moyenne

chiffre1 = int(input("Donne un premier chiffre"))
chiffre2 = int(input("Donne un autre chiffre"))
moyenne2 = trouver_moyenne(chiffre1, chiffre2)
print(f"La moyenne est de {moyenne2}")