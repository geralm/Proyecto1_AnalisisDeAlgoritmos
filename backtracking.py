import dominoes
from copy import deepcopy

solucion = []
mirror = []
tiles = []
reg = []
error = False
j = 0
k = 0
board = []


def reset_regs_sol(i):
    global reg
    global solucion
    while i < len(solucion):
        reg[i] = False
        solucion[i] = 0
        i += 1


def check(i, n_tiles):
    global k
    global j
    if k >= len(board[0]):
        k = 0
        j += 1
        if j >= len(board) and check_tiles(tiles) == "T" and mirror_complete():
            return True
    if check_tiles(tiles) == "T" and mirror_complete():
        return True


def reset_tiles():
    global tiles
    i = 0
    while i < len(tiles):
        tiles[i] = 0
        i += 1


def poda(repetida, n_tiles):
    global k
    global j
    global mirror
    global tiles
    if solucion[repetida] == 1:
        solucion[repetida] = 0
    else:
        solucion[repetida] = 1
    reg[repetida] = True
    reset_tiles()
    reset_regs_sol(repetida+1)
    mirror = deepcopy(board)
    j = 0
    k = 0
    return generar_solucion(board, 0, n_tiles)


def mirror_complete():
    j = 0
    while j < len(board):
        k = 0
        while k < len(board[0]):
            if mirror[j][k] != "V":
                return False
            k += 1
        j += 1
    return True


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
    return "T"


def generar_solucion(board, i, n_tiles):
    global solucion
    global mirror
    global tiles
    global j
    global k
    if check(i, n_tiles):
        return True
    elif (mirror[j][k] != "V" and j+1 >= len(board) and k+1 >= len(board[0])) or (mirror[j][k] != "V" and j+1 >= len(board) and mirror[j][k+1] == "V"):
        if solucion[0] == 1:
            solucion[0] = 0
        else:
            solucion[0] = 1
        reg[0] = True
        reset_tiles()
        j = 0
        k = 0
        mirror = deepcopy(board)
        return generar_solucion(board, 0, n_tiles)
    elif solucion[i] == 0:
        if k+1 >= len(board[0]) and mirror[j][k] != "V":
            solucion[i] = 1
            reg[i] = True
            return generar_solucion(board, i, n_tiles)

        elif mirror[j][k] != "V" and mirror[j][k+1] == "V" and j+1 <= len(board):
            solucion[i] = 1
            reg[i] = True
            return generar_solucion(board, i, n_tiles)

        elif mirror[j][k] != "V" and mirror[j][k+1] != "V":
            tiles[i] = [[board[j][k]]+[board[j][k+1]]]
            repetida = check_tiles(tiles)
            if repetida != "T" and j+1 < len(board) and reg[i] == False:
                tiles[i] = [[board[j][k]]+[board[j+1][k]]]
                repetida_2 = check_tiles(tiles)
                if repetida_2 != "T":
                    return poda(repetida, n_tiles)
                else:
                    solucion[i] = 1
                    reg[i] = True
                    return generar_solucion(board, i, n_tiles)
            elif repetida != "T" and reg[repetida] == False:
                solucion[i] = 0
                reg[i] = False
                return poda(repetida, n_tiles)
            elif repetida != "T":
                return poda(repetida-1, n_tiles)
            mirror[j][k] = "V"
            mirror[j][k+1] = "V"
            k += 2
            return generar_solucion(board, i+1, n_tiles)

        else:
            k += 1
            return generar_solucion(board, i, n_tiles)

    elif solucion[i] == 1:
        if j+1 >= len(board):
            solucion[i] = 0
            reg[i] = True
            return generar_solucion(board, i, n_tiles)

        elif mirror[j][k] != "V" and mirror[j+1][k] != "V":
            tiles[i] = [[board[j][k]]+[board[j+1][k]]]
            repetida = check_tiles(tiles)
            if repetida != "T" and k+1 < len(board[0]) and reg[i] == False:

                tiles[i] = [[board[j][k]]+[board[j][k+1]]]
                repetida_2 = check_tiles(tiles)
                if repetida_2 != "T":
                    solucion[i] = 0
                    return poda(repetida, n_tiles)
                else:
                    solucion[i] = 0
                    reg[i] = True
                    return generar_solucion(board, i, n_tiles)
            elif repetida != "T" and reg[repetida] == False:
                solucion[i] = 0
                reg[i] = False
                return poda(repetida, n_tiles)

            elif repetida != "T":
                return poda(repetida-1, n_tiles)

            mirror[j][k] = "V"
            mirror[j+1][k] = "V"
            k += 1
            return generar_solucion(board, i+1, n_tiles)
        else:
            k += 1
            return generar_solucion(board, i, n_tiles)
    else:
        k += 1
        return generar_solucion(board, i, n_tiles)


def backtracking(tablero):
    global solucion
    global tiles
    global mirror
    global reg
    board = tablero
    n_tiles = int(len(board) * (len(board[0])/2))
    if(board == False):
        return False
    solucion = [0] * n_tiles
    tiles = [0] * n_tiles
    reg = [False] * n_tiles
    mirror = deepcopy(board)
    if generar_solucion(board, 0, n_tiles):
        return solucion
