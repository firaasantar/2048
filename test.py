import random
import numpy as np

position = random.randint(0, 16)

print(type(position))


board = np.zeros((4,4), dtype= int)

boardtest = np.array([[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]])


'''
def emptyAmount(board):
    counter = 0
    rows = len(board)
    col = len(board[0])
    for i in range(rows):
        for j in range(col):
            if(board[i][j] == 0):
                counter += 1
    return counter
                
#print(emptyAmount(board))
rows = len(board)
col = len(board[0])

'''

def move(board, m, totalscore):
    rows = len(board)
    col = len(board[0])
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
                        print(totalscore)
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
    return totalscore

totalscore =0

totalscore = move(boardtest, 'w', totalscore)

print(boardtest)

print(totalscore)

totalscore =  move(boardtest, 'w', totalscore)

print(boardtest)

print(totalscore)