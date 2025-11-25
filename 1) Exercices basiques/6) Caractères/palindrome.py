mot = []
choix = input("Donne le mot de ton choix.")
for i in choix : 
    print(i)
    mot.append(i)
mot2 = mot.copy()
mot2.reverse()
if mot == mot2 : 
    print("C'est un palindrome.")
else : 
    print("Ce n'est pas un palindrome.")