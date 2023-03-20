import time
import sys
import termios

from building import Building, Townhall
from building import Canon
from building import Hut
from building import Wall
from barbarians import Barbarians
from kingclass import King
from input import Get, input_to

import colorama
from colorama import Back, Style
import os
colorama.init(autoreset=True)

columns = 80
rows = 40

hutsCoordinates = [[8,2],[13,60],[35,73],[7,15],[37,72]]
canonPositions = [[20,60],[35,20]]
victory = ['v','i','c','t','o','r','y','!']
defeat = ['d','e','f','e','a','t',':','(']

class Game:
    def __init__(self):
        self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL
        self.colorArray= [[self.color for _ in range(columns)] for _ in range(rows)]
        self.idArray = [[0 for _ in range(columns)] for _ in range(rows)]       

        self.townhall = Townhall()
        self.king = King()

        self.rageTime = -1
        self.healTime = time.time()

        for i in range(5):
            hut = Hut(hutsCoordinates[i][0],hutsCoordinates[i][1])
            self.colorArray = hut.render(self.colorArray)

        for i in range(2):
            canon = Canon(canonPositions[i][0],canonPositions[i][1])
            self.colorArray = canon.render(self.colorArray)

        for i in (18,23):
            for j in range(6):
                Wall(i,int(columns/2)-2+j)

        for i in range(3):
            for j in (38,43):
                Wall(int(rows/2)-1+i,j)

    def board(self,rows,columns):
        self.colorArray = [[self.color for _ in range(columns)] for _ in range(rows)]
        self.colorArray = [[self.color for _ in range(columns)] for _ in range(rows)]
        self.idArray = [[0 for _ in range(columns)] for _ in range(rows)]

    def spawn(self, key):
        if(key == 'z'):
            Barbarians(38,22)
        if(key == 'c'):
            Barbarians(17,65)
        if(key == 'v'):
            Barbarians(35,65)

    def rageStart(self):
        self.color = Back.LIGHTMAGENTA_EX + " " + Style.RESET_ALL
        self.king.velocity = 2
        Barbarians.velocity = 2
        self.townhall.health = 10 - 2*(10 - self.townhall.health)
        for hut in Hut.hutsList:
            hut.health = 10 - 2*(10 - hut.health)
        for canon in Canon.canonsList:
            canon.health = 10 - 2*(10 - canon.health)

    def rageEnd(self):
        self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL
        self.king.velocity = 1
        Barbarians.velocity = 1

    def healStart(self):
        self.color = Back.LIGHTYELLOW_EX + " " + Style.RESET_ALL

        self.townhall.health = (3/2) * self.townhall.health
        for hut in Hut.hutsList:
            hut.health = (3/2)*hut.health
            if(hut.health>10):
                hut.health = 10
        for canon in Canon.canonsList:
            canon.health = (3/2)*canon.health
            if(canon.health>10):
                canon.health = 10

    def healEnd(self):
        self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL

    def narikey(self):
        for building in Building.buildingList:
            if isinstance(building, Townhall):
                continue

            if(abs(building.coordinates[0] - self.king.coordinates[0]) < 5 and 
               abs(building.coordinates[1] - self.king.coordinates[1]) < 5):
                building.health = building.health - 5
        
    def checkVictory(self):
        check = False
        if(self.townhall.death == True):
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

    def checkDefeat(self):
        check = False
        for barbarian in Barbarians.barbariansList:
            if(barbarian.death == True):
                check = True
            else:
                return False
        if(self.king.death == True):
            check = True
        else:
            return False
        return check

    def render(self):
        key = input_to(Get())
        os.system('clear')

        if(key == 'r'):
            self.rageTime = time.time()
            self.rageStart()
        if(time.time() - self.rageTime>=5):
            self.rageEnd()
            self.rageTime = time.time()

        if(key == 'h'):
            self.healTime = time.time()
            self.healStart()
        if(time.time() - self.healTime >= 5):
            self.healEnd()

        if(key == 'x'):
            self.narikey()

        if(key == ' '):
            self.king.attack(self, self.townhall, Hut, Canon, Wall)

        # clear board
        self.board(rows, columns)

        # render all buildings
        for building in Building.buildingList:
            self.colorArray = building.render(self.colorArray)
            self.idArray = building.idUpdate(self.idArray)

        self.king.move(key, self.idArray)
        self.colorArray = self.king.render(self.colorArray)
        self.idArray = self.king.idUpdate(self.idArray)

        for cannon in Canon.canonsList:
            cannon.shoot(self.king, Barbarians)

        for barbarian in Barbarians.barbariansList:
            barbarian.choose(Building)
            barbarian.move(self.idArray)
            self.colorArray = barbarian.render(self.colorArray)
            self.idArray = barbarian.idUpdate(self.idArray)

        if(self.checkVictory()==True):
            self.colorArray= [[Back.LIGHTGREEN_EX + " " + Style.RESET_ALL for _ in range(columns)]for _ in range(rows)]
            for i in range(8):
                self.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.GREEN + victory[i] + Style.RESET_ALL
            return False
        if(self.checkDefeat()==True):
            self.colorArray= [[Back.LIGHTRED_EX + " " + Style.RESET_ALL for i in range(columns)]for j in range(rows)]
            for i in range(8):
                self.colorArray[int(rows/2)-1][int(columns/2)-4+i] = Back.LIGHTRED_EX + defeat[i] + Style.RESET_ALL
            return False # originally it didnt close

        print("\n".join(["".join(row) for row in self.colorArray]))
        return True

game = Game()
while game.render():
    pass
