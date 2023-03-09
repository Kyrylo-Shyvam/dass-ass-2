from pickle import TRUE
import colorama
from colorama import Back, Fore, Style
import math
import numpy as np
colorama.init(autoreset=TRUE)
columns = 80
rows = 40
# idArray = 
# 0 - nothing
# 1 - King?
# 2 - Hut
# 3 - Cannon
# 4 - Townhall?
# 7 - Walls
# 9 - barbarians
##colorArray = [[Back.BLACK+" "+Style.RESET_ALL for i in range(columns)]for j in range(rows)]
class Game:
    def __init__(self, rows, columns):
        ##baseColor =
        ##colorArray = [[Back.LIGHTGREEN_EX+str(i)+str(j)+" "+Style.RESET_ALL for i in range(columns)]for j in range(rows)]
        
        ## printing the Town Hall
        self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL
        self.colorArray= [[self.color for i in range(columns)]for j in range(rows)]
        self.idArray = [[0 for i in range(columns)]for j in range(rows)]


        
        
    def board(self,rows,columns):
        ##self.colorArray = [[Back.LIGHTGREEN_EX+str(i)+str(j)+" "+Style.RESET_ALL for i in range(columns)] for j in range(rows)]
        self.colorArray = [[self.color for i in range(columns)] for j in range(rows)]
        self.colorArray = [[self.color for i in range(columns)] for j in range(rows)]
        self.idArray = [[0 for i in range(columns)] for j in range(rows)]
        """ for i in range(3):
            for j in range(4):
                self.colorArray[int(rows/2)-1+i][int(columns/2)-1+j]= Back.YELLOW + " " + Style.RESET_ALL
                
        for i in range(3):
            for j in (38,43):
                self.colorArray[int(rows/2)-1+i][j]= Back.LIGHTBLACK_EX + " " + Style.RESET_ALL

        for i in (18,22):
            for j in range(6):
                self.colorArray[i][int(columns/2)-2+j] = Back.LIGHTBLACK_EX + " " + Style.RESET_ALL

        ## canons
        canonPositions = [[20,60],[35,20]]
        for i in range(len(canonPositions)):
            for j in range(len(canonPositions[0])):
                self.colorArray[canonPositions[i][0]][canonPositions[i][1]] = Back.BLACK + " " + Style.RESET_ALL

         """


        
    def render(self):
        
        print("\n".join(["".join(row) for row in self.colorArray]))

    
