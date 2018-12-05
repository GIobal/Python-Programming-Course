'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 10.1 (XML-bestanden schrijven)
 In Practice Exercise 9_4 heb je een CSV bestand aangemaakt van deze producten:
 Maak nu met een teksteditor en op basis van deze tabel, een XML-bestand dat
 er zo uitziet:

 Uitvoer:
    <?xml version="1.0" encoding="UTF-8"?>
    <artikelen>
        <artikel nummer="121">
            <code>ABC123</code>
            <naam>Highlight pen></naam>
            <voorraad>231</voorraad>
            <prijs>0.56</prijs>
        </artikel>
        ...
    </artikelen>

 Installeer nu ook de module 'xmltodict'. File > Settings > Zoek op
 'interpreter' en klik op 'Project Interpreter'. Klik rechts in het scherm op
 het plusje. Zoek nu op 'xmltodict' en installeer het package.

 Schrijf een programma waarmee je het XML-bestand inleest en alle artikel-
 namen onder elkaar print!

'''
import xmltodict

with open('artikelen.xml') as file:
    document = xmltodict.parse(file.read())
    for artikel in document['artikelen']['artikel']:
        print(artikel['naam'])