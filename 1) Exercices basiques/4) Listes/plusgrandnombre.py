liste = []
liste2 = []

resultat = input("Ecris tous les chiffres que tu veux.")
liste = resultat.split()
for i in liste : 
    i = int(i)
    liste2.append(i)
liste2.sort()
liste2.reverse()
print(liste2)
print(f"Le chiffre le plus haut est le chiffre {liste2[0]}")