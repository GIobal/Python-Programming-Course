'''

 Introduction To Computing Using Python (Werkboek)

 Final Assignment: Bagagekluizen

 Op veel stations kun je een bagagekluis huren. We willen graag dat jij de
 software realiseert voor deze kluis. Er zijn door de beheerders de volgende
 randvoorwaarden gesteld aan het systeem:

    - Er zijn in totaal 12 kluizen
    - De kluis moet beveiligd zijn met een 4-cijferig wachtwoord.
    - Als de stroom uitvalt mag de data niet verloren gaan en daarom moet je
      een bestand gebruiken voor de opslag van gegevens zoals kluisnummers en
      wachtwoorden.

 De gebruiker moet het onderstaande menu te zien krijgen:

    1: Ik wil een nieuwe kluis
    2: Ik wil mijn kluis openen
    3: Ik geef mijn kluis terug
    4: Ik wil weten hoeveel kluizen nog vrij zijn

 Als je kiest voor "1: Ik wil een nieuwe kluis", dan krijg de gebruiker een
 willekeurige code van 4 cijfers als er nog een kluis beschikbaar is. Deze code
 hoort bij een van de twaalf kluizen. Sla het nummer van de kluis samen met de
 4 cijferige code op 1 regel op in een tekstbestand en geef de code en het
 kluisnummer terug aan de gebruiker op het scherm.

 Als je kiest voor "2: Ik wil mijn kluis openen", dan vraag je de gebruiker om
 zijn/haar code en als deze klopt dan toon je het nummer van de kluis dat
 daarbij hoort. Het zou leuk zijn als we de kluis ook echt konden openen, maar
 dat gaat lastig zonder een echte set bagagekluizen natuurlijk...

 Als je kiest voor "3: Ik geef mijn kluis terug", dan zou je een regel uit het
 tekstbestand moeten halen, maar dat is ingewikkeld en daarom is deze menukeuze
 optioneel!

 Als je kiest voor "4: Ik wil weten hoeveel kluizen nog vrij zijn", dan geef je
 als uitvoer het aantal kluizen dat nog beschikbaar is.

'''

from random import randint

file = open('kluizen.txt', 'a+')
file.seek(0)
file.close()

def nieuwe_kluis():
    file = open('kluizen.txt', 'r+')
    kluizen = []
    for kluis in file.readlines():
        kluizen.append(int(kluis.split(',')[0]))
    if(len(kluizen) < 12):
        for i in range(0, 12):
            if i + 1 not in kluizen:
                code = str(randint(1000, 9999))
                file.write(str(i + 1) + ',' + code + '\n')
                print('Kluisnummer {} met code {} '
                      'is toegewezen.\n'.format(str(i + 1), code))
                file.seek(0)
                break
    file.close()

def kluis_openen():
    file = open('kluizen.txt', 'r')
    codeInput = int(input('Voer 4-cijferige code in: '))
    kluizen = []
    for kluis in file.readlines():
        nummer, code = kluis.split(',')
        kluizen.append([int(nummer), int(code.rstrip())])
    for kluis in kluizen:
        if codeInput == kluis[1]:
            print('Kluis met nummer {} is geopend.\n'.format(kluis[0]))
            return
    print('Foutmelding! Er bestaat geen kluis met deze code.\n')
    file.close()

def kluis_teruggeven():
    file = open('kluizen.txt', "r+")
    codeInput = int(input('Voer 4-cijferige code in: '))
    kluizen = []
    for kluis in file.readlines():
        nummer, code = kluis.split(',')
        kluizen.append([int(nummer), int(code.rstrip())])
    nieuweRegels = []
    for kluis in kluizen:
        if codeInput != kluis[1]:
            nieuweRegels.append('{},{}\n'.format(kluis[0], kluis[1]))
    file.seek(0)
    file.truncate()
    file.writelines(nieuweRegels)
    file.close()

def aantal_kluizen_vrij():
    file = open('kluizen.txt', 'r')
    file.seek(0)
    aantalVrij = 12 - len(file.readlines())
    print('Er zijn {} kluisjes vrij.\n'.format(aantalVrij))
    file.close()

isBezig = True

while(isBezig):
    print('1: Ik wil een nieuwe kluis\n2: Ik wil mijn kluis openen\n'
          '3: Ik geef mijn kluis terug\n4: Ik wil weten hoeveel kluizen nog '
          'vrij zijn\n5: Ik wil stoppen\n''')

    menukeuze = int(input('Kies een menu optie: '))

    if menukeuze == 1:
        nieuwe_kluis()
    elif menukeuze == 2:
        kluis_openen()
    elif menukeuze == 3:
        kluis_teruggeven()
    elif menukeuze == 4:
        aantal_kluizen_vrij()
    else:
        isBezig = False