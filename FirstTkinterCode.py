"""My First Ever Attempt At Doing Something With tkinter!"""

import tkinter
import random

window = tkinter.Tk()

def random_number():
    RandInt = random.randint(1,6)
    DiceThrown.configure(text="Dice Thrown! " + str(RandInt))

PageTitle = tkinter.Label(window, text="Random Number Generator", font="Helvectica 16 bold")
PageTitle.pack()

PageButton = tkinter.Button(window, text="Roll Dice", font="Helvectica 16 bold", command=random_number)
PageButton.pack()

DiceThrown = tkinter.Label(window, font="Helvectica 16")
DiceThrown.pack()

window.mainloop()
