'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures (Perkovic - §3.2)

 Practice Exercise 3.5 (for + if)
 Schrijf een for-loop die over lijst met getallen itereert, en alle even
 getallen print.

'''

nummers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for nummer in nummers:
    if nummer % 2 == 0:
        print(nummer)
