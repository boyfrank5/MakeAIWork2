#!/usr/bin/env python

import random
import numpy as np


class Dobbelsteen:
    
    def __init__(self):
        self.history = list()
        self.values = set(range(1, 7))  
        self.roll()
        
        # https://realpython.com/python-dice-roll
        self.faces = {

            1: (

                "┌─────────┐\n"
                "│         │\n"
                "│    ●    │\n"
                "│         │\n"
                "└─────────┘\n"
            ),

            2: (

                "┌─────────┐\n"
                "│  ●      │\n"
                "│         │\n"
                "│      ●  │\n"
                "└─────────┘"
            ),

            3: (

                "┌─────────┐\n"
                "│  ●      │\n"
                "│    ●    │\n"
                "│      ●  │\n"
                "└─────────┘"
            ),

            4: (

                "┌─────────┐\n"
                "│  ●   ●  │\n"
                "│         │\n"
                "│  ●   ●  │\n"
                "└─────────┘"

            ),

            5: (

                "┌─────────┐\n"
                "│  ●   ●  │\n"
                "│    ●    │\n"
                "│  ●   ●  │\n"
                "└─────────┘"
            ),

            6: (

                "┌─────────┐\n"
                "│  ●   ●  │\n"
                "│  ●   ●  │\n"
                "│  ●   ●  │\n"
                "└─────────┘"

            )

        }

    def getList(self):
        return list(self.values)

    def roll(self):
        self.number = random.choice(self.getList())
        self.history.append(self.number)

    def getNumber(self):
        return self.number

    def show(self):        
        return str(self.faces.get(self.number))
    
    def getHistory(self):
        return np.array(self.history) # Geef de variabele 'history' als een numpy array terug.
    
    
def main(): #conventie van python om altijd een Main functie te begruiken. 
    d = Dobbelsteen()
    d.roll()
    d.show()
    d.getHistory() 
    print(d.getHistory())


    
if __name__ == main():
    main()           