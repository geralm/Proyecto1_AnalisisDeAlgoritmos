import dominoes
from fuerzaBruta import check_tiles
from copy import deepcopy

solucion = []

def get_0(k):
    i =0
    while i >= 0:
        k -= 1
        if solucion[k] == 0:
            return k
    return False


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
            if not(check_tiles(tiles)):
                if j+1 >= len(board):
                    solucion[get_0(i)] = 1
                    return generar_solucion(board)
                if solucion[i-1] == 1:
                    solucion[i] = 1
                    return generar_solucion(board)

                solucion[i-1] = 1
                return generar_solucion(board)
            mirror[j][k] = "V"
            mirror[j][k+1] = "V"
            k += 2

            if i+1 < len(solucion) and (solucion[i+1] == 0):
                if len(board[0])-k == 1 and mirror[j][k] != "V":
                    solucion[i+1] = 1
                    return generar_solucion(board)
                elif len(board[0])-k == 0:
                    k = 0
                    j += 1
                elif k+1 < len(board[0]) and mirror[j][k+1] == "V":
                    solucion[i+1] = 1
                    return generar_solucion(board)
                
            elif i+1 < len(solucion) and (solucion[i+1] == 1 and len(board)-j == 1 or k >= len(board[0])):
                j += 1
                k = 0
        elif solucion[i] == 1 and mirror[j][k] != "V" and len(board) > j+1 and mirror[j+1][k] != "V":
            tiles[i] = [[board[j][k]]+[board[j+1][k]]]
            if not(check_tiles(tiles)):
                solucion[get_0(i)] = 1
                return generar_solucion(board)
            mirror[j][k] = "V"
            mirror[j+1][k] = "V"
            k += 1

            if i+1 < len(solucion) and (solucion[i+1] == 0):
                if len(board[0])-k == 1 and mirror[j][k] != "V":
                    solucion[i+1] = 1
                    return generar_solucion(board)
                elif len(board[0])-k == 0:
                    k = 0
                    j += 1
                elif k+1 < len(board[0]) and mirror[j][k+1] == "V":
                    solucion[i+1] = 1
                    return generar_solucion(board)
                elif j+1 >= len(board) and solucion[i] == 1:
                    solucion[i] = 0
                    solucion[get_0(i)] = 1
                    return generar_solucion(board)
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

        i += 1

    if check_tiles(tiles):
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

board = dominoes.create_puzzle(3)
n_tiles = int(len(board) * (len(board[0])/2))
print(board)
print(backtracking(board))
