import colorama
from colorama import Back, Fore, Style

class Hut:
    hutsList = []
    def __init__(self,xCoordinate, yCoordinate):
        self.coordinates = [xCoordinate, yCoordinate]
        self.health = 10
        self.death = False
    def render(self,colorArray):
        if(self.health <=0):
            self.color = Back.LIGHTBLACK_EX + str(self.health) + Style.RESET_ALL
            self.death = True
        else:
            self.color = Back.LIGHTYELLOW_EX + "  " + Style.RESET_ALL
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self,idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 2
        return idArray

""" hutColor = Back.LIGHTYELLOW_EX + " " + Style.RESET_ALL
        hutPositions = [[8,2],[13,60],[27,73],[21,18],[37,49]]
        for coordinates in hutPositions:
            self.colorArray[coordinates[0]][coordinates[1]] = hutColor """