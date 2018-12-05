'''

 Introduction To Computing Using Python (Werkboek)

 Strings, Text Data, and File I/O (Perkovic – §4.1 t/m 4.3)

 Practice Exercise 5.2 (files lezen)
 Maak met behulp van PyCharm (of Notepad) het onderstaande bestand
 'kaartnummers.txt', dat bestaat uit klantenkaartnummers en namen. Op iedere
 regel staan de gegevens van 1 kaart:

 325255, Jan Jansen
 334343, Erik Materus
 235434, Ali Ahson
 645345, Eva Versteeg
 534545, Jan de Wilde
 345355, Henk de Vries

 Schrijf een Python programma waarmee je het bestand opent, en splits elke
 regel op de komma en zorg dat de uitvoer (op het scherm) is zoals op de
 volgende pagina is weergegeven! Vergeet niet het bestand te sluiten!

'''

file = open('kaartnummers.txt', 'r')
content = file.read()
file.close()

for line in content.splitlines():
    kaartnummer, klant = line.split(',')
    print('{} heeft kaartnummer: {}'.format(klant, kaartnummer))
