dictionnaire_test = {
    "Alice": ("Lyon", "Maths/Physique/Sport"),
    "Ben" : ("Marseille", "Physique/Théâtre"),
    "Charlie" : ("Saint-Etienne", "Anglais/Maths/Allemand")
}

for etudiant in dictionnaire_test.items() : 
    print(etudiant)


for cle, valeur in dictionnaire_test.items() : 
    print("L'étudiant ", cle, "habite à ", valeur, ".")