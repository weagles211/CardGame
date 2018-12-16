class Controller:

    def __init__(self):
        self.validCommand = ["Draw","View","Count","End"]
    
    def Action(self):
        command = input("Enter command:")
        if self.ValidateCommand(command):
            return command
        else:
            print("Invalid Command")
    
    def ValidateCommand(self,command):
        if command in self.validCommand:
            return True
        else:
            return False

    def DrawGameState(self, hand):

        if len(hand.cardlist) > 0:
            line1section = "------ "
            line2section = "|    | "
            line3sectionleft = "| "
            line3sectionright = " | "
            line4section = "|    | "
            line5section = "------ "


            line1 = ""
            line2 = ""
            line3 = ""
            line4 = ""
            line5 = ""

            for card in hand.cardlist:
                line1 += line1section
                line2 += line2section
                line3 += line3sectionleft + card + line3sectionright
                line4 += line4section
                line5 += line5section  
            
            lines = [line1,line2,line3,line4,line5 ]
            
            print("\n".join(lines))
        else:
            print("No cards in hand")
              
