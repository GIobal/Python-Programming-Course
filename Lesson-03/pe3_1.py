'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures (Perkovic - §3.2)

 Practice Exercise 3.1 (if-statement)
 Schrijf een programma dat de gebruiker vraagt om de score van een multiple-
 choice toets. Het programma bepaalt of het resultaat voldoende is. Bij meer
 dan 15 punten is de deelnemer geslaagd!

'''

score = input('Geef je score: ' )

if int(score) > 15:
    print('Gefeliciteerd!\nMet een score van ' + score + ' ben je geslaagd!')

'''
 In het geval dat je de bovenstaande uitvoer programmeerd met 2 print()-
 opdrachten en je plaatst de tweede print()-opdracht niet recht onder de eerste,
 maar bijvoorbeeld onder de i van 'if', dan valt deze opdracht buiten de scope 
 van de if-statement en zal altijd printen ongeacht het antwoord van de 
 gebruiker.
'''