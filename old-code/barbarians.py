from distutils.command.build import build
from colorama import Fore, Back, Style
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
                
                if(distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])<min_distance):
                    

                    
                    if(building.death==False):
                        self.target = building
                        min_distance = distance(self.coordinates[0],self.coordinates[1],building.coordinates[0],building.coordinates[1])
                    
            self.occupied = True
            
        if(self.target.health<=0):
            self.target = None
            self.occupied = False
       
    ##barbarian movement
    # see issue 20
    def move(self,idArray):
        if(self.target!=None):
            if(self.coordinates[0]<self.target.coordinates[0]):
                if(idArray[self.coordinates[0]+1][self.coordinates[1]]==0 or idArray[self.coordinates[0]+1][self.coordinates[1]]==9): # see issue 10
                    self.coordinates[0]+=self.velocity
            elif(self.coordinates[0]>self.target.coordinates[0]):
                if(idArray[self.coordinates[0]-1][self.coordinates[1]]==0 or idArray[self.coordinates[0]-1][self.coordinates[1]]==9):
                    self.coordinates[0]-=self.velocity
            elif(self.coordinates[1]<self.target.coordinates[1]):
                if(idArray[self.coordinates[0]][self.coordinates[1]+1]==0 or idArray[self.coordinates[0]][self.coordinates[1]+1]==9):
                    self.coordinates[1]+=self.velocity
            elif(self.coordinates[1]>self.target.coordinates[1]):
                if(idArray[self.coordinates[0]][self.coordinates[1]-1]==0 or idArray[self.coordinates[0]][self.coordinates[1]-1]==9):
                    self.coordinates[1]-=self.velocity
            if(abs(self.coordinates[0]-self.target.coordinates[0])<=1 and abs(self.coordinates[1]-self.target.coordinates[1])<=1):
                self.target.health-=2
                if(self.target.health<=0):
                    self.occupied = False
                    self.target = None
        return idArray




