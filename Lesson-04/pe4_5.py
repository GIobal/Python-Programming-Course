'''

 Introduction To Computing Using Python (Werkboek)

 Functions (Perkovic - §3.3 t/m §3.5)

 Practice Exercise 4.5 (functie met list-parameter en for-loop)
 Schrijf (en test) de functie kwadraten_som() die 1 parameter heeft:
 grondgetallen. Dit is een list met integers. De return-waarde van de functie
 is de som van de kwadraten van alle positieve getallen in de lijst! Een lijst
 van [4, 5, 3, -81] heeft als return waarde dus 50 (16 + 9 + 25)

'''

def kwadraten_som(grondgetallen):
    ''' Returns sum of squared positive numbers in given parameter. '''
    positief = []
    for getal in grondgetallen:
        if getal > 0:
            positief.append(getal ** 2)
    return sum(positief)

antwoord = kwadraten_som([4, 5, 3, -81])
print(antwoord)