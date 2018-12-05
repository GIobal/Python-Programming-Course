'''

 Introduction To Computing Using Python (Werkboek)

 Containers (Sets and Chars) (Perkovic – §6.2 t/m 6.4)

 Practice Exercise 8.1 (sets)
 Hieronder staat een afbeelding van een tweetal trajecten (bruin en groen). Zet
 beide trajecten allebei in een set met de namen "bruin" en "groen"...

 Print daarna eerst met een set-functie welke plaatsen in beide trajecten worden
 aangedaan (de overeenkomst).

 Gebruik vervolgens opnieuw een set functie om te printen hoe het traject
 "bruin" verschilt van het traject "groen". Je moet dan dus op het scherm zien
 welke plaatsen van traject "bruin" ze niet allebei aandoen!

 Print ook alle stations op beide trajecten uit. Print elk station maar 1!
 Gebruik weer een set-functie!

'''

bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout',
         'Helmond', 'Helmond Brouwhuis', 'Deurne'}

groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze',
         'Weert'}

# Komen in beiden voor:
print(bruin.intersection(groen)) # {'Eindhoven', 'Beukenlaan', 'Boxtel', 'Best'}

# Verschilt:
print(bruin.difference(groen)) # {"Helmont 't Hout", 'Helmond', 'Deurne'
                               # 'Helmond Brouwhuis'}

# Alle stations op beide trajecten:
print(bruin | groen)