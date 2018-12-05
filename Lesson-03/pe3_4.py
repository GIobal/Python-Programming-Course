'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures (Perkovic - §3.2)

 Practice Exercise 3.4 (for + if)
 Schrijf een for-loop die over een lijst met strings itereert, en van elk woord
 de eerste twee karakters print. De lijst ['maandag', 'dinsdag', 'woensdag']
 zou dus moeten resulteren in:

 ma
 di
 wo

'''

dagen = ['maandag', 'dinsdag', 'woensdag']

for dag in dagen:
    print(dag[:2])
