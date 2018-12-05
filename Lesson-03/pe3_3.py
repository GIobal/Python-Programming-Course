'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures (Perkovic - §3.2)

 Practice Exercise 3.3 (if-else)
 Pas de uitwerking van exercise 3.2 aan en geef ook een melding als de gebruiker
 niet mag stemmen!

'''

leeftijd = input('Geef je leeftijd: ')

heeftNederlandsPaspoort = input('Nederlands paspoort: ')

if int(leeftijd) >= 18 and heeftNederlandsPaspoort.lower() == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Jammer, je mag nog niet stemmen.')