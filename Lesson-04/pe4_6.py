'''

 Introduction To Computing Using Python (Werkboek)

 Functions (Perkovic - §3.3 t/m §3.5)

 Practice Exercise 4.6 (functie met (im)mutable parameter)
 Schrijf (en test) functie wijzig() met één parameter: letterlijst. Zorg dat de
 functie de lijst leegt en de letters ['d', 'e', 'f'] toevoegt. Er is geen
 return-waarde! Test je programma als volgt:

 lijst = ['a', 'b', 'c']
 print(lijst)
 wijzig(lijst)
 print(lijst)

'''

lijst = ['a', 'b', 'c']
letterlijst = 'f'

def wijzig(letterlijst):
    lijst.clear()
    lijst.append(letterlijst)

print(lijst)
wijzig(letterlijst)
print(lijst)

# Q: Waarom kun je in de functie niet de opdracht lijst = ['d', 'e', 'f'] geven?
# A: Dit zou een nieuwe variabele lijst aanmaken in de scope van de functie,
#    hierdoor kun je niet meer bij de originele variabele die je moet muteren.

# Q: Werkt jouw functie ook met string-parameter? Probeer dit! Waarom werkt het
#    wel/niet?
# A: Dit werkt wel, omdat de list.append() methode zowel een list als een
#    een string accepteert. Deze plaatst hij dan achter de originele lijst.

# Q: Welke rol speelt (im)mutabiliteit in deze vraag?
# A: In het kader van de eerste vraag, zou variabele lijst, op het moment dat je
#    een nieuwe variabele genaamd 'lijst' in de functie aanmaakt, immutabel
#    worden, omdat de referentie binnen de scope van de functie verloren gaat.
#
#    Je past in dit voorbeeld voor het eerst een variabele aan buiten de scope
#    waar we de vorige lessen mee hebben gewerkt.