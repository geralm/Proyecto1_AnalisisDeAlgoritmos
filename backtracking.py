import dominoes
from fuerzaBruta import check_tiles
from copy import deepcopy

solucion = []

def generar_solucion(board):
    global solucion
    i = 0
    j = 0
    k = 0
    tiles = [0] * n_tiles
    mirror = deepcopy(board)
    complete = False
    while i < len(solucion):
        if solucion[i] == 0 and mirror[j][k] != "V" and mirror[j][k+1] != "V":
            tiles[i] = [[board[j][k]]+[board[j][k+1]]]
            mirror[j][k] = "V"
            mirror[j][k+1] = "V"
            if not(check_tiles(tiles)):
                solucion[i-1] = 1
                generar_solucion(board)
            k += 2

            if i+1 < len(solucion) and (solucion[i+1] == 0 and len(board[0])-k == 1 or len(board[0])-k == 0):
                k = 0
                j += 1
            elif i+1 < len(solucion) and (solucion[i+1] == 1 and len(board)-j == 1 or k >= len(board[0])):
                j += 1
                k = 0
        elif solucion[i] == 1 and mirror[j][k] != "V" and len(board) > j+1 and mirror[j+1][k] != "V":
            tiles[i] = [[board[j][k]]+[board[j+1][k]]]
            if not(check_tiles(tiles)):
                solucion[i-1] = 1
                generar_solucion(board)
            mirror[j][k] = "V"
            mirror[j+1][k] = "V"
            k += 1

            if i+1 < len(solucion) and (solucion[i+1] == 0 and (len(board[0])-k == 1 or len(board[0])-k == 0)):
                k = 0
                j += 1
            elif i+1 < len(solucion) and (solucion[i+1] == 1 and (len(board)-j == 1 or len(board[0]) <= k)):
                j += 1
                k = 0
        else:
            k += 1
            if k >= len(board[0]) or (solucion[i] == 0 and (len(board[0])-k == 1 or len(board[0])-k == 0)):
                k = 0
                j += 1
                if j >= len(board):
                    i = len(solucion)
                    complete = False
                    break
                else:
                    continue
            else:
                continue

        if (solucion[i] == 0 and k+1 > len(board[0])) or (solucion[i] == 1 and j+1 > len(board)) or j >= len(board):
            solucion[i-1] = 1
            generar_solucion(board)
        else:
            complete = True

        i += 1

    if complete == True and check_tiles(tiles) == True:
        return True
    else:
        return False

def backtracking(board):
    global solucion
    if(board==False):
        return False
    solucion = [0] * n_tiles
    generar_solucion(board)
    return solucion

board = dominoes.create_puzzle(2)
n_tiles = int(len(board) * (len(board[0])/2))
print(board)
print(backtracking(board))
