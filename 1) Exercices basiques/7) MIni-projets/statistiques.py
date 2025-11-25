
def trouver_maximum(nombre):
    maximum = 0 
    if maximum < nombre : 
        maximum = 0 + nombre
    else : 
        pass
    return maximum


def calculer_la_moyenne() :
    somme = 0 
    reponse = int(input("Combien de notes veux-tu ajouter ?"))
    for i in range(reponse):
        chiffre = int(input("Quel chiffre veux-tu ajouter ?"))
        somme += chiffre
    moyenne = somme / reponse
    return moyenne

choix = int(input("Donne ton nombre "))
reponse = trouver_maximum(choix)
print(f"Le maximum est de {reponse}")

moyenne2 = calculer_la_moyenne()
print(f"La moyenne est de {moyenne2}")