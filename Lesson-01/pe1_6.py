'''

 Introduction To Computing Using Python (Werkboek)

 Starten met Python (Perkovic - §1.1 t/m §2.3)

 Practice Exercise 1.6 (lists)
 Het bereik van een lijst is het verschil tussen de grootste en het kleinste
 getal. Schrijf een Python expressie die het bereik van een lijst berekent. Als
 bijvoorbeeld variabele list bestaat uit de getallen 4, 7, -2, en 12, dan moet
 de expressie evalueren naar 14 (verschil tussen 12 en -2). Zorg dat de
 expressie altijd werkt, ook al bestaat de lijst uit andere waarden!

'''

numbers = [4, 7, -2, 12]

a = abs(min(numbers) - max(numbers))
print(a) # 14