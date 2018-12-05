'''

 Introduction To Computing Using Python (Werkboek)

 Execution Control Structures (Perkovic – §5.1 t/m 5.3)

 Practice Exercise 6.2 (lists)
 Schrijf een nieuw programma waarin een list met minimaal 10 strings wordt
 ingelezen. Het programma plaatst alle vier-letter strings uit de ingelezen
 list in een nieuw list en drukt deze af. Inlezen van een lijst kan met
 eval(input("Geef lijst met minimaal 10 string: "))

'''

lst = eval(input("Geef lijst met minimaal 10 string: "))
# ['boter', 'kaas', 'bier', 'pizza', 'thee', 'drop, 'koek', 'cola', 'boterham',
#  'stamppot']

nieuweLst = []
for string in lst:
    if len(string) == 4:
        nieuweLst.append(string)

print(nieuweLst) # ['kaas', 'bier', 'thee', 'drop', 'koek', 'cola']