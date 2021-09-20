import dominoes
from fuerzaBruta import check_tiles
from copy import deepcopy

solucion = []

def get_0(k):
    aux = k
    k-=1
    while k >= 0:
        if solucion[k] == 0:
            return k
        k-=1
    return aux

def check_tiles(tiles):
    i = 0
    k = 1
    while(i != len(tiles)):
        j = k
        while(j != len(tiles)):
            if tiles[i] != 0 and tiles[j] != 0 and tiles[i] == tiles[j]:
                return i
            else:
                j += 1
        i += 1
        k += 1
    return True

def generar_solucion(board):
    global solucion
    i = 0
    j = 0
    k = 0
    tiles = [0] * n_tiles
    mirror = deepcopy(board)
    complete = False
    while i < len(solucion):
        #en caso de ser 0
        if solucion[i] == 0 and mirror[j][k] != "V" and mirror[j][k+1] != "V":
            tiles[i] = [[board[j][k]]+[board[j][k+1]]]
            repetida = check_tiles(tiles)
            if repetida != True:
                if solucion[i] == 1 and solucion[repetida] ==1:
                    solucion[i] = 0
                    solucion[repetida] = 0
                    solucion[get_0(i)] = 1
                    return generar_solucion(board)
                elif solucion[i] == 1 and solucion[repetida] == 0:
                    solucion[repetida] = 1
                    solucion[i] = 0
                    return generar_solucion(board)
                elif j+1 < len(board):
                    solucion[i] = 1
                    return generar_solucion(board)
                elif j+1 >= len(board) and solucion[repetida] == 1:
                    solucion[get_0(i)] = 1 
                    return generar_solucion(board)
                else:
                    solucion[repetida] = 1
                    return generar_solucion(board)

            mirror[j][k] = "V"
            mirror[j][k+1] = "V"
            k += 2

            if k >= len(board[0]):
                k = 0 
                j+=1

            if i+1 < len(solucion) and solucion[i+1] == 0 and mirror[j][k] != "V":
                if k+1 < len(board[0]) and mirror[j][k+1] == "V":
                    solucion[i+1] = 1
                    return generar_solucion(board)

                elif k+1 >= len(board[0]):
                    solucion[i+1] = 1
                    return generar_solucion(board)
                

        #en caso de ser 1                 
        elif solucion[i] == 1 and mirror[j][k] != "V" and len(board) > j+1 and mirror[j+1][k] != "V":
            tiles[i] = [[board[j][k]]+[board[j+1][k]]]
            repetida = check_tiles(tiles)
            if repetida != True:
                if solucion[i] == 1 and solucion[repetida] == 1:
                    solucion[i] = 0
                    solucion[repetida] = 0
                    solucion[get_0(i)] = 1
                    return generar_solucion(board)
                elif solucion[i] == 1 and solucion[repetida] == 0:
                    solucion[repetida] = 1
                    solucion[i] = 0
                    return generar_solucion(board)
                elif j+1 < len(board):
                    solucion[i] = 1
                    return generar_solucion(board)
                elif j+1 > len(board) and solucion[repetida] == 1:
                    solucion[get_0(i)] = 1
                    return generar_solucion(board)
                else:
                    solucion[repetida] = 1
                    return generar_solucion(board)

            mirror[j][k] = "V"
            mirror[j+1][k] = "V"
            k += 1

            if k >= len(board[0]):
                k = 0
                j += 1

            if i+1 < len(solucion) and solucion[i+1] == 0:
                if k+1 < len(board[0]) and mirror[j][k] != "V" and mirror[j][k+1] == "V":
                    solucion[i+1] = 1
                    return generar_solucion(board)

                elif k+1 >= len(board[0]):
                    solucion[i+1] = 1
                    return generar_solucion(board)

        elif solucion[i] == 0 and k+1 >= len(board[0]) and mirror[j][k] != "V":
            solucion[i] = 1
            return generar_solucion(board)

        elif solucion[i] == 1 and j+1 >= len(board):
            solucion[i] = 0
            return generar_solucion(board)
        else: 
            k+=1
            if k >= len(board[0]):
                k = 0
                j += 1
            if j > len(board):
                break
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


board = dominoes.create_puzzle(6)
n_tiles = int(len(board) * (len(board[0])/2))
print(board)
print(backtracking(board))
