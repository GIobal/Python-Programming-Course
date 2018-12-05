from tkinter import *

root = Tk() # Creëer het hoofdscherm

button1 = Button(master = root, text = 'Button 1')
button1.pack(side = LEFT, pady = 10)

button2 = Button(master = root, text = 'Button 2')
button2.pack(side = RIGHT, pady = 10)

button3 = Button(master = root, text = 'Button 2')
button3.pack(side = TOP, pady = 10)

root.mainloop()
