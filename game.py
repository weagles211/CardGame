import gameobjects
import userinterface

class Game():

    def __init__(self):
        print("Game Loading")
        self.gamedeck = gameobjects.Deck()
        self.player = gameobjects.Player()
        self.userinterface = userinterface.Controller()
        self.RunGame()

    def RunGame(self):
        print("Game Running")
        while 0 == 0:

            command = self.userinterface.Action()

            if command == "Draw":
                if self.player.hand.getTotal() == 9:
                    print("No more cards can be drawn.")
                else: 
                    drawncard = self.gamedeck.draw(1)
                    self.player.hand.addTo(drawncard)
                    print(drawncard)
                
            elif command == "View":
                self.player.hand.view()

            elif command == "Count":
                print(self.gamedeck.getTotal())


            elif command == "End":
                break
            else:
                print ("Invalid Command")

            self.userinterface.DrawGameState(self.player.hand)


#Run Game
activegame = Game()
