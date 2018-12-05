'''

 Introduction To Computing Using Python (Werkboek)

 Basisconcepten (Perkovic - §2.3 t/m §3.1)

 Practice Exercise 2.3 (operator voorrang)
 Voeg haakjes toe aan de volgende expressies zodat ze naar True evalueren.
 Print het resultaat! Schrijf dit programma in een nieuw bestand, bijvoorbeeld
 pe2_3.py. Doe dit vanaf nu bij elke opdracht!

'''

# 1. 0 == 1 == 2
a = 0 == (1 == 2)
print(a)

# 2. 2 + 3 == 4 + 5 == 7
b = (2 + (3 == 4) + 5) == 7
print(b)

# 3. 1 < -1 == 3 > 4
c = (1 < -1) == (3 > 4)
print(c)