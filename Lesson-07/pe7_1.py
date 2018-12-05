'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 7.1 (while-loop)
 Schrijf een while-loop die steeds getallen van de gebruiker vraagt tot deze
 0 ingeeft.

'''

getallen = []

vraagOmGetal = True
while(vraagOmGetal):
    getal = int(input('Geef een getal op: '))
    if(getal != 0):
        getallen.append(getal)
    else:
        vraagOmGetal = False
        print('Er zijn {} getallen ingevoerd, '
              'de som is: {}'.format(len(getallen), sum(getallen)))