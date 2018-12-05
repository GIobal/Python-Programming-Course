'''

 Introduction To Computing Using Python (Werkboek)

 Basisconcepten (Perkovic - §2.3 t/m §3.1)

 Practice Exercise 2.2 (getallen, strings en conversie)
 De Hogeschool Utrecht wil studenten financieel ondersteunen bij hun studie,
 afhankelijk van de cijfers die een student haalt. Voor elk cijferpunt krijg je
 €30,-. Voor een 1,0 krijg je dus 30 euro, voor een 2,5 krijg je 75 euro en voor
 een 10,- beloont de HU een student met €300,-.

 Maak variabelen cijferICOR, cijferPROG en cijferCSN. Geef ze alle drie de
 waarde die jij verwacht dat je voor de betreffende vakken in blok 1 zult gaan
 halen. Maak nu vervolgens ook de volgende variabelen aan, en bereken de
 bijbehorende waarden m.b.v. een Python expressie:

    gemiddelde      het gemiddelde van de variabelen cijferICOR, cijferPROG en
                    cijferCSN.
    beloning        de totale beloning voor deze drie cursussen.
    overzicht       een string met een tekstuele omschrijving het gemiddelde en
                    de beloning:

                    'Mijn cijfers (gemiddeld een 7.5) leveren een beloning van
                    €675.0 op!'

 Print tot slot variabele overzicht! Schrijf dit programma in een nieuw bestand,
 bijvoorbeeld pe2_2.py

'''

cijferICOR, cijferPROG, cijferCSN = 7, 9, 7

# Gemiddelde.
gemiddelde = round((cijferICOR + cijferPROG + cijferCSN) / 3, 1)
print(gemiddelde)

# Beloning.
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30

# Overzicht.
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een' \
            ' beloning van €' + str(format(beloning, ',.2f')) + ' op!'
print(overzicht)
