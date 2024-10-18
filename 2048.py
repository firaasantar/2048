import numpy as np
import random

board = np.zeros((4,4), dtype= int)


def printBoard(board):
    rows = len(board)
    col = len(board[0])
    for i in range(rows):
        for j in range(col):
            print(board[i][j], end = ' ')
        print()
    print('\n')

def emptyAmount(board):
    counter = 0
    rows = len(board)
    col = len(board[0])
    for i in range(rows):
        for j in range(col):
            if(board[i][j] == 0):
                counter += 1
    return counter

def addNumber(board):
    numberOptions = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    emptySpaces = emptyAmount(board)
    position = random.randint(0, emptySpaces - 1)
    rows = len(board)
    col = len(board[0])
    counter = 0
    breakBoolean = False
    for i in range(rows):
        for j in range(col):
            if(board[i][j] == 0):
                if(counter == position):
                    board[i][j] = numberOptions[random.randint(0,9)]
                    breakBoolean = True
                    break
                else:
                    counter += 1
        if(breakBoolean):
            break
        

def move(board, m, totalscore):
    rows = len(board)
    col = len(board[0])
    if(m == 'w'):
        for i in range(col):
            for j in range(1, rows):
                bo = True
                temp = j
                while(bo and temp > 0):
                    if (board[temp][i] == 0):
                        bo = False
                        break
                    elif(board[temp][i] == board[temp-1][i]):
                        board[temp-1][i] = 2*board[temp-1][i]
                        totalscore += board[temp-1][i]
                        board[temp][i] = 0
                        bo = False
                        break
                    elif(board[temp-1][i] == 0):
                        board[temp-1][i] = board[temp][i]
                        board[temp][i] = 0
                        temp -= 1
                    else:
                        bo = False
                        break
    elif(m == 's'):
        for i in range(col):
            for j in range(rows - 2, -1, -1):
                bo = True
                temp = j
                while(bo and temp < 3):
                    if (board[temp][i] == 0):
                        bo = False
                        break
                    elif(board[temp][i] == board[temp+1][i]):
                        board[temp+1][i] = 2*board[temp+1][i]
                        totalscore += board[temp+1][i]
                        board[temp][i] = 0
                        bo = False
                        break
                    elif(board[temp+1][i] == 0):
                        board[temp+1][i] = board[temp][i]
                        board[temp][i] = 0
                        temp += 1
                    else:
                        bo = False
                        break
    
    elif(m == 'a'):
        for i in range(rows):
            for j in range(1, col):
                bo = True
                temp = j
                while(bo and temp > 0):
                    if (board[i][temp] == 0):
                        bo = False
                        break
                    elif(board[i][temp] == board[i][temp-1]):
                        board[i][temp-1] = 2*board[i][temp-1]
                        totalscore += board[i][temp-1]
                        board[i][temp] = 0
                        bo = False
                        break
                    elif(board[i][temp-1] == 0):
                        board[i][temp-1] = board[i][temp]
                        board[i][temp] = 0
                        temp -= 1
                    else:
                        bo = False
                        break
                    
    elif(m == 'd'):
        for i in range(rows):
            for j in range(col - 2, -1, -1):
                bo = True
                temp = j
                while(bo and temp < 3):
                    if (board[i][temp] == 0):
                        bo = False
                        break
                    elif(board[i][temp] == board[i][temp+1]):
                        board[i][temp+1] = 2*board[i][temp+1]
                        totalscore += board[i][temp+1]
                        board[i][temp] = 0
                        bo = False
                        break
                    elif(board[i][temp+1] == 0):
                        board[i][temp+1] = board[i][temp]
                        board[i][temp] = 0
                        temp += 1
                    else:
                        bo = False
                        break
    else:
        return totalscore
    return totalscore


def checkOver(board):

    rows = len(board)
    col = len(board[0])
    if(emptyAmount(board) != 0):
        return False
    else:
        for i in range(rows):
            for j in range(col-1):
                if(board[i][j] == board[i][j+1]):
                    return False
            
        for i in range(col):
            for j in range(rows-1):
                if(board[j][i] == board[j+1][i]):
                    return False
        return True

def check2048(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == 2048):
                return True


def playGame(board):
    totalscore = 0
    addNumber(board)
    is2048 = False
    while(checkOver(board) == False):
        if(is2048):
            addNumber(board)
            printBoard(board)
            m = input('Enter w, a, s, d: ')
            if(m == 'stop'):
                break
            totalscore = move(board, m, totalscore)
        else:
            addNumber(board)
            printBoard(board)
            m = input('Enter w, a, s, d: ')
            if(m == 'stop'):
                break
            totalscore = move(board, m, totalscore)
            
            
            if(check2048(board)):
                print('Congrats for reaching 2048!!!\nWould you like to continue? (Yes/No)')
                cont = input()
                if(cont.lower() == 'no'):
                    break
                else:
                    is2048 = True
                
    print(f'Your total score is: {totalscore}')
    
playGame(board)
