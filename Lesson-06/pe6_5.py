'''

 Introduction To Computing Using Python (Werkboek)

 Execution Control Structures (Perkovic – §5.1 t/m 5.3)

 Practice Exercise 6.5 (nested loop)
 Schrijf een programma met twee for-loops in elkaar (nested) om de tafels van
 1 t/m 10 uit te printen.

'''

for i in range(1, 11):
    for j in range(1,11):
        print(j * i)