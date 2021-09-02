"""
Elaborado por: Adrian Vargas, Esteban Leiva
Fecha: 1/9/2021
"""

#Importacion de librerías
from tkinter import * 

#definicion de variables globables
CANTIDAD_FICHAS = 6
FILAS = CANTIDAD_FICHAS+1
COLUMNAS = CANTIDAD_FICHAS+2
ANCHOVENTANA =FILAS *100
ALTOVENTANA =((COLUMNAS//2)*100)+50
#definicion de funciones
def hacerCuadricula(root):
    cuadricula = []
    for i in range(FILAS):
        for j in range(COLUMNAS):
            recuadro = Entry(root) # aqui va un text variable
            recuadro.place(x = i*50, y = j*50, w=50, h = 50)
            cuadricula.append(recuadro)
    return cuadricula
#Código principal
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
root.mainloop()