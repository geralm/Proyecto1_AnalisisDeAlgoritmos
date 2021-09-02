import dominoes
from copy import deepcopy
import sys

board = dominoes.create_puzzle(2)

def check_tiles(tiles):
    i = 0
    k = 1
    while(i != len(tiles)):
        j = k
        while(j != len(tiles)):
            if tiles[i] == tiles[j]:
                return False
            else:
                j += 1
        i += 1
        k+=1
    return True

"""
2 2 1 3 0 
0 2 0 2 1 
0 0 1 3 2 
3 3 1 3 1 

"""

def fuerza_bruta(board):
    i = 0
    j = 0
    solution = []
    tiles = []
    ori = 0
    n_tiles = int(len(board) * (len(board[0])/2))
    sol = [None] * n_tiles
    solucion = generateAllBinaryStrings(n_tiles,board,0,sol)
    return solucion


def arreglo_binario(A, n, board): 
    i = 0 
    j = 0
    k = 0
    mirror = deepcopy(board)
    tiles = []
    complete = False
    while i < len(A):

        if A[i] == 0 and mirror[j][k] != "V" and mirror[j][k+1] != "V":
            tiles += [[board[j][k]]+[board[j][k+1]]]
            mirror[j][k] = "V"
            mirror[j][k+1] = "V"
            k+=2

            if i+1 < len(A) and  (A[i+1] == 0 and len(board[0])-k == 1 or len(board[0])-k == 0):
                k=0
                j+=1
            elif i+1 < len(A) and (A[i+1] == 1 and len(board)-j == 1 or k > len(board[0])):
                j+=1
                k=0
        elif A[i] == 1 and mirror[j][k] != "V" and len(board) > j+1 and mirror[j+1][k] != "V":
            tiles += [[board[j][k]]+[board[j+1][k]]]
            mirror[j][k] = "V"
            mirror[j+1][k] ="V"
            k+=1

            if i+1 < len(A) and (A[i+1] == 0 and (len(board[0])-k == 1 or len(board[0])-k == 0)):
                k = 0
                j += 1
            elif i+1 < len(A) and (A[i+1] == 1 and (len(board)-j == 1 or len(board[0]) <= k)):
                j+=1
                k=0
        else:
            k+=1
            if k >= len(board[0]) or (A[i] == 0 and (len(board[0])-k == 1 or len(board[0])-k == 0)):
                k = 0
                j += 1
                if j>=len(board):
                    i = len(A)
                    complete = False
                    break
                else: 
                    continue
            else:
                continue

        if (A[i] == 0 and k+1 > len(board[0])) or (A[i] == 1 and j+1 > len(board)) or j >= len(board):
                i = len(A)
                complete = False
                break
        else:
            complete = True

        i+=1      
    if complete == True:
        if check_tiles(tiles) == True:
            return A

def generateAllBinaryStrings(n, board, i,A):
    
    if i == n:
        if arreglo_binario(A,n,board) != None:
            return arreglo_binario(A,n,board)
        return
    A[i] = 0
    generateAllBinaryStrings(n,board, i + 1, A)

    A[i] = 1
    generateAllBinaryStrings(n, board, i + 1, A)
print(board)
print(fuerza_bruta(board))