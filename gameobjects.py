import random

class CardSet:

    def __init__(self):
        self.cardlist = []
        pass
    
    def getTotal(self):
        return len(self.cardlist)
        
    def draw(self, num):
        drawncard = self.cardlist.pop(0)
        return drawncard

    def shuffle(self):
        random.shuffle(self.cardlist)

    def view(self):
        print(self.cardlist)

    def addTo(self,card):
        self.cardlist.append(card)

class Deck(CardSet):

    def __init__(self):
        CardSet.__init__(self)
        self.generatedeck()
        self.shuffle()
        
    def generatedeck(self):
        shapes = ["A","B","C","D","E","F","G","H","I","J"]
        nums = ["1","2","3","4","5","6","7","8"]      
        for shape in shapes:
            for num in nums:
                self.cardlist.append(shape + num)
   
class Player:

    def __init__(self):
        self.hand = CardSet()
        self.disoardpile = CardSet()
        


