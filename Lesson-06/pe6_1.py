'''

 Introduction To Computing Using Python (Werkboek)

 Execution Control Structures (Perkovic – §5.1 t/m 5.3)

 Practice Exercise 6.1 (decision control)
 Schrijf een functie seizoen(maand) die als parameter/maandnummer meekrijgt. Het
 functie-resultaat is het seizoen die bij die maand hoort. Nummers 3 t/m 5
 horen bij lente, 9 t/m 11 'herfst' etc.

'''

def seizoen(maand):
    if maand in (3, 4, 5):
        return 'lente'
    elif maand in (6, 7, 8):
       return 'zomer'
    elif maand in (9, 10, 11):
        return 'herfst'
    elif maand in (1, 2, 12):
        return 'winter'

print(seizoen(10))