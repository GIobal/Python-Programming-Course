'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures (Perkovic - §3.2)

 Practice Exercise 3.2 (if met 2 booleaanse operators)
 Je mag stemmen als je 18 jaar of ouder bent en in het bezit bent van een
 Nederlands paspoort. Schrijf een programma dat de leeftijd van de gebruiker
 vraagt en of diegene een Nederlands paspoort heeft (ja/nee). Als aan beide
 voorwaarden is voldaan, print dan dat de gebruiker mag stemmen! Doe dit weer
 in een nieuw bestand, bijvoorbeeld pe3_2.py. In de conditie van een if-
 statement kun je meerdere voorwaarden tegelijk controleren met bijvoorbeeld or
 of and (zie Perkovic blz 18 en 19). Voor deze opgave mag je daarom maximaal
 1 keer een if-statement gebruiken.

'''

leeftijd = input('Geef je leeftijd: ')

heeftNederlandsPaspoort = input('Nederlands paspoort: ')

if int(leeftijd) >= 18 and heeftNederlandsPaspoort.lower() == 'ja':
    print('Gefeliciteerd, je mag stemmen!')