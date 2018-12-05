'''

 Introduction To Computing Using Python (Werkboek)

 Catching Exceptions, CSV-files (Perkovic – §4.4 & §7.3)

 Practice Exercise 9.2 (CSV-files schrijven)
 Met onderstaande code worden de gegevens van iedereen vastgelegd die wil
 inloggen in een overheidssysteem. Voorletters, achternaam, geboortedatum en
 e-mailadres worden ingelezen via de console en weggeschreven naar een CSV-
 bestand, voorafgegaan door de huidige datum en tijd. Van meerdere personen
 moeten deze gegevens ingelezen kunnen worden en weggeschreven naar het CSV-
 bestand. Het programma stop na intikken van de naam 'einde'. Maak het
 programma af:

 Een mogelijke uitvoer zou dan worden:
    Wat is je achternaam:    van Oranje
    Wat zijn je voorletters: W.A.
    Wat is je geboortedatum: 27-04-1967
    Wat is je e-mail adres:  willem@nederland.nl

 Het CSV-bestand ziet er hierna zo uit:
 Tue 03 May 2016 at 12:06;W.A.;van Oranje;27-04-1967;willem@nederland.nl

'''
from datetime import datetime
import csv

bestand = 'inloggers.csv'

with open('inloggers.csv', 'w') as file:
    while(True):
        naam = input("Wat is je achternaam? ")
        if(naam == 'einde'):
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        tijdstip = datetime.strftime(datetime.now(), '%a %d %b %G at %H:%M')
        text = [tijdstip, voorl, naam, gbdatum, email]
        file.write(';'.join(text))
        file.write('\n')

