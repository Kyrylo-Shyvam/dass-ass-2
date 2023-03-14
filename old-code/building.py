from colorama import Back, Style
import time

class Building:
    buildingList = []
    def __init__(self,x,y):
        self.coordinates = [x,y]
        self.health = 10
        self.death = False
        Building.buildingList.append(self)
    


class Hut(Building):
    hutsList = []
    def __init__(self,x,y):
        super().__init__(x,y)
        
    def render(self,colorArray):
        if(self.health <=0):
            self.color = Back.LIGHTBLACK_EX + " " + Style.RESET_ALL
            self.death = True
        elif(self.health > 5):
            self.color = Back.LIGHTYELLOW_EX + " " + Style.RESET_ALL
        elif(self.health > 3):
            self.color = Back.LIGHTRED_EX + " " + Style.RESET_ALL
        else:
            self.color = Back.YELLOW + " " + Style.RESET_ALL
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self,idArray):
        idArray[self.coordinates[0]][self.coordinates[1]] = 2
        return idArray


class Canon(Building):
    canonsList = []
    def __init__(self,xCoordinate,yCoordinate):
        ##self.coordinates = [xCoordinate,yCoordinate]
        ##self.health = 10
        super().__init__(xCoordinate,yCoordinate)
        self.occupied = False
        self.victim = None
        self.target = None
        self.init = time.time()
        
        ##self.death = False
    def render(self,colorArray,):
         
        ## canons
        if(self.health>7):
            self.color = Back.BLACK +" "+ Style.RESET_ALL
        elif(self.health > 5):
            self.color = Back.LIGHTBLACK_EX +" " + Style.RESET_ALL
        elif(self.health > 3):
            self.color = Back.RED + " " + Style.RESET_ALL
        else:
            self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL
            self.death = True
        
        colorArray[self.coordinates[0]][self.coordinates[1]] = self.color
        return colorArray
    def idUpdate(self, idArray):
        if(self.death==False):
            idArray[self.coordinates[0]][self.coordinates[1]] = 3
        return idArray

    def shoot(self,king,Barbarians):
        if(self.death==False):
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
            
class Wall(Building):
    wallsList = []
    def __init__(self, x, y):
        super().__init__(x,y)
        
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

    
        
class Townhall(Building):
    

    def __init__(self):
        self.rows = 4
        self.columns = 3
        self.health = 10
        self.death = False
    def render(self,colorArray,idArray):
        if(self.health>0):        
            for i in range(self.rows):
                for j in range(self.columns):
                    colorArray[int(40/2)-1+i][int(80/2)-1+j]= Back.YELLOW + " " + Style.RESET_ALL   # see issue 10
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
                idArray[int(40/2)-1+i][int(80/2)-1+j] = 4   # see issue 10
        """ for i in (18,22):
            for j in range(6):
                idArray[i][int(80/2)-2+j] = 6


        for i in range(3):
            for j in (38,43):
                idArray[int(40/2)-1+i][j]= 6 """
        return idArray
