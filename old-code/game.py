from array import array
from distutils.spawn import spawn # see issue 23
from pickle import TRUE
import time
import colorama
from colorama import Fore, Back, Style
import time
from townhall import Townhall # see issue 6
colorama.init(autoreset=TRUE)
import numpy as np
from gameclass import Game
from kingclass import King
from input import input_to, Get
from os import system
from building import Townhall # see issue 6
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
        Check = True
    else:
        Check = False
num=str(fileNum)
file=file+num+".txt"
rageTime = -1
healTime = time.time()
rows = 40
columns = 80
COC=Game(rows,columns) # see issue 7
king = King()
COC.render()
townhall = Townhall()
victory = ['v','i','c','t','o','r','y','!']
defeat = ['d','e','f','e','a','t',':','(']

hutsCoordinates = [[8,2],[13,60],[35,73],[7,15],[37,72]]
hutsList = []

for i in range(5):
    hut = Hut(hutsCoordinates[i][0],hutsCoordinates[i][1])
    
    COC.colorArray = hut.render(COC.colorArray)
    hutsList.append(hut)

canonPositions = [[20,60],[35,20]]
canonsList = []
for i in range(2):
    canon = Canon(canonPositions[i][0],canonPositions[i][1])
    COC.colorArray = canon.render(COC.colorArray)
    canonsList.append(canon)
wallsList = []
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
barbariansList = []

# see issue 12
Hut.hutsList = hutsList
Canon.canonsList = canonsList
Wall.wallsList = wallsList
Barbarians.barbariansList = barbariansList
""" getch = Get()
for i in range(100):
    print(input_to(getch)) """

# see issue 8
def renderHuts():
    for i in range(len(Hut.hutsList)):
        COC.colorArray=Hut.hutsList[i].render(COC.colorArray)
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
# see issue 23
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
    
    Townhall.health = (3/2)*Townhall.health # see issue 6, 10, 18
    for hut in Hut.hutsList:
        hut.health = (3/2)*hut.health   # see issue 10
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

    key = king.input()
    king.move(COC.idArray)
    
    spawn(key)
    if(key == 'r'):
        rageTime = time.time()
        rageStart()
    if(time.time()-rageTime>=5):
        rageEnd()
        rageTime = time.time()

    if(key == 'h'): # see issue 18
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
    
        
        


    
