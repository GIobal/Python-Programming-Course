'''

 Introduction To Computing Using Python (Werkboek)

 Starten met Python (Perkovic - §1.1 t/m §2.3)

 Practice Exercise 1.4 (boolean expressions)
 Schrijf booleaanse expressies die van de variabelen van Practice Exercise 1_3
 evalueren of:

'''

# 1. 6.75 groter is dan a en kleiner dan b.
a = 6
b = 7

c = 6.75 > a and 6.75 < b
print(c) # True

# 2. De lengte van inventaris meer dan 5 keer zo groot is als de lengte van
# van variabele mijnnaam.
inventaris = ['papier', 'nietjes', 'pennen']

voornaam = 'Yannick'
achternaam = 'Thomassen'

mijnnaam = voornaam + ' ' + achternaam

d = len(inventaris) > len(mijnnaam) * 5
print(d) # False

# 3. De lijst inventaris leeg is, of juist meer dan 10 items bevat.
e = len(inventaris) == 0 or len(inventaris) > 10
print(e) # False