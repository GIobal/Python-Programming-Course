'''

 Introduction To Computing Using Python (Werkboek)

 Execution Control Structures (Perkovic – §5.1 t/m 5.3)

 Practice Exercise 6.4 (two-dimensional-lists)
 Van elke student worden 3 cijfers bijgehouden. In de lijst studentencijfers
 staan de gegevens van 4 studenten. Schrijf code voor twee functies die het
 gemiddelde cijfer voor iedere student en het gemiddelde van alle studenten
 berekent. De eerste functie heeft als return-waarde een één dimensionale-lijst
 met alle gemiddelden per student, en de tweede functie heeft als return-waarde
 een int-getal met het gemiddelde van alle studenten! Maak het onderstaande
 programma af:

'''

studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0 ,0]]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijfers in studentencijfers:
        antw.append(round(sum(cijfers) / len(cijfers)))
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddelde_per_student = []
    for cijfers in studentencijfers:
        gemiddelde_per_student.append(round(sum(cijfers) / len(cijfers)))
    # Na maken van de lijst met gemiddelden per student, kun je opnieuw
    # hier de gemiddelden van uitrekenen.
    antw = round(sum(gemiddelde_per_student) / len(gemiddelde_per_student))
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))