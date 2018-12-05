'''

 Introduction To Computing Using Python (Werkboek)

 Strings, Text Data, and File I/O (Perkovic – §4.1 t/m 4.3)

 Practice Exercise 5.5 (string functions)
 Schrijf functie gemiddelde(), die de gebruiker vraagt om een willekeurige zin
 in te voeren. De functie berekent vervolgens de gemiddelde lengte van de
 woorden in de zin en print dit uit.

'''

zin = input('Voer een willekeurige zin in: ')

woorden = []
for woord in zin.split():
    woorden.append(len(woord))

gemiddelde = float(sum(woorden)) / len(woorden)
print(gemiddelde)
