'''

 Introduction To Computing Using Python (Werkboek)

 Final Assignment: NS-functies

 De NS heeft standaardtarieven voor treinreizen, maar onder sommige omstandig-
 heden krijger reizigers korting. Bijvoorbeeld omdat ze in een bepaalde
 leeftijdscategorie vallen. In deze opdracht maak je twee functies:
 standaardtarief(..) en ritprijs(..). De eerste functie bepaalt het standaard-
 bedrag voor een bepaalde rit. De tweede functie maakt hier gebruik van, maar
 bepaalt zelf ook nog welke kortingen van toepassing zijn en levert als
 return-waarde de definitieve prijs.

'''

'''
 Deel 1
 
 Schrijf functie standaardprijs(afstandKM). Iedere treinrit kost 80 cent per
 kilometer, maar als de rit langer is dan 50 kilometer betaal je een vast bedrag
 van €15,- plus 60 cent per kilometer. Ga bij invoer van negatieve afstanden
 uit van een afstand van 0 kilometer (prijs is dan dus 0 Euro).

'''

def standaardPrijs(afstandKM):
    if afstandKM > 0:
        if afstandKM <= 50:
            return 0.80 * afstandKM
        else:
            return 15 + 0.60 * afstandKM
    return 0.0

'''
 Deel 2
 Schrijf nu ook de functie ritprijs(leeftijd, weekendrit, afstandKM). De
 parameter weekendrit is een boolean die aangeeft of de rit in het weekend
 plaats zal hebben (True) of niet (False). Het eerste wat de functie
 ritprijs moet doen, is het aanroepen van de functie standaardprijs, waarbij
 de afstand in kilometers doorgegeven moet worden, om de standaardprijs voor
 de rit op te vragen. Aan de hand van de return-waarde kan de ritprijs worden
 berekend. De regels zijn als volgt:
 
 Op werkdagen reizen kinderen (onder 12 jaar) en ouderen (65 en ouder) met
 30% korting. In het weekend reist deze groep met 35% korting. De overige
 leeftijdsgroepen reizen betalen de gewone prijs, behalve in het weekend, dan
 reist deze leeftijdsgroep met 40% korting.
'''

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardPrijs(afstandKM)
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            return prijs - prijs * 0.3
        else:
            return prijs - prijs * 0.4
    else:
        if leeftijd < 12 or leeftijd >= 65:
            return prijs - prijs * 0.35
        else:
            return prijs

'''
 Deel 3

 De diverse parameters kunnen voor heel veel verschillende executie-paden
 zorgen. Dat wil zeggen dat de code op heel veel verschillende manieren door-
 lopen kan worden. Verstandig is om je programma in ieder geval op grens-
 waarden te testen. Voor leeftijd test je dan 11, 12, 64 en 65, maar voor
 al die leeftijden ook weer of het een weekendrit is of niet (4x2 = 8
 combinaties). Voor elk van die 8 combinaties kan er ook weer een korte of lange
 treinrit (of een negatieve afstand) ingevoerd worden, wat 8x3 = 24 testpaden
 oplevert. Test jouw methode ritprijs zo goed mogelijk! 
'''

# 1. 11 jaar oud, geen weekendrit, 0 km.
print(ritprijs(11, False, 0)) # 0.0

# 2. 12 jaar oud, geen weekendrit, 0 km.
print(ritprijs(12, False, 0)) # 0.0

#  3. 64 jaar oud, geen weekendrit, 0 km.
print(ritprijs(64, False, 0)) # 0.0

#  4. 65 jaar oud, geen weekendrit, 0 km.
print(ritprijs(65, False, 0)) # 0.0

# 5. 11 jaar oud, weekendrit, 0 km.
print(ritprijs(11, True, 0)) # 0.0

# 6. 12 jaar oud, weekendrit, 0 km.
print(ritprijs(12, True, 0)) # 0.0

# 7. 64 jaar oud, weekendrit, 0 km.
print(ritprijs(64, True, 0)) # 0.0

# 8. 65 jaar oud, weekendrit, 0 km.
print(ritprijs(65, True, 0)) # 0.0

# 9. 11 jaar oud, geen weekendrit, 30 km.
print(ritprijs(11, False, 30)) # 15.6000...1

# 10. 12 jaar oud, geen weekendrit, 30 km.
print(ritprijs(12, False, 30)) # 24.0

# 11. 64 jaar oud, geen weekendrit, 30 km.
print(ritprijs(64, False, 30)) # 24.0

# 12. 65 jaar oud, geen weekendrit, 30 km.
print(ritprijs(65, False, 30)) # 15.6000...1

# 13. 11 jaar oud, weekendrit, 30 km.
print(ritprijs(11, True, 30)) # 16.8

# 14. 12 jaar oud, weekendrit, 30 km.
print(ritprijs(12, True, 30)) # 14.3999...

# 15. 64 jaar oud, weekendrit, 30 km.
print(ritprijs(64, True, 30)) # 14.3999...

# 16. 65 jaar oud, weekendrit, 30 km.
print(ritprijs(65, True, 30)) # 16.8

# 17. 11 jaar oud, geen weekendrit, 50 km.
print(ritprijs(11, False, 50)) # 26.0

# 18. 12 jaar oud, geen weekendrit, 50 km.
print(ritprijs(12, False, 50)) # 40.0

# 19. 64 jaar oud, geen weekendrit, 50 km.
print(ritprijs(64, False, 50)) # 40.0

# 20. 65 jaar oud, geen weekendrit, 50 km.
print(ritprijs(65, False, 50 )) # 26.0

# 21. 11 jaar oud, weekendrit, 50 km.
print(ritprijs(11, True, 50)) # 28.0

# 22. 12 jaar oud, weekendrit, 50 km.
print(ritprijs(12, True, 50)) # 24.0

# 23. 64 jaar oud, weekendrit, 50 km.
print(ritprijs(64, True, 50)) # 24.0

# 24. 65 jaar oud, weekendrit, 50 km.
print(ritprijs(65, True, 50)) # 28.0