import os
from gameclass import Game

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

game = Game()

while(1):
    end = game.render()

    file_name=open(file,"a")
    file_name.write("\n".join(["".join(row) for row in game.colorArray]))
    file_name.write("\n")
    file_name.close()

    if(end):
        break
