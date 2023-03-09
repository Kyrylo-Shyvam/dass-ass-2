
import colorama
from colorama import Back, Fore, Style
import time

class Canon:
    canonsList = []
    def __init__(self,xCoordinate,yCoordinate):
        self.coordinates = [xCoordinate,yCoordinate]
        self.health = 10
        self.occupied = False
        self.victim = None
        self.target = None
        self.init = time.time()
        self.death = False
    def render(self,colorArray,):
         
        ## canons
        if(self.health>0):
            self.color = Back.BLACK + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + "  " + Style.RESET_ALL
            self.death = True
        
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self, idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 3
        return idArray

    def shoot(self,king,Barbarians):
        min_distance = 10
        print(self.occupied)
        self.target = None
        if(self.victim!=None):
            if(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[1]-self.coordinates[1])<5):
                            
                print('yess')
            else:
                print('nooo')
                self.victim = None
                self.occupied = False
        if(abs(king.coordinates[0]-self.coordinates[0])<5 and abs(king.coordinates[1]-self.coordinates[1])<5 and king.death == False):
            distance = abs(king.coordinates[0]-self.coordinates[0]) + abs(king.coordinates[1]-self.coordinates[1])
            if(distance<min_distance):
                min_distance = distance
                self.target = king
        for barbarian in Barbarians.barbariansList:
            if(abs(barbarian.coordinates[0]-self.coordinates[0])<5 and abs(barbarian.coordinates[1]-self.coordinates[1])<5):
                distance = abs(barbarian.coordinates[0]-self.coordinates[0]) + abs(barbarian.coordinates[1]-self.coordinates[1])
                if(barbarian.death == False):
                    if(distance<min_distance):
                        min_distance = distance
                        self.target = barbarian
        print(self.target)
        if(self.target!=None):
            if(self.occupied==False):
                self.victim = self.target
                self.occupied = True
            
                
                if(min_distance<10):
                    self.victim.health -= 1
                    self.occupied = True
                    if(self.victim.health <=0):
                        self.victim = None
                        self.occupied = False
            else:
                print(self.coordinates, self.victim.coordinates)
                print(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[0]-self.coordinates[0])<5)
                if(self.target != self.victim):
                    if(abs(self.victim.coordinates[0]-self.coordinates[0])<5 and abs(self.victim.coordinates[1]-self.coordinates[1])<5):
                        
                        print('yes')
                    else:
                        self.victim = self.target
                print(self.victim)
                if(time.time()-self.init > 1):
                    self.init = time.time()
                    self.victim.health -= 1
                if(self.victim.health <=0):
                    self.victim = None
                    self.occupied = False
        
        