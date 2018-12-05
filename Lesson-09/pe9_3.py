'''

 Introduction To Computing Using Python (Werkboek)

 Catching Exceptions, CSV-files (Perkovic – §4.4 & §7.3)

 Practice Exercise 9.3 (CSV-files lezen)
 In deze opdracht krijg je een CSV-bestand met informatie van een aantal gamers.
 Per regel staan er drie gegevens van een gamer: de naam, de speeldatum en de
 behaalde score. Het programma leest alle regels in en bepaalt welke gamer de
 hoogste score heeft behaald en op welke datum dat was.

 Uitvoer:
    De hoogste score is 69 op 11-05-2016 behaald door Douwe Bob

 Deze informatie komt uit het volgende CSV-bestand, neem deze over:
    Anton;12-05-2016;29
    Douwe Bob;13-05-2016;44
    Anton;11-05-2016;39
    Douwe Bob;12-05-2016;55
    Anton;10-05-2016;29
    Douwe Bob;11-05-2016;69

'''

with open('gamers.csv', 'r') as file:
    scores = []
    for line in file.readlines():
        naam, datum, score = line.rstrip().split(';')
        scores.append([score, [datum, naam]])
    hoogsteScore = max(scores)
    print('De hoogste score is: {} op {} behaald door '
          '{}'.format(hoogsteScore[0], hoogsteScore[1][0], hoogsteScore[1][1]))