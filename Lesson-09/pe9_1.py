'''

 Introduction To Computing Using Python (Werkboek)

 Catching Exceptions, CSV-files (Perkovic – §4.4 & §7.3)

 Practice Exercise 9.1 (catching exceptions)
 Je reist met een grote groep en hebt een hotel afgehuurd. Dat kost €4356,-.
 Dit is kostbaar, daarom wil je weten hoeveel dit per persoon kost. Schrijf een
 programma dat de gebruiker vraagt om het aantal personen dat mee op reis gaat.
 Deel het bedrag door het aantal reizigers en print dat uit! Gebruik een try-
 except; zorg dat bij foute invoer deze verschillende foutmeldingen geprint
 worden:

    Aantal = 0          - Delen door nul kan niet!
    Aantal = -20        - Negatieve getallen zijn niet toegestaan!
    Aantal = 'twintig'  - Gebruik cijfers voor het invoeren van het aantal!
    Alle andere fouten: - Onjuiste invoer!

'''

try:
    aantalReizigers = int(input('Hoeveel personen gaan er mee op reis? : '))
    if aantalReizigers == 0:
        raise Exception('Delen door nul kan niet!')
    elif aantalReizigers < 0:
        raise Exception('Negatieve getallen zijn niet toegestaan!')
    elif isinstance(aantalReizigers, str):
        raise Exception('Gebruik cijfers voor het invoeren van het aantal!')
except Exception:
    print()
except ValueError:
    print('Onjuiste invoer!')

print('De kosten voor 1 persoon '
      'bedraagt: {0:.2f}'.format(4356 / aantalReizigers))