'''

 Introduction To Computing Using Python (Werkboek)

 Functions (Perkovic - §3.3 t/m §3.5)

 Practice Exercise 4.2 (functie met list-parameter)
 Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst. Ga
 ervan uit dat dit een list is met integers. De return-waarde van de functie
 moet de som (optelling) van de getallen in de lijst zijn! Tip: bekijk nog eens
 de list-functies (Perkovic, blz. 28).

'''


def som(getallenLijst):
    ''' Return the sum of given list parameter '''
    return sum(getallenLijst)

antwoord = som([1, 2, 3])
print(antwoord) # 6