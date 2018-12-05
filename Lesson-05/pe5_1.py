'''

 Introduction To Computing Using Python (Werkboek)

 Strings, Text Data, and File I/O (Perkovic – §4.1 t/m 4.3)

 Practice Exercise 5.1 (formatting)
 Schrijf een functie convert() waar je een temperatuur in graden Celsius (als
 parameter van deze functie) kunt omzetten naar graden Fahrenheit. Je kunt de
 temperatuur in Fahrenheit berekenen met de Formule T(°F) = T(°C) × 1.8 + 32.
 Dus 25 °C = 25 * 1.8 + 32 = 77 °F.

'''

def convert(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

print(convert(25)) # 77.0

'''
 Schrijf nu ook een tweede functie table() waarin je met een for-loop van -30°C
 t/m 40°C in stappen van 10 graden de temperatuur in Fahrenheit print. Zorg
 middels een geformatteerde output voor dezelfde precisie en uitleining als het
 voorbeeld hieronder:
'''

def table():
    print('{0:>3}{1:>9}'.format('F', 'C'))
    for i in range(-30, 50, 10):
        print('{0:>5}{1:>9}'.format(str(convert(i)), str(float(i))))

table()