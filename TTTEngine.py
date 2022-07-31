#Make the 3 by 3 board
from tokenize import String
from typing import List


def new_board():
    boardList = []
    for i in range(3):
        boardList.append([])
        for j in range(3):
            boardList[i].append("None")
    return boardList 

#Print the state of the board
print (new_board())

#Loop and ask players for moves
    #Player one then player two and repeat until game over
    #Moves update board
    #if three in a row exit loop

#Declare winner and ask to play again