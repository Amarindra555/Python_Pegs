from typing import List, Optional, Tuple
import re

def generateBoard(n):
    n = n.replace('X','1 ')
    n = n.replace('o','0 ')
    n = n.split()
    map_object = map(int, n)
    lst = list(map_object)
    return(lst)

def solve(board):
    if checkBoard(board):
        return True
    
    result = True
    step = 0
    direction = 'x'
    global output
    global count_possibilities
    count_possibilities = 0

    for i in range(len(board)):
        if i < len(board)-2:
            if board[i] and board[i+1] and not board[i+2]:
                count_possibilities += 1
                step = i
                direction = 'R'
        if i > 1:
            if board[i] and board[i-1] and not board[i-2]:
                count_possibilities += 1
                step = i
                direction = 'L'
    
    if count_possibilities == 0:
        result = False
    elif count_possibilities > 1:
        result = True
        makeMove(step, direction)
        output.append((step, direction))
    elif count_possibilities == 1:
        result = True
        makeMove(step,direction)
        output.append((step, direction))
    # print(count_possibilities)
    return result


def makeMove(position, direction):
    global gameBoard
    if direction == 'R':
        gameBoard[position] = 0
        gameBoard[position+1] = 0
        gameBoard[position+2] = 1
    elif direction == 'L':
        gameBoard[position] = 0
        gameBoard[position-1] = 0
        gameBoard[position-2] = 1
    # print(gameBoard)
def checkBoard(board):
    if sum(board) == 1:
        return True
    return False

def pegsSolution(gameBoard):
    count = 0
    global count_possibilities

    while solve(gameBoard) == True:
        count += 1
        if count > 10:
            break
        if(count_possibilities>1):
            break
    return output



n = str(input())
gameBoard = generateBoard(n)
output = []
count_possibilities = 0
output = pegsSolution(gameBoard)

if count_possibilities > 1:
    print("There are multiple solutions")
elif output == []:
    if checkBoard(gameBoard):
        print(output)
    else:
        print(None)
else:
    if checkBoard(gameBoard):
        print(output)
    else:
        print(None)