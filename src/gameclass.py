import colorama
from colorama import Back, Style
import os
colorama.init(autoreset=True)
columns = 80
rows = 40

class Game:
    def __init__(self, rows, columns):
        self.color = Back.LIGHTGREEN_EX + " " + Style.RESET_ALL
        self.colorArray= [[self.color for _ in range(columns)] for _ in range(rows)]
        self.idArray = [[0 for _ in range(columns)] for _ in range(rows)]       

    def board(self,rows,columns):
        self.colorArray = [[self.color for _ in range(columns)] for _ in range(rows)]
        self.colorArray = [[self.color for _ in range(columns)] for _ in range(rows)]
        self.idArray = [[0 for _ in range(columns)] for _ in range(rows)]
        
    def render(self):
        os.system('cls||clear')
        print("\n".join(["".join(row) for row in self.colorArray]))
