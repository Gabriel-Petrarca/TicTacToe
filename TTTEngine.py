#Make the 3 by 3 board
from tokenize import String
from typing import List
from webbrowser import get


def new_board():
    boardList = []
    for i in range(3):
        boardList.append([])
        for j in range(3):
            boardList[i].append("-")
    return boardList 

#Print the state of the board
def render(new_board):
    from pprint import pprint
    for i in range(3):
        stringFormat = ("".join(board[i])).replace("", "|")
        pprint(stringFormat, width = 30)


#Loop and ask players for moves
    #Player one then player two and repeat until game over
    #Moves update board
    #if three in a row exit loop
def get_move():
    print("Grid is ordered 1 through 9 top to bottom. What is your move?")
    num = input()
    while num <1 or num > 9:
        print("Please enter a valid number")
        num = input()
    return num
def make_move(board, int, String):
    if int >= 1 and int <= 3:
        board[0][int] = String
    if int >= 4 and int <=6:
        int -= 4
        board[1][int] = String
    if int >= 7:
        int -= 7
        board[2][int] = String
    return board
board = new_board()
test = 9
letter = "X"
board = make_move(board, test, letter)
render(board)