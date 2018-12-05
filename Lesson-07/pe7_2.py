'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 7.2 (while-loop)
 Schrijf een nieuw programma waarin de gebruiker een woord moet invoeren. Dit
 woord moet uit vier letters bestaan. Is dat niet zo, dan wordt een foutmelding
 getoond en moet de gebruiker opnieuw een woord invoeren, net zolang totdat er
 een woord is ingevoerd dat uit vier letters bestaat. Dan eindigt het
 programma. Gebruik in ieder geval een while-loop, gecombineerd met het break-
 statement!

'''

while(True):
    woord = input('Geef een string van vier letters: ')
    if(len(woord) == 4):
        print('\nInlezen van correcte string: {} is geslaagd'.format(woord))
        break
    else:
        print('{} heeft {} letters'.format(woord, len(woord)))