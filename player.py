"""
Reaperopoly - Player Class

Initialize with a name and starting wallet amount
me = Player("Bob",0.00)

"""
class Player(object):
    name = "Unknown"
    wallet = 0.00
        
    def __init__(self,name,wallet):
        self.name = name
        self.wallet = wallet
        
    def __str__(self):
        return 'Player(name='+self.name+',wallet=RS$'+str(self.wallet)+')'
    
    def printPlayer(self):
        print(self.name)
        print("RS$" + str(self.wallet))
    
    def getWallet(self):
        return self.wallet
    
    def addWallet(self,amt):
        self.wallet += amt
