'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 7.4 (file & dict)
 Een 'ticker symbool' is een unieke afkorting om aandelen van een bepaald
 bedrijf aan de beurs te identificeren. YHOO is bijvoorbeeld het ticker symbool
 van Yahoo, terwijl GOOG dat is voor Google.
 Gegeven is het onderstaande bestand met ticker symbols:

 YAHOO:YHOO
 GOOGLE INC:GOOG
 Harley-Davidson:HOG
 Yamana Gold:AUY
 Sotheby's:BID
 inBev:BUD

 Schrijf een functie ticker(filename). De functie leest uit de file zowel de
 bedrijfsnaam als het bijbehorende ticker-symbool en slaat die op in een
 dictionary. Dit is de return-waarde van de functie.

 Schrijf nu ook een programma die deze functie gebruikt om als iemand een
 ticker-symbool ingeeft de bedrijfsnaam te printen, en andersom. Het programma
 stopt hierna:

'''

def ticker(filename):
    file = open(filename, 'r')
    symbolen = {}
    for line in file.readlines():
        bedrijf, symbool = line.rstrip().split(':')
        symbolen[bedrijf] = symbool
    file.close()
    return symbolen

symbolen = ticker('ticker_symbolen.txt')

# Geef ticker gebaseerd op bedrijf.
bedrijf = input('Enter Company name: ')
print('Ticker symbol: {}\n'.format(symbolen[bedrijf]))

# Geef bedrijf gebaseerd op ticker.
ticker = input('Enter Ticker symbol: ')
bedrijf = list(symbolen.keys())[list(symbolen.values()).index(ticker)]
print('Company name: {}'.format(bedrijf))