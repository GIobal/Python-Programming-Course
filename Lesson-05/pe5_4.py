'''

 Introduction To Computing Using Python (Werkboek)

 Strings, Text Data, and File I/O (Perkovic – §4.1 t/m 4.3)

 Practice Exercise 5.4 (files schrijven)
 Bij een marathonwedstrijd worden bij een controlepost ale voorbijkomende
 hardlopers genoteerd. De gegevens van elke hardloper worden in het bestand
 hardlopers.txt opgeslagen. Schrijf een programma waarmee een tekstbestand
 wordt aangemaakt (als het bestand nog niet bestaat) of aangevuld (gebruik de
 append-mode) met de gegevens van één hardloper (inlezen van toetsenbord).

 Let op: je zult je programma in deze opdracht steeds opnieuw moeten uitvoeren
 voor elke nieuwe hardloper. Om dit te voorkomen zou je een while-loop kunnen
 gebruiker, maar die behandelen we pas volgende les. Je kunt er natuurlijk voor
 kiezen om daar alvast naar te kijken (niet verplicht).

'''
from datetime import datetime

file = open('hardlopers.txt', 'a+')

hardloper = input('Naam hardloper: ')
tijd = datetime.strftime(datetime.now(), '%a%e %b %G, %H:%M:%S')

file.write(tijd + ', ' + hardloper + '\n')
file.close()