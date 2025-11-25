print("Quel type de valeur veux-tu convertir ?")

code = []

#Menu principal
choix1 = input("1) Temps / 2) Distance / 3) Temperature / " \
            "4) Poids, Masse, 5) Volumes / 6) Vitesse / " \
            "7) Informatique / 8) Energie").strip()
code.append(choix1)

dictionnaire_conversion = {
    "1A" : ("minutes", "secondes"), "1B" : ("heures", "minutes"), "1C" : ("jours", "heures"),
    "2A" : ("kilomètres", "miles"), "2B" : ("mètres", "centimètres"), "2C" : ("centimètres", "pouces"),
    "3A" : ("Celsius", "Fahrenheit"), "3B" : ("Celsius", "Kelvin"),
    "4A" : ("kilogrammes", "grammes"), "4B" : ("kilogrammes", "livres"),
    "5A" : ("litres", "millilitres"), "5B" : ("litres", "gallons"),
    "6A" : ("km/h", "m/s"), "6B" : ("mph", "km/h"),
    "7A" : ("bits", "octets"), "7B" : ("kilo-octets", "mega-octets"), "7C" : ("giga-octets", "tera-octets"),
    "8A" : ("joules", "calories"), "8B" : ("kWh", "joules"),
}


if choix1 == "1" : 
    choix2 = input("A) Minutes/Secondes, B) Heures/Minutes, C) Jours/Heures").strip().upper()
    code.append(choix2)
elif choix1 == "2" : 
    choix2 = input("A) Kilometres/Miles, B) Metres/Centimetres, C) Centimetres/Pouces").strip().upper()
    code.append(choix2)
elif choix1 == "3" :
    choix2 = input("A) Celsius/Fahrenheit, B) Celsius/Kelvin").strip().upper()
    code.append(choix2)
elif choix1 == "4" :
    choix2 = input("A) Kilogrammes/Grammes, B) Kilogrammes/Livres").strip().upper()
    code.append(choix2)
elif choix1 == "5" :
    choix2 = input("A) Litres/Millilitres, B) Litres/Gallons").strip().upper()
    code.append(choix2)
elif choix1 == "6" :
    choix2 = input("A) km/h - m/s, B) mph - km/h").strip().upper()
    code.append(choix2)
elif choix1 == "7" :
    choix2 = input("A) Bits/Octets, B) Kilo-octets/Mega-octets, C) Giga-octets/Téra-octets").strip().upper()
    code.append(choix2)
elif choix1 == "8" :
    choix2 = input("A) Joules/Calories, B) kWh/Joules").strip().upper()
    code.append(choix2)
else : 
    print("Choix invalide")

code_partiel = "".join(code)
uniteA, uniteB = dictionnaire_conversion[code_partiel]
choix3 = input(f"Veux-tu convertir des {uniteA} en {uniteB} (a) ou l'inverse (b) ?").strip().lower()
code.append(choix3)

