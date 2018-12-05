'''

 Introduction To Computing Using Python (Werkboek)

 Functions (Perkovic - §3.3 t/m §3.5)

 Practice Exercise 4.4 (functie met if)
 Schrijf (en test) een functie new_password() die 2 parameters heeft:
 oldpassword en newpassword. De return-waarde is True als het nieuwe password
 voldoet aan de eisen. Het nieuwe password wordt alleen geaccepteerd als het
 verschilt van het oude password èn als het minimaal 6 tekens lang is. Als dat
 niet zo is, is de return waarde False.

 Optioneel: zorg dat het nieuwe password minstens 1 cijfer moet bevatten!

'''

def new_password(oldpassword, newpassword):
    '''Checks if new password meets set requirements. '''
    if oldpassword != newpassword and len(newpassword) >= 6:
        return any(char.isdigit() for char in newpassword)

a = new_password('password123', 'password123')
print(a) # False

b = new_password('password123', 'passw')
print(b) # False

c = new_password('password', 'password')
print(c) # False

d = new_password('password123', 'password1')
print(d) # True