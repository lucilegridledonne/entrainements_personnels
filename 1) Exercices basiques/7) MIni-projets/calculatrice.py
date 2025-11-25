
result = 0 
a = int(input("Donne ton premier chiffre"))
b = int(input("Donne ton second chiffre"))

reponse = int(input("Tape 1 pour +, 2 pour -, 3 pour * et 4 pour /"))

if reponse == 1 : 
    result = a + b
elif reponse == 2 : 
    result = a - b 
elif reponse == 3 : 
    result = a * b
elif reponse == 4 : 
    result = a / b 
    print(result)


