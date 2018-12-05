'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 7.3 (dict)
 Maak een dictionary aan met cijfers voor een cursus. De studentnamen zijn de
 sleutels en de cijfers zijn de waarden in de dictionary. Zorg dat er minimaal
 8 cijfers in de dictionary staan. Schrijf vervolgens code om op basis van die
 dictionary alle cijfers (met naam) boven een 9,0 te printen.

'''

studenten = {
    'Donny van Walsem':  [5, 6, 9],
    'Lesley Oudshoorn':  [7, 8, 9],
    'Yannick Thomassen': [9, 8, 10]
}

for student, cijfers in studenten.items():
    cijfersBovenNegen = []
    for cijfer in cijfers:
        if cijfer >= 9:
            cijfersBovenNegen.append(cijfer)
    print('{0:17} {1}'.format(student,cijfersBovenNegen))
