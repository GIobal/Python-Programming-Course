'''

 Introduction To Computing Using Python (Werkboek)

 Containers (Sets and Chars) (Perkovic – §6.2 t/m 6.4)

 Practice Exercise 8.3 (ascii)
 Als extra beveliging wil de NS op haar E-ticket nog een unieke code afbeelden.
 Er is gekozen voor een hele eenvoudige beveliging: Neem de naam van de
 gebruiker+beginstation+eindstation, vertaal elk karakter naar ASCII en maak
 die waarde 3 groter. De "a" wordt dus een "b", de "b" wordt een "e", etc.
 De "A" wordt een "D", de "W" wordt een "Z", etc. En de spatie "" wordt een "#".

 Zorg ervoor dat je code maakt die deze uitvoer maakt op basis van de invoer van
 de gebruiker. Schrijf een functie def code(invoerstring): die ieder teken van
 invoerstring omzet naar zijn rangordenummer met bibliotheekfunctie ord, en -
 na er 3 bij te hebben opgeteled - die int-waarde weer terug vertaalt naar het
 bijbehorende ASCII-teken met bibliotheekfunctie chr().

    Voorbeeld: code("RutteAlkmaarDen Helder") levert op UxwwhDonpdduGhq#Khoghu

'''

def code(invoerstring):
    asciiCode = ''
    for karakter in invoerstring:
        asciiCode += chr(ord(karakter) + 3)
    return asciiCode

gebruiker = input('Gebruikersnaam: ')

beginstation = input('Bij welk station begint de reis: ')

eindstation = input('Bij welk station eindigt de reis: ')

asciiCode = code(gebruiker+beginstation+eindstation)
print(asciiCode) # "RutteAlkmaarDen Helder" = UxwwhDonpdduGhq#Khoghu