'''

 Introduction To Computing Using Python (Werkboek)

 Final Assignment: NS-kaartautomaat
 In deze opdracht maak je een NS-kaartautomaat. Gegeven is het treintraject
 Schagen - Maastricht:

    Schagen, Heerhugowaard, Alkmaar, Castricum, Zaandam, Amsterdam Sloterdijk,
    Amsterdam Centraal, Amsterdam Amstel, Utrecht Centraal, 's-Hertogenbosch,
    Eindhoven, Weert, Roermond, Sittard, Maastricht.

 De bedoeling is dat je 3 functies schrijft waarmee je 1) het beginstation aan
 een reiziger vraagt, 2) het eindstation aan een reiziger vraagt, en 3) de
 reisgegevens op het scherm print. Jouw functies zouden als volgt gebruikt
 moeten kunnen worden:

    stations = ['Schagen', 'Heerhugowaard', ..., 'Sittard', 'Maastricht']
    beginstation = inlezen_beginstation(stations)
    eindstation = inlezen_eindstation(stations, beginstation)
    omroepen_reis(stations, beginstation, eindstation)

 Een mogelijke uitvoer van deze code (als de functies zijn geschreve), staat
 onderaan de volgende pagina. Op de volgende pagina staat ook een stappenplan
 waarmee je dit programma kunt realiseren.

'''

def inlezen_beginstation(stations):
    while(True):
        station = input('Wat is je beginstation? : ')
        if station in stations:
            return station
    return

def inlezen_eindstation(stations, beginstation):
    while(True):
        station = input('Wat is je eindstation? : ')
        if station in stations:
            if(stations.index(station) > stations.index(beginstation)):
                return station
        print('Deze trein komt niet in {}'.format(station))
    return

def omroepen_reis(stations, beginstation, eindstation):
    beginstationIndex = stations.index(beginstation)
    print('\nHet beginstation {} is het {}e station in het '
          'traject.'.format(beginstation, beginstationIndex + 1))
    eindstationIndex = stations.index(eindstation)
    print('Het eindstation {} is het {}e station in het '
          'traject.'.format(eindstation, eindstationIndex + 1))
    verschil = abs(beginstationIndex - eindstationIndex)
    print('De afstand bedraagt {} station(s).'.format(verschil))
    prijs = verschil * 5
    print('De prijs van het kaartje is {} euro\n'.format(prijs))
    print('Jij stapt in de trein in: {}'.format(beginstation))
    for index, station in enumerate(stations):
        if index > beginstationIndex and index < eindstationIndex:
            print(' - {}'.format(station))
    print('Jij stapt uit in {}'.format(eindstation))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
            'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', '\'-Hertogenbosch', 'Eindhoven', 'Weert',
            'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
