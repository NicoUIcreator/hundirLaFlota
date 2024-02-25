
import funciones as f
import numpy as np
import random
from PIL import Image
import matplotlib.pyplot as plt



while True:
    f.menu()
    numero= int(input("que elegis?\n"))

    if numero ==1:

        tableroUsuario = f.crear_tablero()
        tableroMaquina = f.crear_tablero()
        tableroAtaque= f.crear_tablero()

        barcosUsuario = {"yatch1": f.crear_barco_random(4),
          "cruce1": f.crear_barco_random(3),
          "cruce2": f.crear_barco_random(3),
          "velero1": f.crear_barco_random(2),
          "velero2": f.crear_barco_random(2),
          "velero3": f.crear_barco_random(2),
          "optimis1": f.crear_barco_random(1),
          "optimis2": f.crear_barco_random(1),
          "optimis3": f.crear_barco_random(1),
          "optimis4": f.crear_barco_random(1)}
        
        barcosMaquina = {"yatch1": f.crear_barco_random(4),
          "cruce1": f.crear_barco_random(3),
          "cruce2": f.crear_barco_random(3),
          "velero1": f.crear_barco_random(2),
          "velero2": f.crear_barco_random(2),
          "velero3": f.crear_barco_random(2),
          "optimis1": f.crear_barco_random(1),
          "optimis2": f.crear_barco_random(1),
          "optimis3": f.crear_barco_random(1),
          "optimis4": f.crear_barco_random(1)}


        f.crearJuego(barcosUsuario,tableroUsuario)
        f.crearJuego(barcosMaquina,tableroMaquina)


        
        f.presentacion()

        print("Este es tu Tablero! ")

        print(tableroUsuario)
        print("-----------------------------------------------------------------------------------------------------------")

        def OCULTO(tableroMaquina):
             
            print("Tablero de la Máquina:")
            tableroOculto = np.where(tableroMaquina == 1, 0, tableroMaquina)
            return print(tableroOculto)
        
        OCULTO(tableroMaquina)

        

        while np.any(tableroUsuario != "OO") or np.any(tableroMaquina != "OO"):

            f.turnoUsuario(tableroMaquina)

            f.turnoMaquina(tableroUsuario)

            
            

            

            if np.any(tableroUsuario == "OO"):
                 print("perdiste! te han hundido los barcos!")
                 break
            elif np.any(tableroMaquina == "OO"):
                 print("GANASTE!!")
                 break

            f.mostrarUsuario(tableroUsuario)



    if numero==2:
        f.instrucciones()

    elif numero==3:
        exit()


    else:
            print("tiene que ser una opcion del Menu!\n")
    break
#tablero = f.crearTablero()

#barco1= f.colocarBarco()
#barco2= f.colocarBarco()

#tablero = f.colocarBarco()

#tablero = f.disparo()