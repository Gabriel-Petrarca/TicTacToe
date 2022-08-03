from tokenize import String
from typing import List
from webbrowser import get

#Make the 3 by 3 board
def new_board():
    boardList = []
    for i in range(3):
        boardList.append([])
        for j in range(3):
            boardList[i].append("-")
    return boardList 

#Print the state of the board
def render(board):
    from pprint import pprint
    for i in range(3):
        stringFormat = ("".join(board[i])).replace("", "|")
        pprint(stringFormat, width = 30)


#checks that move is within bounds
def check_move_bounds(num):
    while num < 1 or num > 9:
        print("Please enter a valid number")
        num = input()
    return num

#checks move for open square
def check_square(board, num):
        if num >= 1 and num <= 3:
            num-= 1
            if board[0][num] == "-":
                return True
        elif num >= 3 and num <= 6:
            num -= 4
            if board[1][num] == "-":
                return True
        elif num >= 7:
            num -= 7
            if board[2][num] == "-":
                return True

#returns the inputted move
def get_move():
    print("Grid is ordered 1 through 9 top to bottom. What is your move?")
    num = input()
    check_move_bounds(num)
    return num

# add moves to a new board
def make_move(board, num, String):
    while True:
        if num >= 1 and num <= 3 and check_square(board, num):
            num -= 1
            board[0][num] = String
            break
        elif num >= 4 and num <=6 and check_square(board, num):
            num -= 4
            board[1][num] = String
            break
        elif num >= 7 and check_square(board, num):
            num -= 7
            board[2][num] = String
            break
        else:
            print("square taken try again")
            num = input()
            num = int(num)
    return board

board = new_board()
a = 4
l = "X"
board = make_move(board, a, l)
board = make_move(board, a, l)
render(board)