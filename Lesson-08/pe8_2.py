'''

 Introduction To Computing Using Python (Werkboek)

 Containers (Sets and Chars) (Perkovic – §6.2 t/m 6.4)

 Practice Exercise 8.2 (random)
 Schrijf functie monopolyworp(), die een het gooien van twee dobbelstenen voor
 het spel Monopoly simuleert en afdrukt. Je mag nogmaals gooien als beide stenen
 dezelfde waarde hebben. Zorg dat de functie die worpen ook simuleert! Na
 driemaal dubbel moet de speler naar de gevangenis!

'''
from random import randint

def monopolyworp():
    aantalDezelfdeWaarden = 0
    i = 0
    while(True):
        i += 1
        rol1 = randint(1, 6)
        rol2 = randint(1, 6)
        if(rol1 == rol2):
            print('Dezelfde waarden gegooit op rol: {}, '
                  'namelijk: {}, {}'.format(i, rol1, rol2))
            aantalDezelfdeWaarden += 1
        else:
            aantalDezelfdeWaarden = 0
        if(aantalDezelfdeWaarden == 3):
            print('Driemaal dezelfde waarden gegooit op rol: {}.'.format(i))
            break

monopolyworp()