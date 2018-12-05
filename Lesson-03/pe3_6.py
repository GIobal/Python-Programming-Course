'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures (Perkovic - §3.2)

 Practice Exercise 3.6 (for + if)
 Schrijf een for-loop die langs alle letters van een string loopt en de letter
 uitprint, maar alleen als het een klinker is ('aeiou'). Gebruik string:
 s = "Guido van Rossum heeft programmeertaal Python bedacht."

'''

s = 'Guido van Rossum heeft programmeertaal Python bedacht.'

for letter in s:
    if letter in 'aeiou':
        print(letter)