livres = []
nombres_livres = str(input("Quels livres as-tu acheté ce dernier mois ?"))
nb_livres = nombres_livres.split()
livres.append(nb_livres)
print(len(nb_livres))
nbre_livre = len(nb_livres)
print(f"Tu as acheté {nbre_livre} livres ce mois-ci !")