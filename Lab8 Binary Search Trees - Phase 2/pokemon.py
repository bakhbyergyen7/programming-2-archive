"""
Lab 7 : Binary Search Tree (Phase 1)
Author: Bakhbyergyen Yerjan
Last Modified: 10/31/2022 10:19 AM
"""

class Pokemon:
    def __init__(self, USName, pokenum, JPName):
        self.USName = USName
        self.pokenum = int(pokenum)
        self.JPName = JPName

    def __str__(self):
        return f"{self.USName} {self.pokenum} {self.JPName}"
    
    def __lt__(self,other):
        # Need to put if statement in case it's not a pokedox number but just an integer
        if isinstance(other, Pokemon):
            return self.pokenum < other.pokenum
        elif isinstance(other, int):
            return self.pokenum < other

    def __gt__(self,other):
        if isinstance(other, Pokemon):
            return self.pokenum > other.pokenum
        elif isinstance(other, int):
            return self.pokenum > other

    def __eq__(self,other):
        if isinstance(other, Pokemon):
            return self.pokenum == other.pokenum
        elif isinstance(other, int):
            return self.pokenum == other

