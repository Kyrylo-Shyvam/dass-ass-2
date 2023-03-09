
import colorama
from colorama import Back, Fore, Style

##from game import COC

from input import input_to, Get

class King: 
    def __init__(self):
        getch = Get()
        self.coordinates = [25,55]
        self.rows = 2
        self.columns = 2
        self.color = Back.CYAN + " " + Style.RESET_ALL 
        self.key = 'h'
        self.health = 100
        self.death = False
        self.velocity = 1
        """ for i in range(self.rows):
            for j in range(self.columns):
                colorArray[self.coordinates[0] - 1 + i][self.coordinates[1] - 1 + j] = self.color """
    def input(self):
        getch = Get()
        print(self.coordinates[0],self.coordinates[1])
        self.key = input_to(getch)
        return self.key
        
    def move(self,idArray):
        if(self.key =='w'):
            ##print(idArray[self.coordinates[0]-1][self.coordinates[1]-2],idArray[self.coordinates[0]][self.coordinates[1]-2])
            print(idArray[self.coordinates[0]-2][self.coordinates[1]-1], idArray[self.coordinates[0]-2][self.coordinates[1]])
            if(self.coordinates[0]> 1 and  self.coordinates[0] < 39):
                if(idArray[self.coordinates[0]-2][self.coordinates[1]-1]==0 and idArray[self.coordinates[0]-2][self.coordinates[1]]==0):
                
                    self.coordinates[0]-= self.velocity
        elif(self.key=='s'):
            if(self.coordinates[0]> 1 and  self.coordinates[0] < 39):
                if(idArray[self.coordinates[0]+1][self.coordinates[1]-1]==0 and idArray[self.coordinates[0]+1][self.coordinates[1]]==0):
                
                    self.coordinates[0]+=self.velocity
        elif(self.key=='a'):
            ##print(idArray[self.coordinates[0]-2][self.coordinates[1]-1])
            if(self.coordinates[1]>1 and self.coordinates[1]<79):
                if(idArray[self.coordinates[0]-1][self.coordinates[1]-2]==0 and idArray[self.coordinates[0]][self.coordinates[1]-2]==0):
                
                    
                    self.coordinates[1]-=self.velocity
            
        elif(self.key=='d'):
            if(self.coordinates[1]>1 and self.coordinates[1]<79):
                if(idArray[self.coordinates[0]-1][self.coordinates[1]+1]==0 and idArray[self.coordinates[0]][self.coordinates[1]+1]==0):
                
                    self.coordinates[1]+=self.velocity
        elif(self.key == ' '):
            if(self.coordinates[1]>1 and self.coordinates[1]<79 and self.coordinates[0]> 1 and  self.coordinates[0] < 39):
                pass
    def attack(self,COC,Townhall,hut,canon,wall):
        hutsList = hut.hutsList
        canonsList = canon.canonsList
        wallsList = wall.wallsList
        print(len(wallsList))
        ##print(wall.wallsList)
        if(self.coordinates[1]>1 and self.coordinates[1]<79 and self.coordinates[0]> 1 and  self.coordinates[0] < 39):
            if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]!=0 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]!=0):
                
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==7 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==7):
                   length = len(wallsList)
                   for i in range(length):
                        Wall = wallsList[i]
                        
                        
                        if(Wall.coordinates[0]==self.coordinates[0]-2 and Wall.coordinates[1]==self.coordinates[1]-1 and Wall.health!=0):
                            print(1000)
                            Wall.health -= 1 
                            if(Wall.health==0):
                                
                                COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                        if(Wall.coordinates[0]==self.coordinates[0]-2 and Wall.coordinates[1] == self.coordinates[1] and Wall.health!=0):
                            print(1000)
                            Wall.health -= 1 
                            if(Wall.health==0):
                                    
                                COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0
                        
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==2 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==2):
                    length = len(hutsList)
                    for i in range(length):
                        Hut = hutsList[i]
                        if(Hut.coordinates[0]==self.coordinates[0]-2 and Hut.coordinates[1]==self.coordinates[1]-1 and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.coordinates[0]==self.coordinates[0]-2 and Hut.coordinates[1] == self.coordinates[1] and Hut.health!=0):
                            Hut.health -= 1 
                        if(Hut.health == 0):
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==3 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==3):
                    length = len(canonsList)
                    for i in range(length):
                        Canon = canonsList[i]
                        if(Canon.coordinates[0]==self.coordinates[0]-2 and Canon.coordinates[1]==self.coordinates[1]-1 and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.coordinates[0]==self.coordinates[0]-2 and Canon.coordinates[1] == self.coordinates[1] and Canon.health!=0):
                            Canon.health -= 1 
                        if(Canon.health == 0):
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                            COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0
                if(COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1]==4 or COC.idArray[self.coordinates[0]-2][self.coordinates[1]]==4):
                    
                    
                    Townhall.health -= 1 
                    if(Townhall.health == 0):
                        COC.idArray[self.coordinates[0]-2][self.coordinates[1]-1] = 0
                        COC.idArray[self.coordinates[0]-2][self.coordinates[1]] = 0 
            
            if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]!=0 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]!=0):
                    print(1)
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==7 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]+1 and Wall.coordinates[1]==self.coordinates[1]-1 and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                            if(Wall.coordinates[0]==self.coordinates[0]+1 and Wall.coordinates[1] == self.coordinates[1] and Wall.health!=0):
                                print(1000)
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==2 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==2):
                        length = len(hutsList)
                        print(1)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coordinates[0]+1 and Hut.coordinates[1]==self.coordinates[1]-1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coordinates[0]+1 and Hut.coordinates[1] == self.coordinates[1] and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==3 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coordinates[0]+1 and Canon.coordinates[1]==self.coordinates[1]-1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coordinates[0]+1 and Canon.coordinates[1] == self.coordinates[1] and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                                COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
                    if(COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1]==4 or COC.idArray[self.coordinates[0]+1][self.coordinates[1]]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coordinates[0]+1][self.coordinates[1]-1] = 0
                            COC.idArray[self.coordinates[0]+1][self.coordinates[1]] = 0
              
            if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]!=0 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]!=0):
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==7 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]-1 and Wall.coordinates[1]==self.coordinates[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                            if(Wall.coordinates[0]==self.coordinates[0] and Wall.coordinates[1] == self.coordinates[1]-2 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==2 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coordinates[0]-1 and Hut.coordinates[1]==self.coordinates[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coordinates[0] and Hut.coordinates[1] == self.coordinates[1]-2 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==3 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coordinates[0]-1 and Canon.coordinates[1]==self.coordinates[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coordinates[0] and Canon.coordinates[1] == self.coordinates[1]-2 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2]==4 or COC.idArray[self.coordinates[0]][self.coordinates[1]-2]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coordinates[0]-1][self.coordinates[1]-2] = 0
                            COC.idArray[self.coordinates[0]][self.coordinates[1]-2] = 0
            if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]!=0 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]!=0):
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==7 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==7):
                        length = len(wallsList)
                        for i in range(length):
                            Wall = wallsList[i]
                            
                            
                            if(Wall.coordinates[0]==self.coordinates[0]-1 and Wall.coordinates[1]==self.coordinates[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                    
                                    COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                            if(Wall.coordinates[0]==self.coordinates[0] and Wall.coordinates[1] == self.coordinates[1]+1 and Wall.health!=0):
                                Wall.health -= 1 
                                if(Wall.health==0):
                                        
                                    COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==2 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==2):
                        length = len(hutsList)
                        for i in range(length):
                            Hut = hutsList[i]
                            if(Hut.coordinates[0]==self.coordinates[0]-1 and Hut.coordinates[1]==self.coordinates[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.coordinates[0]==self.coordinates[0] and Hut.coordinates[1] == self.coordinates[1]+1 and Hut.health!=0):
                                Hut.health -= 1 
                            if(Hut.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==3 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==3):
                        length = len(canonsList)
                        for i in range(length):
                            Canon = canonsList[i]
                            if(Canon.coordinates[0]==self.coordinates[0]-1 and Canon.coordinates[1]==self.coordinates[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.coordinates[0]==self.coordinates[0] and Canon.coordinates[1] == self.coordinates[1]+1 and Canon.health!=0):
                                Canon.health -= 1 
                            if(Canon.health == 0):
                                COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                                COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                    if(COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1]==4 or COC.idArray[self.coordinates[0]][self.coordinates[1]+1]==4):
                        Townhall.health -= 1 
                        if(Townhall.health == 0):
                            COC.idArray[self.coordinates[0]-1][self.coordinates[1]+1] = 0
                            COC.idArray[self.coordinates[0]][self.coordinates[1]+1] = 0
                            
    def update(self,colorArray):
        self.color = Back.CYAN + str(self.health) + Style.RESET_ALL
        if(self.health>=0):
            self.color = Back.CYAN + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTBLACK_EX + " " + Style.RESET_ALL
            self.death = True
        for i in range(self.rows):
            for j in range(self.columns):
                colorArray[self.coordinates[0] - 1 + j][self.coordinates[1] - 1 + i] = self.color

                
        return colorArray

    def idUpdate(self,idArray):
        for i in range(self.rows):
            for j in range(self.columns):
                idArray[self.coordinates[0] - 1 + j][self.coordinates[1] - 1 + i] = 1
        return idArray

    def healthDisplay(self,colorArray):
        health = ['H','e','a','l','t','h','=',]
        fraction = self.health/100
        for i in range(len(health)):
            colorArray[1][60 - 7 + i] = Back.LIGHTGREEN_EX + health[i] + Style.RESET_ALL
        toColor = int(fraction*10)
        for i in range(toColor):
            colorArray[1][60 + i] = Back.GREEN + ' ' + Style.RESET_ALL
        for i in range(10-toColor):
            colorArray[1][60 + toColor + i] = Back.RED + ' ' + Style.RESET_ALL
        return colorArray

