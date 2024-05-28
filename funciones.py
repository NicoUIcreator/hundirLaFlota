import numpy as np
import random



def menu():
    print("Bienvenido a Hundir la Flota")
    print("1. Jugar")
    print("2. Ver instrucciones")
    print("3. Salir del juego\n")
    barco2()
    

def instrucciones():
    print("Instrucciones:")
    print("Tu objetivo es hundir los barcos de la máquina antes de que ella hunda los tuyos.")
    print("Durante tu turno, ingresa las coordenadas para disparar al tablero de la máquina.")
    print("El juego termina cuando uno de los jugadores hunde todos los barcos del otro.")
    input("Escribe 1 para jugar o 3 para salir\n")




#--------------------------------------------------------------------------------------------------------------

def presentacion():
    print("Hundiendo la Flota")
    nombre=input("Cual es tu nombre Capitan?\n\n\n").upper()
    print(f"El juego acaba de iniciar, BIENVENIDO CAPITAN {nombre}!\n\n Hemos generado 2 tableros Aleatorios con 10 barcos para cada participante.\n El juego te ira guiando mediante Prints e Inputs!\n\n MUCHA SUERTE")
    barcoNaval()

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
def disparar(casilla:tuple, tablero):
    if tablero[casilla] == "__":
        print("Agua")
        tablero[casilla] = "AA"
        return tablero, False
    elif tablero[casilla] == "OO":
        print("Tocado")

        tablero[casilla] = "X!"
        return tablero, True
    else:
        print("Ya has disparado aquí")

    return tablero, bool

#--------------------------------------------------------------------------------------------------------------
def verificar(x:dict):
    listabarcos=[]

    for clave, lista_tuplas in x.items():
    
        for tupla in lista_tuplas:
            listabarcos.append(tupla)
    return listabarcos
#--------------------------------------------------------------------------------------------------------------

def crear_barco_random(eslora):
    



    fila_a = random.randint(0,9)

    columna_a = random.randint(0,9)

    orientacion = random.choice(["S","O","E","N"])

    barco = [(fila_a, columna_a)]

    while len(barco) < eslora:
    
        match orientacion:

            case "O":
                 # columna_a = columna_a - 1
                if columna_a - (eslora-1) >= 0:
                    columna_a -= 1
                else:
                    orientacion = random.choice(["S","E","N"])


            case "E":
                
                if columna_a + (eslora-1) <= 9:

                    columna_a += 1
                else:

                    orientacion = random.choice(["O","N","S"])
                

            case "S":
                if fila_a + (eslora-1) <= 9:

                    fila_a += 1
                else:
                    orientacion = random.choice(["O","E","N"])

            case "N":
                if fila_a - (eslora-1) >= 0:
                    fila_a -= 1
                else:
                    orientacion = random.choice(["S","E","O"])

        barco.append((fila_a, columna_a))

        if barco[0] == barco[1]:
            crear_barco_random(2)
    

    return barco



barcos = {"yatch1": crear_barco_random(4),
          "cruce1": crear_barco_random(3),
          "cruce2": crear_barco_random(3),
          "velero1": crear_barco_random(2),
          "velero2": crear_barco_random(2),
          "velero3": crear_barco_random(2),
          "optimis1": crear_barco_random(1),
          "optimis2": crear_barco_random(1),
          "optimis3": crear_barco_random(1),
          "optimis4": crear_barco_random(1)}

barcosMaquina = {"yatch1": crear_barco_random(4),
          "cruce1": crear_barco_random(3),
          "cruce2": crear_barco_random(3),
          "velero1": crear_barco_random(2),
          "velero2": crear_barco_random(2),
          "velero3": crear_barco_random(2),
          "optimis1": crear_barco_random(1),
          "optimis2": crear_barco_random(1),
          "optimis3": crear_barco_random(1),
          "optimis4": crear_barco_random(1)}

def verificar(x:dict):

    listabarcos=[]

    for clave, lista_tuplas in x.items():
    
        for tupla in lista_tuplas:
            listabarcos.append(tupla)
    return listabarcos

def checkRepetidos(x:dict):

    while len(verificar(x)) != len(set(verificar(x))):
    
        x=crearBarcos()
    else:
        x

    return x

def colocarBarco(barco, tableroUsuario):


    
    for v,j in enumerate(barco):
        if tableroUsuario[j] == "OO":
    
            
            barco=crear_barco_random(len(barco))
            colocarBarco(barco, tableroUsuario)
            return tableroUsuario
        else:

            tableroUsuario[j] = "OO"
        
    return tableroUsuario

def colocarBarcos(barcos,tableroUsuario):
    
    for k,v in barcos.items():
        
        tableroUsuario = colocarBarco(v, tableroUsuario)

    return tableroUsuario


#--------------------------------------------------------------------------------------------------------------
#def colocar_barcos(barcos, tablero):
    for barco in barcos:
        tablero = colocar_barco(barco, tablero)
    return tablero

def mostrarUsuario(tablero):
    print("Tablero del Usuario:")
    print(tablero)
    
def mostrarOculto(tablero):
    print("Tablero de la Máquina:")
    tablero_oculto = np.where(tablero == "OO", "__", tablero)
    print(tablero_oculto)

def crearBarcos():
    
    barcos = {"yatch1": crear_barco_random(4),
            "cruce1": crear_barco_random(3),
            "cruce2": crear_barco_random(3),
            "velero1": crear_barco_random(2),
            "velero2": crear_barco_random(2),
            "velero3": crear_barco_random(2),
            "optimis1": crear_barco_random(1),
            "optimis2": crear_barco_random(1),
            "optimis3": crear_barco_random(1),
            "optimis4": crear_barco_random(1)}
    return barcos

def checkRepetidos(x:dict):

    while len(verificar(x)) != len(set(verificar(x))):
    
        x=crearBarcos()
    else:
        x

    return x

def crearJuego(x:dict,tablero):
    x = {"yatch1": crear_barco_random(4),
          "cruce1": crear_barco_random(3),
          "cruce2": crear_barco_random(3),
          "velero1": crear_barco_random(2),
          "velero2": crear_barco_random(2),
          "velero3": crear_barco_random(2),
          "optimis1": crear_barco_random(1),
          "optimis2": crear_barco_random(1),
          "optimis3": crear_barco_random(1),
          "optimis4": crear_barco_random(1)}
    checkRepetidos(x)
    colocarBarcos(x,tablero)
    return x,tablero


def turnoUsuario(tableroMaquina):
    while (np.any(tableroMaquina == "OO")):
        print("\nTurno del Usuario:")
        mostrarOculto(tableroMaquina)
    
        fila = int(input("Ingrese la fila para disparar: "))
        columna = int(input("Ingrese la columna para disparar: "))
        if tableroMaquina[fila, columna] == "OO":
            print("¡Has golpeado un barco!")
            tableroMaquina[fila, columna] = "X!"
            continue
        
        else:
            print("¡Agua!")
            tableroMaquina[fila, columna] = "AA"
        return tableroMaquina
        


def turnoMaquina(tableroUsuario):
    while (np.any(tableroUsuario == "OO")):

        print("\nTurno de la Máquina:")
        filaRandom=random.randint(0,9)
        columnaRandom=random.randint(0,9)
        

        if tableroUsuario[filaRandom, columnaRandom] == "OO":
            print("La máquina ha golpeado uno de tus barcos!")
            tableroUsuario[filaRandom, columnaRandom] = "X!"
            continue
        else:
            print("La máquina ha disparado al agua.")
            tableroUsuario[filaRandom, columnaRandom] = "AA"

        return tableroUsuario,mostrarUsuario(tableroUsuario)
    
    #def soloNumeros(numero):
def barcoNaval():
    return print('''                
                      |==|  |==|  |==|
                    __|__|__|__|__|__|_
                __|___________________|___
            __|__[]__[]__[]__[]__[]__[]__|___
            |............................o.../
            \.............................../
        ,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_)''')

def barco2():
    return print(''' .  o ..
 o . o o.o
      ...oo
        __[]__
     __|_o_o_o\__
     \""""""""""/
      \. ..  . /
 ^^^^^^^^^^^^^^^^^^^^''')