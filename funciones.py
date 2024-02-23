import numpy as np
import random

#--------------------------------------------------------------------------------------------------------------

def presentacion():
    print("Hundiendo la Flota")
    nombre=input("Cual es tu nombre Capitan?\n\n\n").upper()
    print(f"El juego acaba de iniciar, BIENVENIDO CAPITAN {nombre}!\n\n Hemos generado 2 tableros Aleatorios con 4 barcos para cada participante.\n El juego te ira guiando mediante Prints e Inputs!\n\n MUCHA SUERTE")


#--------------------------------------------------------------------------------------------------------------
def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "__")
#--------------------------------------------------------------------------------------------------------------
def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "OO"
    return tablero
#--------------------------------------------------------------------------------------------------------------
def colocar_barcos(barcos, tablero):
    for barco in barcos:
        tablero = colocar_barco(barco, tablero)
    return tablero
#--------------------------------------------------------------------------------------------------------------
def disparar(casilla, tablero):
    if tablero[casilla] == "__":
        print("Agua")
        tablero[casilla] = "A!"
    elif tablero[casilla] == "OO":
        print("Tocado")
        tablero[casilla] = "XX"
    else:
        print("Ya has disparado aquí")
    return tablero
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------

def crear_barco_random(eslora):

    fila_a = random.randint(0,9)
    columna_a = random.randint(0,9)

    orientacion = random.choice(["S","O","E","N"])

    barco = [(fila_a, columna_a)]

    while len(barco) < eslora:
        match orientacion:
            case "O":
                columna_a -= 1 # columna_a = columna_a - 1
            case "E":
                columna_a += 1
            case "S":
                fila_a += 1
            case "N":
                fila_a -= 1
        barco.append((fila_a, columna_a))

    return barco

barcos = {"yatch": 4,
          "cruce": 3,
          "velero": 2,
          "optimis": 1}

def eslora():
    for k,v in barcos.items():
        print(v)