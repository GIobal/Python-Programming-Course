'''

 Introduction To Computing Using Python (Werkboek)

 Functions (Perkovic - §3.3 t/m §3.5)

 Practice Exercise 4.1 (functie met 3 parameters)
 Maak een nieuwe Python file aan voor deze opdracht (vanaf nu is dat standaard
 en zal dat niet steeds meer bij de opdracht staan). Schrijf (en test) de
 functie som() die 3 parameters heeft: getal1, getal2 en getal3. De return-
 waarde van de functie moet de som (optelling) van deze parameters zijn!

'''


def som(getal1, getal2, getal3):
    ''' Return the sum of 3 given integer parameters '''
    return getal1 + getal2 + getal3

antwoord = som(1, 2, 3)
print(antwoord) # 6