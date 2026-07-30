from datetime import datetime
import random

def mostrarCartas(nombre, existe):
    print(f"¡{nombre} mantén tus ojos bien abiertos mientras las cartas se mueven!")

    carta1=["Q", "♥"]#carta ganadora
    carta2=["8", "♣"]
    carta3=["J", "♦"]

    print("┌───┐ ┌───┐ ┌───┐")
    print(f"|{carta1[0]}  | |{carta2[0]}  | |{carta3[0]}  |")
    print(f"| {carta1[1]} | | {carta2[1]} | | {carta3[1]} |")
    print(f"|  {carta1[0]}| |  {carta2[0]}| |  {carta3[0]}|")
    print("└───┘ └───┘ └───┘")
    
    input("Presione enter: ")

    print("┌───┐ ┌───┐ ┌───┐")
    print("|   | |   | |   |")
    print("| ? | | ? | | ? |")
    print("|   | |   | |   |")
    print("└───┘ └───┘ └───┘")
    intercambios=[

        ("I", "M", "izquierda (I) con la del medio (M)"),

        ("D", "M", "derecha (D) con la del medio (M)"),
        ("M", "I", "la del medio (M) con izquierda (I)"),
        ("D", "I", "derecha (D) con izquierda (I)"),
        ("I", "D", "izquierda (I) con derecha (D)"),
        ]
    posiciones = {"I": "Q♥", 
                  "M": "8♣", 
                  "D": "J♦"}
    
    movimientosIntercambio = random.sample(intercambios, 5)

    for pos1, pos2, descripcion in movimientosIntercambio:
        print(f"Intercambio {descripcion}...")
        aux=posiciones[pos1]
        posiciones[pos1]=posiciones[pos2]
        posiciones[pos2]=aux
    
    for posicion, carta in posiciones.items():
        if carta == "Q♥":
            posicionGanadora=posicion
            break
    
    
    cartaCorrecta(nombre, posicionGanadora, posiciones, existe)


def jugar():

    print("Adivina dónde está la reina de corazones")
    nombre=input("Ingrese su nombre de usuario: ").capitalize()
    accion=input(f"{nombre} seleccione jugar [J], tabla de posiciones [T], salir [S]: ").upper()
    while accion!="S":

        if accion!="S" and accion!="T" and accion!="J":
            print("Opcion no disponible en el Juego.")
        elif accion== "J":
            existe=jugador(nombre)
            mostrarCartas(nombre, existe)

        elif accion=="T":
            tablaPosiciones()

        accion=input(f"{nombre} seleccione jugar [J], tabla de posiciones [T], salir [S]: ").upper()

    if accion=="S":
        print("¡Adiós!")



def cartaCorrecta(nombre, posicionGanadora, posiciones, existe):
    opcionCarta=input("¿En cuál de las cartas está la reina de corazones? [I], [M], [D]: ").upper()
    

    while opcionCarta!="D" and opcionCarta!="M"  and opcionCarta!="I":
      opcionCarta=input("¿En cuál de las cartas está la reina de corazones? [I], [M], [D]: ").upper()

    print("Elegiste:", opcionCarta)
    print("La posición ganadora era:", posicionGanadora)
    
    puntosGanador=5
    fecha=datetime.now().strftime("%d/%m/%Y")
    hora=datetime.now().strftime("%H:%M")

    if opcionCarta == posicionGanadora:
        puntosTotal=0
        if existe:
                puntos=sumarPuntos()
                puntosTotal=(puntos[nombre])+5
        else:
            puntosTotal=puntosGanador

        print(f"{nombre}, la opcion {opcionCarta} es CORRECTA ¡Has recibido +{puntosGanador} puntos!")
        

        with open("puntajes.txt", "r") as puntaje:
            lineas=[]
            for i in puntaje:
                if existe:
                    lineas.append(f"{nombre}, {puntosTotal} puntos. Jugada {fecha} {hora}\n")
                else:
                    lineas.append(i)
        if not existe:
            lineas.append(f"{nombre}, {puntosTotal} puntos. Jugada {fecha} {hora}\n")



        with open("puntajes.txt", "w") as puntaje:
            for i in lineas:
                print(i, file=puntaje)
            

    elif opcionCarta =='I' or opcionCarta=='M':
        print("Lo siento perdedor(a) :-(")
        print("¡Gracias por jugar!")

    
    ordenFinal(posiciones)

    
def tablaPosiciones():
    lista=[]
    with open("puntajes.txt", "r") as puntajes:
        for points in puntajes:
            lista.append(points.strip())

    lista.sort(key=lambda x:int(x.split(",")[1].split()[0]), reverse=True)

    with open("puntajes.txt", "w") as puntaje:
        for i in lineas:
            print(i, end="", file=puntaje)

    with open("puntajes.txt", "r") as puntaje:
            for i in puntaje:
                print(i)
    
    
def jugador(nombre):
    with open("puntajes.txt", "r") as archivo:
        existe=False
        for i in archivo:
            if nombre in i:
                existe=True
                break

        return existe

def sumarPuntos():
    with open("puntajes.txt", "r") as archivo:
        puntos={}
        for i in archivo:
            jugador=i.strip().split(",")
            puntosJugador=jugador[1].split()
            puntos[jugador[0]]=int(puntosJugador[0])
        return puntos


def ordenFinal(posiciones):

    valorIzq=posiciones["I"][0]
    llaveIzq=posiciones["I"][1]
    
    valorMedio=posiciones["M"][0]
    llaveMedio=posiciones["M"][1]
    
    valorDer=posiciones["D"][0]
    llaveDer=posiciones["D"][1]

    print("┌───┐ ┌───┐ ┌───┐")
    print(f"|{valorIzq}  | |{valorMedio}  | |{valorDer}  |")
    print(f"| {llaveIzq} | | {llaveMedio} | | {llaveDer} |")
    print(f"|  {valorIzq}| |  {valorMedio}| |  {valorDer}|")
    print("└───┘ └───┘ └───┘")

jugar()