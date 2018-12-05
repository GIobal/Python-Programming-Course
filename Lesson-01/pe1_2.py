'''

 Introduction To Computing Using Python (Werkboek)

 Starten met Python (Perkovic - §1.1 t/m §2.3)

 Practice Exercise 1.2 (strings)
 Schrijf en evalueer Python expressies die de volgende vragen beantwoorden:

'''

# (a) Hoeveel letters zijn er in 'Supercalifragilisticexpialidocious' ?
a = len('Supercalifragilisticexpialidocious')
print(a) # 34

# (b) Komt in ' Supercalifragilisticexpialidocious' de tekst 'ice' voor?
b = 'ice' in 'Supercalifragilisticexpialidocious'
print(b) # True

# (c) Is het woord 'Antidisestablishmentarianism' langer dan
# 'Honorificabilitudinitatibus' ?
c = 'Antidisestablishmentarianism' > 'Honorificabilitudinitatibus'
print(c) # False

# (d) Welke componist komt in alfabetische volgorde het eerst: 'Berlioz',
# 'Borodin', 'Brian', 'Bartok', 'Bellini' 'Buxtehude', 'Bernstein'? Welke het
# laatst?
componists = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Buxtehude', 'Bernstein']

# Eerste componist in componists in alfabetische volgorde.
first = min(componists)
print(first) # Bartrok

# Laatste componist in componists in alfabetische volgorde.
last = max(componists)
print(last) # Buxtehude