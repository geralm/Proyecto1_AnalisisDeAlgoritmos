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
CANTIDAD_FICHAS =4
FILAS = CANTIDAD_FICHAS+1
COLUMNAS = CANTIDAD_FICHAS+2
ANCHOVENTANA =FILAS *100 +100
ALTOVENTANA =((COLUMNAS//2)*100)+50+200

#------------------------------------------definicion de funciones----------------------

def hacerEspejo():
    mirror=[] #matriz espejo
    for i in range(COLUMNAS*FILAS):
        mirror.append(-1) #agrega
    return mirror
def revisarEspejo(espejo):
    """
    Retorna verdadero si el espejo aún tiene campos disponibles
    """
    for i in espejo:
        if i==-1:
            return True
    return False
def reset(cuadricula):
    for i in cuadricula:
        i.configure(bg="white")
        i.delete (0, 11 )
    return True
def pintarCuadros(cuadricula, resultados, tablero):
    """
    Funcion que resultados y me los acomodará en el cuadro los valores de los resultados
    Input: array de cuadrícula, y array de resultados
    Output: void [1, 1, 1, 1, 1, 1,      0, 0, 0,     1, 1, 0, 1, 1, 0]
    """
    global root
    reset(cuadricula)
    espejo = hacerEspejo() #el espejo es para tener un control cuando puede pintarse un recuadro y cuando no
    indiceResultados= 0 
   
    while revisarEspejo(espejo):
        indiceCuadro=0
        if indiceResultados >= FILAS*(COLUMNAS/2):
            return
        while espejo[indiceCuadro]!=-1:
            indiceCuadro+=1
        if resultados[indiceResultados]==0: #horizontal

            espejo[indiceCuadro]=0 
            espejo[indiceCuadro+1]=0
        else: 
            espejo[indiceCuadro+COLUMNAS]=1
            espejo[indiceCuadro]=1 
        indiceResultados+=1
    indice=0
    for i in tablero:
        for j in i: 
            cuadricula[indice].configure(font=("Arial",14))
            cuadricula[indice].insert(10,"   ")
            cuadricula[indice].insert(10,j)
            
            indice+=1
    i = 0       
    while i<len(espejo): 
        if espejo[i]==0:
            cuadricula[i].configure(background="SpringGreen2")
        else:
            cuadricula[i].configure(background="sky blue")
        i+=1
        root.after(50)
        root.update()  
    return True
    
def hacerCuadricula(root):
    """
    Funcion que me realizará la cuadrícula dependientemente de las fichas que me acomodará 
    Input: la ventana a modificar
    Output: la cuadrícula en forma de arreglo
    """
    cuadricula = []
    
    for i in range(2,FILAS+2):
       
        for j in range(3,COLUMNAS+3):
            recuadro = Entry(root) # aqui va un text variable
            recuadro.place(x = j*50, y = i*50, w=50, h = 50)
            cuadricula.append(recuadro)
    return cuadricula
def botonFuerzaB():
    global board
    global solucion
    global mensajeEntry
    mensajeEntry.delete(0,100)
    board = dominoes.create_puzzle(CANTIDAD_FICHAS)
    print(board)
    solucion=fuerzaBruta.fuerza_bruta(board)
    print(solucion)
    
    try:
        mensaje=pintarCuadros(cuadricula, solucion, board)
    except:
        mensajeEntry.insert(0,"La cuadricula no pudo resolverse, intente de nuevo")
   
    return 
def botonBT():
    global solucion
    global root
    global mensajeEntry
    mensajeEntry.delete(0,100)
    i=0
    while True and i<50:
        try:
            board=dominoes.create_puzzle(CANTIDAD_FICHAS)
            solucion= backtracking.backtracking(board)
            break
        except:
            i+=1
            pass
    print(board)
    print(solucion)
    try:
        mensaje=pintarCuadros(cuadricula, solucion, board)
    except:
        mensajeEntry.insert(0,"La cuadricula no pudo resolverse, intente de nuevo")
    return
#--------------------------------------Código principal---------------------------------------------
global root
global mensajeEntry
board = []
solucion = []
root = Tk()
root.title("Análisis de algoritmos-Búsqueda de fuerza bruta y Backtraking")
root.configure(background="Purple4")
x_ventana = root.winfo_screenwidth() // 2 - ANCHOVENTANA // 2
y_ventana = root.winfo_screenheight() // 2 - ALTOVENTANA // 2
posicion = str(ANCHOVENTANA) + "x" + str(ALTOVENTANA) + "+" + str(x_ventana) + "+" + str(y_ventana)
root.geometry(posicion)
root.resizable(0,0)
#titulos
labeltitulo=Label(root, text="Dominoes",bg="purple1", fg="white")
labeltitulo.configure(font=("verdana",24))
labeltitulo.place(x=(ANCHOVENTANA/3)+10, y=10)
#botonsalir
botonSalir  = Button(root, text = "Salir", command =root.quit, bg = "red", fg="white", font="Arial")
botonSalir.place(x = ANCHOVENTANA-100, y = ALTOVENTANA-70,  w = 75,h = 40)
#cuadricula
cuadricula= hacerCuadricula(root)
#boton fuerza bruta
botonFuerzaBruta = Button(root, text="Fuerza Bruta",command=lambda:botonFuerzaB(), bg="wheat2", fg="black")
botonFuerzaBruta.place(x = 3*50, y= ALTOVENTANA-70, w = 100, h= 40)
#boton backtraking
botonBacktracking = Button(root, text= "Backtracking", command=lambda:botonBT(), bg="LightYellow2", fg="Black")
botonBacktracking.place(x=COLUMNAS*50+50, y=ALTOVENTANA-70, w=100, h=40)
##
mensajeEntry = Entry(root)
mensajeEntry.place(x=(ANCHOVENTANA/3)-40, y=55, w=300,h=35)
root.mainloop()
