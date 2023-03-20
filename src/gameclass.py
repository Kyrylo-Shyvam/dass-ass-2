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
        
    def render(self):
        key = input_to(Get())
        os.system('clear')

        if(key == 'r'):
            self.rageTime = time.time()
            self.rageStart()
        if(time.time() - self.rageTime>=5):
            self.rageEnd()
            self.rageTime = time.time()

        # clear board
        self.board(rows, columns)

        self.king.move(key, self.idArray)
        self.colorArray = self.king.render(self.colorArray)
        self.idArray = self.king.idUpdate(self.idArray)

        # render all buildings
        buildings = Building.buildingList
        for i in range(len(buildings)):
            self.colorArray = buildings[i].render(self.colorArray)
            self.idArray = buildings[i].idUpdate(self.idArray)

        print("\n".join(["".join(row) for row in self.colorArray]))

game = Game()
while 1:
    game.render()
