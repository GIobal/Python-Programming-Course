'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 10.3 (Locals & Globals)
 In de onderstaande programma's worden locals en globals gebruikt. Ga na wat de
 uitvoer is van deze programma's. Het is natuurlijk erg makkelijk om ze gewoon
 uit te voeren, maar probeer voordat je dat doet te beredeneren wat de uitvoer
 is en controleer dan pas jouw antwoord!

'''

# Uitvoer 8_3A:
a = 3

def f(y):
    global a
    a = 9
    return 2 * y + a

print(a) # B) 3

# Uitvoer 8_3B:
x = 1
y = 4

def fun():
    x = 2
    global y
    y = 3
    print(y, end = ' ')

fun()
print(y, end = '\n') # D) 3 3

# Uitvoer 8_3C:
x = 2
y = 5

def fun():
    y = 3
    global x
    x = 1
    print(x * y, end = ' ')
    return x * y

x = fun()
print(x * y, end = '\n') # A) 3 15

# Uitvoer 8_3D:
a = 3

def fun1():
    global a
    print('a:', a, end = ' ')
    b = 7
    a = 0
    return b

def fun2(y):
    a = y + fun1()
    b = 7
    a += 1
    return a

a = 9
fun2(5)
print('a:', a) # B) a: 9 a: 0

# Uitvoer 8_3E:
x = 1
y = 4

def doe1():
    global x
    y = 7
    x = 0
    return y

def doe2():
    x = doe1()
    x += 1
    return x

x = doe1()
print(x) # C) 7


# Uitvoer 8_3F:
a = 5
def fun1():
    global a
    b = 2
    a = 4
    return a + b

def fun2(y):
    global a
    a = y + fun1()
    a += 1
    return a

print('a:', a, end = ' ')
a = fun2(3)
print('a:', a) # D) a: 5 a: 10

# Uitvoer 8_3G:
x = 1
y = 3

def doe1():
    global x
    y = 4
    x = 0
    return x + y

def doe2():
    x = doe1()
    x += 2
    return x

doe2()
print(x)

# Uitvoer 8_3H:
def doe1():
    y = 7
    x = 0
    return y

def doe2():
    global x
    x = doe1()
    x += 1

doe2()
print(x) # D) 8