'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 7.5 (dict)
 Schrijf een functie namen() die de gebruiker steeds opnieuw vraagt om de
 voornaam van een student in de klas. Als de gebruiker een lege tekst invoert,
 stopt het programma en moet van elke naam geprint worden hoevaak de naam
 in de klas voorkomt. Plaats de namen als sluetel (key) in een dict, en hou
 als waarde (value) bij hoe vaak ze zijn voorgekomen. Zie uitvoer op de
 volgende bladzijde!



'''

def namen():
    namen = {}
    while(True):
        naam = input('Volgende naam: ')
        if not naam:
            print(namen)
            for naam, aantal in namen.items():
                if(aantal == 1):
                    print("Er is 1 student met de naam {}".format(naam))
                else:
                    print("Er zijn {} studenten met "
                          "de naam {}".format(aantal, naam))
        else:
            if naam in namen:
                namen[naam] += 1
            else:
                namen[naam] = 1

namen()