'''

 Introduction To Computing Using Python (Werkboek)

 Starten met Python (Perkovic - §1.1 t/m §2.3)

 Practice Exercise 1.5 (lists)
 We gaan een lijst bijhouden met je favoriete artiesten. We gaan de lijst eerst
 creëren met 1 artiest en dan uitbreiden. Schrijf per stap een expressie om:

'''

# 1. Een nieuwe list met 1 artiest aan te maken met de naam favorieten.
favorieten = ['nothing,nowhere']
print(favorieten) # ['nothing,nowhere']

# 2. De lijst uit te breiden met een tweede artiest.
favorieten.append('lil peep')
print(favorieten) # ['nothing,nowhere', 'lil peep']

# 3. De tweede artiest de vervangen door een andere naam.
favorieten[1] = 'VAGUE003'
print(favorieten) # ['nothing,nowhere', 'VAGUE003']