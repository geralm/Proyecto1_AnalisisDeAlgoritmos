"""
Elaborado por: Adrian Vargas, Esteban Leiva
Fecha: 1/9/2021
"""

#------------------------------Importacion de librerías------------------------------------
from typing import Collection
import fuerzaBruta
import dominoes
from tkinter import *

#----------------------------definicion de variables globables----------------------------
CANTIDAD_FICHAS = 4
FILAS = CANTIDAD_FICHAS+1
COLUMNAS = CANTIDAD_FICHAS+2
ANCHOVENTANA =FILAS *100
ALTOVENTANA =((COLUMNAS//2)*100)+50
#------------------------------------------definicion de funciones----------------------

def pintarCuadros(cuadricula, resultados):
    """
    Funcion que resultados y me los acomodará en el cuadro los valores de los resultados
    Input: array de cuadrícula, y array de resultados
    Output: void [1, 1, 1, 1, 1, 1,      0, 0, 0,     1, 1, 0, 1, 1, 0]
    """
    if resultados == False:
        return False
    pfilas = 0 #posicion de las fichas (Funciona como un índice) en ------>   eje x
    pcolumnas=0 #posicion de las fichas (Funciona como un índice) en ------> eje y
    rpasado = 0 #significa el resultado pasado
    for i in resultados:
        if pfilas >= COLUMNAS:
            if rpasado == 1: #esto para que el programa sepa si el último valor fue vertical u horizontal
                #con el fin de avanzar uno o dos casillas hacia abao
                pcolumnas+=2 
            else: 
                pcolumnas+=1
            pfilas=0
        if (pcolumnas+1)>FILAS:
            return
        if i == 0: #va horizontal color verde
            cuadricula[pfilas][pcolumnas].configure(background="SpringGreen2")
            cuadricula[pfilas+1][pcolumnas].configure(background="SpringGreen2")
            rpasado=0
            pfilas+=2   
        if i == 1 : #van verticales color azul
            try:
                cuadricula[pfilas][pcolumnas].configure(background="sky blue")
                cuadricula[pfilas][pcolumnas+1].configure(background="sky blue")  
            except:
                pass
            rpasado=1
            pfilas+=1
        
     

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
#--------------------------------------Código principal---------------------------------------------
global root
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
board = dominoes.create_puzzle(CANTIDAD_FICHAS)
solucion=fuerzaBruta.fuerza_bruta(board)
print(solucion)
mensaje = pintarCuadros(cuadricula, solucion)
tkBoxMensaje = Entry(root)
tkBoxMensaje.place(x = 10, y = ALTOVENTANA-50,w= 200, h= 30)
if mensaje == False or mensaje == []: 
    tkBoxMensaje.insert(0, " No se pudo pintar los recuadros")
    tkBoxMensaje.configure(state= 'readonly')
root.mainloop()
