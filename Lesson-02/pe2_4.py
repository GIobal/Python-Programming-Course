'''

 Introduction To Computing Using Python (Werkboek)

 Basisconcepten (Perkovic - §2.3 t/m §3.1)

 Practice Exercise 2.4 (Input/Output)
 Schrijf een programma dat de gebruiker vraagt om zijn uurloon, het aantal uur
 dat hij of zij gewerkt heeft en dat daarna het salaris uitrpint.

'''

uurloon = input('Wat verdien je per uur: ')

aantalUur = input('Hoeveel uur heb je gewerkt: ' )

inkomen = float(uurloon) * int(aantalUur)

uitvoer = str(aantalUur) + ' uur werken levert ' + str(format(inkomen, ',.2f'))\
          + ' Euro op'
print(uitvoer)
