'''

 Introduction To Computing Using Python (Werkboek)

 Catching Exceptions, CSV-files (Perkovic – §4.4 & §7.3)

 Practice Exercise 9.4 (CSV-files met headers)
 De onderstaande tabel bevat de gegevens van een aantal producten.

 Stap 1: Maak (met Python) een CSV-bestand met bovenstaande gegevens
         (inclusief headers).
 Stap 2: Lees vervolgens het bestand met een Python programma weer in en print
         1.) de naam en prijs van het duurste product.
         2.) het artikelnummer en de voorraad van het artikel met de kleinste
             voorraad en
         3.) het totaalaantal producten in voorraad!

 Uitvoer:
    Het duurste artikel is Monitorstandaard en die kost 32.50 Euro
    Er zijn slechts 34 exemplaren in voorraad van het product met nummer 128
    In totaal hebben wij 1073 producten in ons magazijn liggen

'''

headers = ['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs']
artikelen = {
    ('121', 'ABC123', 'Highlight pen', '231', '0.56'),
    ('123','PQR678', 'Nietmachine', '587', '9.99'),
    ('128','ZYX163', 'Bureaulamp', '34', '19.95'),
    ('137','MLK709', 'Monitorstandaard', '66', '32.50'),
    ('271','TRS665', 'Ipad hoes', '155', '19.00')
}

with open('artikelen.csv', 'w') as file:
    file.truncate()
    file.write(';'.join(headers))
    file.write('\n')
    for artikel in artikelen:
        file.write(';'.join(artikel))
        file.write('\n')
    file.close()

with open('artikelen.csv', 'r') as file:
    file.readline() # Skip headers
    content = file.readlines()
    artikelen = []
    voorraden = []
    for line in content:
        nummer, code, naam, voorraad, prijs = line.rstrip().split(';')
        artikelen.append((int(nummer), code, naam, int(voorraad), float(prijs)))
        voorraden.append(int(voorraad))
    # Duurste.
    duursteArtikel = sorted(artikelen, key=lambda x: x[4])[-1]
    print('Het duurste artikel is {} en die kost '
          '{} Euro'.format(duursteArtikel[2], duursteArtikel[4]))
    # Kleinste voorraad.
    kleinsteVoorraad = sorted(artikelen, key=lambda x: x[3])[0]
    print('Er zijn slechts {} exemplaren in voorraad van het product '
          'met nummer {}'.format(kleinsteVoorraad[3], kleinsteVoorraad[0]))
    # Totaal aantal producten.
    aantal = sum(voorraden)
    print('In totaal hebben wij {} producten in ons magazijn '
          'liggen'.format(aantal))
    file.close()