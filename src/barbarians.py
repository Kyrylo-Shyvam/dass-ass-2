from colorama import Back, Style
from building import Townhall
import math

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

class Barbarians:
    barbariansList = []
    velocity = 1
    def __init__(self,xCoordinate,yCoordinate):
        self.coordinates = [xCoordinate,yCoordinate]
        self.health = 10
        self.death = False
        self.target = None
        self.occupied = False
        Barbarians.barbariansList.append(self)
        
    def render(self,colorArray):
        ## barbarians
        if(self.health>0):
            self.color = Back.LIGHTRED_EX + str(self.health) + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + "  " + Style.RESET_ALL
            self.death = True
        
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self,idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 9
        return idArray
    
    def choose(self,Building):
        print("Target",self.target)
        if(self.target != None):
            print('Distance',abs(self.coordinates[0]-self.target.coordinates[0]),abs(self.coordinates[1]-self.target.coordinates[1]))
        if(self.occupied == False):
            print('barbPeek')
            min_distance = 1000
            for building in Building.buildingList:
                if isinstance(building, Townhall):
                    continue

                if(distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])<min_distance):
                    

                    
                    if(building.death==False):
                        self.target = building
                        min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])
                    
            self.occupied = True
            
        if(self.target.health<=0):
            self.target = None
            self.occupied = False
       
    ##barbarian movement
    def move(self,idArray):
        if(self.target == None):
            return idArray

        done = False
        for index in (0, 1):
            for sign in (1, -1):
                temp = idArray[self.coordinates[0] + sign*(1 - index)][self.coordinates[1] + sign*index]
                if((sign*self.coordinates[index] < sign*self.target.coordinates[index]) and
                   (( temp == 0 ) or
                    ( temp == 9 ))):
                    self.coordinates[index] = self.coordinates[index] + sign*self.velocity
                    done = True
                    break
            if(done): break
            
        if(abs(self.coordinates[0]-self.target.coordinates[0])<=1 and
           abs(self.coordinates[1]-self.target.coordinates[1])<=1):
            self.target.health-=2
            if(self.target.health<=0):
                self.occupied = False
                self.target = None
        
        return idArray