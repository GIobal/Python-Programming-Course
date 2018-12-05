'''

 Introduction To Computing Using Python (Werkboek)

 Execution Control Structures (Perkovic – §5.1 t/m 5.3)

 Practice Exercise 6.3 (lists)
 Gegeven is variable invoer = "5-9-7-1-7-8-3-2-4-8-7-9". Schrijf een nieuw
 programma waarin je deze variabele splitst in een lijst van getallen en print
 de gesorteerde lijst. Bepaal en print na het opsplitsen de grootste waarde,
 kleinste waarde, aantal getallen, de som en het gemiddelde!

'''

invoer = "5-9-7-1-7-8-3-2-4-8-7-9"

getallen = list(map(int, invoer.split('-'))) # Zet strings gelijk om naar ints.
getallen.sort()

grootste = max(getallen)

kleinste = min(getallen)

aantal = len(getallen)

som = sum(getallen)

gemiddelde = sum(getallen) / len(getallen)

print('''Gesoorteerde lijst van ints: {}
Grootste getal: {} en Kleinste getal: {}
Aantal getallen: {} en Som van de getallen: {}
Gemiddelde: {}
'''.format(getallen, grootste, kleinste, aantal, som, gemiddelde))