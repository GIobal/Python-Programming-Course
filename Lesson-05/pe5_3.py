'''

 Introduction To Computing Using Python (Werkboek)

 Strings, Text Data, and File I/O (Perkovic – §4.1 t/m 4.3)

 Practice Exercise 5.3 (files lezen)
 Schrijf een programma dat het bestand kaartnummers.txt opnieuw opent en het
 aantal regels en het grootste kaartnummer in het bestand bepaalt. Print
 deze gegevens vervolgens uit:

'''

file = open('kaartnummers.txt', 'r')
content = file.read()
file.close()

# Aantal regels.
aantalRegels = len(content.splitlines())

# Grootste kaartnummer in bestand.
i = 0
kaartnummers = []
for index, line in enumerate(content.splitlines()):
    kaartnummer, klant = line.split(',')
    kaartnummers.append((kaartnummer, index + 1))
grootsteKaartnummer = max(kaartnummers)[0]
opRegel = max(kaartnummers)[1]

print('Deze file telt {} regels.\nHet grootste kaartnummer is: {} en dat staat '
      'op regel {}'.format(aantalRegels, grootsteKaartnummer, opRegel))

