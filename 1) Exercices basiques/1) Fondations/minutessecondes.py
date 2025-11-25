reponse = int(input("Veux-tu convertir 1) les minutes en secondes ou 2) les secondes en minutes ?"))

if reponse == 1 : 
    temps = int(input("Donne les minutes que tu veux convertir"))
    resultat = temps * 60
    print (f"Cela fait {resultat} secondes !")
else : 
    temps = int(input("Donne les secondes que tu veux convertir"))
    resultat = temps / 60
    print (f"Cela fait {resultat} minutes !")
