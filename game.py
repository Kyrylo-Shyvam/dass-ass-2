from array import array
from distutils.spawn import spawn # Why do we need this; not used?
from pickle import TRUE  # Used to auto reset colorama. Why?
import time
import colorama
from colorama import Fore, Back, Style
import time
from townhall import Townhall
# If you find yourself repeatedly sending reset sequences to turn off color changes
# at the end of every print, then init(autoreset=True) will automate that:
colorama.init(autoreset=TRUE) 
import numpy as np
from gameclass import Game
from kingclass import King
from input import input_to, Get
from os import system
from building import Townhall
from building import Canon
from building import Hut
from building import Wall
from barbarians import Barbarians
from building import Building
import os
""" arrays = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        arrays[i][j] = Back.BLUE+Fore.RED+"  "+Style.RESET_ALL

print("\n".join(["".join(row) for row in arrays])) """

fileNum=1
if not os.path.exists('./replay'):
    os.makedirs('./replay')
    
file="./replay/game"
Check = True

while(Check):
    if(os.path.exists(file+str(fileNum)+".txt")):
        fileNum+=1
        Check = True # Not required
    else:
        Check = False

num=str(fileNum) # Number of files in replay directory + 1 extra
file=file+num+".txt" # Name of new file?

rageTime = -1    # Is it not working?
healTime = time.time() # Time since 1970, why?

rows = 40
columns = 80 # Already mentioned in gameclass?

COC=Game(rows,columns)
king = King()
COC.render()  
#  What render exactly does?
# It prints a self.colorArray, final output to be shown.
townhall = Townhall()

victory = ['v','i','c','t','o','r','y','!']
defeat = ['d','e','f','e','a','t',':','(']

hutsCoordinates = [[8,2],[13,60],[35,73],[7,15],[37,72]]
hutsList = [] # Is this list of working huts? No. All huts objects

for i in range(5):
    hut = Hut(hutsCoordinates[i][0],hutsCoordinates[i][1])
    COC.colorArray = hut.render(COC.colorArray)
    # Rendering saved a hut image on board.
    hutsList.append(hut)

canonPositions = [[20,60],[35,20]]
canonsList = []
for i in range(2):
    canon = Canon(canonPositions[i][0],canonPositions[i][1])
    # Same for cannons
    COC.colorArray = canon.render(COC.colorArray)
    canonsList.append(canon)

wallsList = []
# We create walls in the middle of the map
# We do not render them?
for i in (18,23):
    for j in range(6):
        wall = Wall(i,int(columns/2)-2+j)
        ##COC.colorArray = wall.render(COC.colorArray)
        wallsList.append(wall)

for i in range(3):
    for j in (38,43):
        wall = Wall(int(rows/2)-1+i,j)
        ##COC.colorArray = wall.render(COC.colorArray)
        wallsList.append(wall)

Hut.hutsList = hutsList
Canon.canonsList = canonsList
Wall.wallsList = wallsList

barbariansList = []
Barbarians.barbariansList = barbariansList
# Why these comments?
""" getch = Get()
for i in range(100):
    print(input_to(getch)) """

def renderHuts():
    # We already had a function to render in Huts
    # This one renders all of them. And updates id, which is stored.
    for i in range(len(Hut.hutsList)):
        COC.colorArray=Hut.hutsList[i].render(COC.colorArray)
        # Id array tells id (of object) at each coordinate.
        # Actually we need only this one 2D array. Other can be deleted.
        COC.idArray = Hut.hutsList[i].idUpdate(COC.idArray)

def renderCanons():
    for i in range(len(canonsList)):
        COC.colorArray=canonsList[i].render(COC.colorArray)
        COC.idArray = canonsList[i].idUpdate(COC.idArray)

def renderWalls():
    for i in range(len(Wall.wallsList)):
        COC.colorArray=Wall.wallsList[i].render(COC.colorArray)
        COC.idArray = Wall.wallsList[i].idUpdate(COC.idArray)

def renderBarbarians():
    for i in range(len(Barbarians.barbariansList)):
        COC.colorArray=Barbarians.barbariansList[i].render(COC.colorArray)
        COC.idArray = Barbarians.barbariansList[i].idUpdate(COC.idArray)

def canonShoot():
    for i in range(len(canonsList)):
        canonsList[i].shoot(king,Barbarians)

def spawn(key):
    if(key == 'z'):
        barbarian = Barbarians(38,22)
        COC.colorArray = barbarian.render(COC.colorArray)
        COC.idArray = barbarian.idUpdate(COC.idArray)
        Barbarians.barbariansList.append(barbarian)
    if(key == 'c'):
        barbarian = Barbarians(17,65)
        COC.colorArray = barbarian.render(COC.colorArray)
        COC.idArray = barbarian.idUpdate(COC.idArray)
        Barbarians.barbariansList.append(barbarian)
    if(key == 'v'):
        barbarian = Barbarians(35,65)
        COC.colorArray = barbarian.render(COC.colorArray)
        COC.idArray = barbarian.idUpdate(COC.idArray)
        Barbarians.barbariansList.append(barbarian)

def rageStart():
    COC.color = Back.LIGHTMAGENTA_EX + "  " + Style.RESET_ALL
    king.velocity = 2
    Barbarians.velocity = 2
    townhall.health = 10 - 2*(10 - townhall.health)
    for hut in Hut.hutsList:
        hut.health = 10 - 2*(10 - hut.health)
    for canon in Canon.canonsList:
        canon.health = 10 - 2*(10 - canon.health)

def rageEnd():
    COC.color = Back.LIGHTGREEN_EX + "  " + Style.RESET_ALL
    king.velocity = 1
    Barbarians.velocity = 1

def healStart():
    COC.color = Back.LIGHTYELLOW_EX + "  " + Style.RESET_ALL
    # Bug - must be 'townhall', leads to crash.
    # And heal spell must heal troops, not buildings.
    Townhall.health = (3/2)*Townhall.health # Must be capped?
    for hut in Hut.hutsList:
        hut.health = (3/2)*hut.health
        if(hut.health>10):
            hut.health = 10
    for canon in Canon.canonsList:
        canon.health = (3/2)*canon.health
        if(canon.health>10):
            canon.health = 10

def healEnd():
    COC.color = Back.LIGHTGREEN_EX + "  " + Style.RESET_ALL
    
def checkVictory():
    check = False
    if(townhall.death == True):
        check = True
    else:
        return False
    for hut in Hut.hutsList:
        if(hut.death == True):
            check = True
        else:
            return False
    for canon in Canon.canonsList:
        if(canon.death == True):
            check = True
        else:
            return False
    return check

def checkDefeat():
    check = False
    for barbarian in Barbarians.barbariansList:
        if(barbarian.death == True):
            check = True
        else:
            return False
    if(king.death == True):
        check = True
    else:
        return False
    return check

def narikey():
    for building in Building.buildingList:
        # Damage buildings near king
        if(abs(building.coordinates[0]-king.coordinates[0])< 5 and abs(building.coordinates[1]-king.coordinates[1]) < 5):
            building.health = building.health - 5
 
def moveBarbarians():
    for barbarian in Barbarians.barbariansList:
        barbarian.choose(Building)
        barbarian.move(COC.idArray)

while(1):


    COC.board(rows,columns)
    COC.idArray = townhall.idUpdate(COC.idArray)
    COC.colorArray =  townhall.render(COC.colorArray, COC.idArray)

    renderHuts()
    renderCanons()
    renderWalls()
    canonShoot()
    moveBarbarians()
    renderBarbarians()

    key = king.input() # Input should be separate from king
    king.move(COC.idArray)
    
    spawn(key)
    if(key == 'r'):
        rageTime = time.time()
        rageStart()
    if(time.time()-rageTime>=5):
        rageEnd()
        rageTime = time.time()

    if(key == 'h'):
        healTime = time.time()
        healStart()
    if(time.time()-healTime>=5):
        healEnd()
    if(key == 'x'):
        narikey()
    if(key == ' '):
        king.attack(COC,townhall,Hut,Canon,Wall)


    COC.colorArray = king.update(COC.colorArray)
    COC.idArray = king.idUpdate(COC.idArray)
    king.healthDisplay(COC.colorArray)
    if(checkVictory()==True):
        COC.colorArray= [[Back.LIGHTGREEN_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
        for i in range(8):
            COC.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.GREEN + victory[i] + Style.RESET_ALL
        break
    if(checkDefeat()==True):
        COC.colorArray= [[Back.LIGHTRED_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
        for i in range(8):
            COC.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.LIGHTRED_EX + defeat[i] + Style.RESET_ALL
    
    system('clear')
    COC.render()
    file_name=open(file,"a")
    file_name.write("\n".join(["".join(row) for row in COC.colorArray]))
    file_name.write("\n")
    file_name.close()
    
        
        



