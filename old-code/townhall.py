import colorama
from colorama import Back, Fore, Style

class Townhall:
    

    def __init__(self):
        self.rows = 4
        self.columns = 3
        self.health = 10
        self.death = False
    def render(self,colorArray,idArray):
        if(self.health>7):        
            for i in range(self.rows):
                for j in range(self.columns):
                    colorArray[int(40/2)-1+i][int(80/2)-1+j]= Back.YELLOW + " " + Style.RESET_ALL
        elif(self.health > 5):
            for i in range(self.rows):
                for j in range(self.columns):
                    colorArray[int(40/2)-1+i][int(80/2)-1+j]= Back.LIGHTYELLOW_EX + " " + Style.RESET_ALL

        elif(self.health > 3):
            for i in range(self.rows):
                for j in range(self.columns):
                    colorArray[int(40/2)-1+i][int(80/2)-1+j]= Back.LIGHTRED_EX + " " + Style.RESET_ALL
        
        else:
            self.death = True
            for i in range(self.rows):
                for j in range(self.columns):
                    colorArray[int(40/2)-1+i][int(80/2)-1+j]= Back.LIGHTBLACK_EX + " " + Style.RESET_ALL   
        """ for i in (18,22):
            for j in range(6):
                colorArray[i][int(80/2)-2+j] = Back.LIGHTBLACK_EX + str(idArray[i][int(80/2)-2+j]) + Style.RESET_ALL


        for i in range(3):
            for j in (38,43):
                colorArray[int(40/2)-1+i][j]= Back.LIGHTBLACK_EX + str(idArray[int(40/2)-1+i][j]) + Style.RESET_ALL """
        return colorArray 
    def idUpdate(self, idArray): 
        for i in range(self.rows):
            for j in range(self.columns):
                idArray[int(40/2)-1+i][int(80/2)-1+j] = 4
        """ for i in (18,22):
            for j in range(6):
                idArray[i][int(80/2)-2+j] = 6


        for i in range(3):
            for j in (38,43):
                idArray[int(40/2)-1+i][j]= 6 """
        return idArray