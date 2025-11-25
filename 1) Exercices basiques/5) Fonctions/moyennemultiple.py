def trouver_moyenne():
    choix = int(input("Combien de chiffres veux-tu rentrer ?"))
    total = 0 
    for x in range(choix) : 
        chiffre = int(input("Entre ton chiffre"))
        total = total + chiffre
    moyenne = total/choix
    return moyenne

moyenne = trouver_moyenne()
print(f"La moyenne est de {moyenne}")