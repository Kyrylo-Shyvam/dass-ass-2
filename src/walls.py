from colorama import Back, Fore, Style

class Wall:
    wallsList = []
    def __init__(self, x, y):
        self.coordinates = [x, y]
        self.health = 2
        
    def render(self, colorArray):
        
        if(self.health <= 0):
            self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + " " + Style.RESET_ALL
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self, idArray):
        if(self.health>0):
            idArray[self.coordinates[0]][self.coordinates[1]] = 7

        
        return idArray
    
    