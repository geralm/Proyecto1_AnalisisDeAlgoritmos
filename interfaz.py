"""
Elaborado por: Adrian Vargas, Esteban Leiva
Fecha: 1/9/2021
"""

#------------------------------Importacion de librerías------------------------------------
from os import extsep
from typing import Collection, Tuple
import fuerzaBruta
import dominoes
import backtracking
from tkinter import *

#----------------------------definicion de variables globables----------------------------
CANTIDAD_FICHAS = 4
FILAS = CANTIDAD_FICHAS+1
COLUMNAS = CANTIDAD_FICHAS+2
ANCHOVENTANA =FILAS *100
ALTOVENTANA =((COLUMNAS//2)*100)+50
#------------------------------------------definicion de funciones----------------------
def hacerEspejo():
    mirror=[] #matriz espejo
    for i in range(COLUMNAS):
        vacio=[] #fila o columna vacía
        for j in range(FILAS):
            vacio.append(True) #agrega el valor siempre True
        mirror.append(vacio) #agrega
    return mirror
def pintarCuadros(cuadricula, resultados):
    """
    Funcion que resultados y me los acomodará en el cuadro los valores de los resultados
    Input: array de cuadrícula, y array de resultados
    Output: void [1, 1, 1, 1, 1, 1,      0, 0, 0,     1, 1, 0, 1, 1, 0]

    La idea del algoritmo de la interfaz es colocar las fichas hasta que logre encontrar campo 
    NO con precisión
    cuadricula[pfilas][pcolumnas].configure(background="SpringGreen2")
    cuadricula[pfilas][pcolumnas+1].configure(background="sky blue")  
    """
    espejo = hacerEspejo() #el espejo es para tener un control cuando puede pintarse un recuadro y cuando no
 
    indiceResultados = 0
    posfila=0 
    for i in espejo:
        posCol = 0
        for j in i:
            if j == True: #si es true significa que es una casilla en blanco
                if resultados[indiceResultados]==0:
                    try:
                        if espejo[posfila][posCol] and espejo[posfila+1][posCol]:
                            cuadricula[posfila][posCol].configure(background="SpringGreen2")
                            cuadricula[posfila+1][posCol].configure(background="SpringGreen2")
                            posCol+=2

                            espejo[posfila][posCol] = False
                            espejo[posfila+1][posCol] = False
                            indiceResultados+=1 #aumenta para determinar el siguiente resultado
                        else: 
                            print("Error al pintar los cuadros verdes ")
                    except:
                        break
                else: 
                    if espejo[posfila][posCol] and espejo[posfila][posCol+1]:
                        cuadricula[posfila][posCol].configure(background="sky blue")
                        cuadricula[posfila][posCol+1].configure(background="sky blue") 
                        posCol+=1
                        espejo[posfila][posCol] = False
                        espejo[posfila][posCol+1] = False
                        indiceResultados+=1 #aumenta para determinar el siguiente resultado   
                    else: 
                        print("Error al pintar los cuadros celestes")
        posfila+=1
    return True
def hacerCuadricula(root):
    """
    Funcion que me realizará la cuadrícula dependientemente de las fichas que me acomodará 
    Input: la ventana a modificar
    Output: la cuadrícula en forma de arreglo
    """
    cuadricula = []
    for i in range(COLUMNAS):
        col = [] #columnas cuadrícula
        for j in range(FILAS):
            recuadro = Entry(root) # aqui va un text variable
            recuadro.place(x = i*50, y = j*50, w=50, h = 50)
            col.append(recuadro)
        cuadricula.append(col)
    return cuadricula
def botonFuerzaB():
    """
    """
    global board
    global solucion
    board = dominoes.create_puzzle(CANTIDAD_FICHAS)
    solucion=fuerzaBruta.fuerza_bruta(board)
    print(solucion)
    print(len(solucion))
    mensaje = pintarCuadros(cuadricula, [0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])
    return 
#--------------------------------------Código principal---------------------------------------------
global root
board = []
solucion = []
root = Tk()
root.title("Análisis de algoritmos-Búsqueda de fuerza bruta y Backtraking")
x_ventana = root.winfo_screenwidth() // 2 - ANCHOVENTANA // 2
y_ventana = root.winfo_screenheight() // 2 - ALTOVENTANA // 2
posicion = str(ANCHOVENTANA) + "x" + str(ALTOVENTANA) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root.resizable(0,0)
botonSalir  = Button(root, text = "Salir", command =root.quit, bg = "red", fg="white", font="Arial")
botonSalir.place(x = ANCHOVENTANA-100, y = ALTOVENTANA-40,  w = 75,h = 30)
cuadricula= hacerCuadricula(root)
botonFuerzaBruta = Button(root, text="FB",command=lambda:botonFuerzaB(), bg="Yellow", fg="black")
botonFuerzaBruta.place(x = ANCHOVENTANA-100, y= ALTOVENTANA-100, w = 75, h= 30)
root.mainloop()
