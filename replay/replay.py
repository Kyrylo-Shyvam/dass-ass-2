import os
import sys

    
num=input("Number of the game to view: ")
file="./game"+num+".txt"

with open(file,'r') as f:
    rows=0
    List=[]
    
    for line in f.readlines():
        List.append(line)
        rows = rows+1
        if(rows%50==0):
            os.system('clear')
            print(''.join(List))
            os.system('sleep 1')
            List=[]

