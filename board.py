"""
Reaperopoly - Board Class

Defines the playing board of the game and all of it's spaces etc..

----------------------------------------------------------------
| GO             | Misery Avenue | Death Chest   | Bane Avenue |
| - Collect $200 |- Price $60    | - Pick a card | - Price $60 |
----------------------------------------------------------------

"""
class BoardSpace(object):
    name = ""

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

class Board(object):
    spaces = {
        "0" : "GO",
        "1" : "Misery Avenue",
        "2" : "Death Chest"
    }
    name = 'Reaperopoly Board'
    
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def printBoard(self):
        # TODO printBoard(): This is sample ASCII art code to display the current board
        print("----------------------------------------------------------------")
        print("| GO             | Misery Avenue | Death Chest   | Bane Avenue |")
        print("| - Collect $200 |- Price $60    | - Pick a card | - Price $60 |")
        print("----------------------------------------------------------------")
