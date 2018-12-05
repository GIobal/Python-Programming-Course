'''

 Introduction To Computing Using Python (Werkboek)

 Final Assignment: XML-stationslijsten
 In deze opdracht lees je gegevens uit een XML-bestand. Dit bestand is op de
 volgende bladzijde gegeven. Het bestand kun je overnemen voor je eigen
 programma: en bevat de gegevens van vier stations. Van ieder station is
 staat vermeld:

    - Code
    - Type
    - Namen (Kort, Middel & Lang)
    - Land
    - Synoniemen (niet altijd aanwezig)

 Lees de gegevens uit het bestand en plaats deze in een dict! Laat je programma
 nu achtereenvolgens de onderstaande gegevens afdrukken op het scherm:

    1. Van alle stations de code en het type.
    2. Van alle stations de code en synoniemen (maar alleen als er
       synoniemen zijn).
    3. Van alle stations de code en de lange naam.

 Let op: bij stap 2 mag je de dict met alle synoniemen uitprinten, maar dat kan
 natuurlijk netter. Bij stap 3 is het de bedoeling dat je wel netjes de lange
 naam van een station uit de namen-dict haalt!

 Mogelijke uitvoer:
    Dit zijn de codes en types van de 4 stations:
    HT   - knooppuntIntercitystation
    ALMO - stoptreinstation
    ATN  - stoptreinstation
    ASA  - intercitystation

    Dit zijn alle stations met één of meer synoniemen:
    HT   - OrderedDict([('Synoniem', ["Hertogenbosch ('s), 'Den Bosch'])])

    Dit is de lange naam van elk station:
    HT   - 's-Hertogenbosch
    ALMO - Almere Oostvaarders
    ATN  - Aalten
    ASA  - Amsterdam Amstel

'''
import xmltodict

with open('stations.xml') as file:
    document = xmltodict.parse(file.read())
    # Codes en types van 4 stations.
    print('Dit zijn de codes en types van de 4 stations:')
    for station in document['Stations']['Station']:
        print('{0:4} - {1}'.format(station['Code'], station['Type']))

    # Stations met synoniemen.
    print('\nDit zijn alle stations met één of meer synoniemen:')
    for station in document['Stations']['Station']:
        if(station['Synoniemen']):
            synoniemen = station['Synoniemen']['Synoniem']
            print('{0:4} - {1}'.format(station['Code'], ', '.join(synoniemen)))

    # Lange naam van elk station.
    print('\nDit is de lange naam van elk station:')
    for station in document['Stations']['Station']:
        print('{0:4} - {1}'.format(station['Code'], station['Namen']['Lang']))