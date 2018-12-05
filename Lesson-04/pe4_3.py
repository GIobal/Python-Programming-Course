'''

 Introduction To Computing Using Python (Werkboek)

 Functions (Perkovic - §3.3 t/m §3.5)

 Practice Exercise 4.3 (functie met if)
 Schrijf (en test) de functie lang_genoeg() die voor Efteling-attracties
 bepaalt of een gebruiker in een attractie mag. De functie heeft één parameter,
 namelijk de lengte van de gebruiker in centimers. Als de gebruiker 120
 centimeter of langer is de return-waarde van de functie "Je bent lang genoeg
 voor de attractie!", anders is de melding "Sorry, je bent te klein!".

'''

def lang_genoeg(lengte):
    '''Returns message based on given height in centimeters.'''
    if(lengte >= 120):
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

reactie = lang_genoeg(180)
print(reactie) # 'Je bent lang genoeg voor de attractie!'