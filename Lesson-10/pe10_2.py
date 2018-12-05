'''

 Introduction To Computing Using Python (Werkboek)

 Control Structures & Dictionaries (Perkovic – §5.4 t/m 6.1)

 Practice Exercise 10.1 (Namespaces)
 In onderstaande programma's wordt verkeerd gebruik gemaakt van namespaces.
 Verbeter de code!

'''
import time

# b = 7
# def verdubbelB():
#   b = b + b
# verdubbelB()
# print(b)

b = 7

def verdubbelB(b):
    return b + b

b = verdubbelB(b)
print(b)

# print(time.strftime(("%H:%M:%S)))
print(time.strftime("%H:%M:%S"))

# def f(y):
#   return 2*y + 1
# print(f(3)+g(3))
# def g(x)
#   return 5 + x + 10

def f(y):
    return 2 * y + 1

def g(x):
    return 5 + x + 10

print(f(3) + g(3))
