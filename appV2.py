from datetime import datetime
import random

def mostrarCartas(nombre):
    print(f"¡{nombre} mantén tus ojos bien abiertos mientras las cartas se mueven!")

    carta1=["Q", "♥"]#carta ganadora
    carta2=["8", "♣"]
    carta3=["J", "♦"]
    posiciones=["Q", "8", "J"]
    posicionGanadora=posiciones[0]
    posicionGanadora = random.choice(["Q", "8", "J"])
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
    
    movimientosIntercambio=random.sample(intercambios, 5) #movimientos
    for mueve in movimientosIntercambio:
        print(f"Intercambio {mueve}")
    cartaCorrecta(carta1, carta2, carta3, nombre, posicionGanadora)


def jugar():

    print("Adivina dónde está la reina de corazones")
    nombre=input("Ingrese su nombre de usuario: ").capitalize()
    accion=input(f"{nombre} seleccione jugar [J], tabla de posiciones [T], salir [S]: ").upper()
    puntosGanador=8
    while accion!="S":

        if accion!="S" and accion!="T" and accion!="J":
            print("Opcion no disponible en el Juego.")
        elif accion== "J":
            mostrarCartas(nombre)

        elif accion=="T":
            tablaPosiciones()

        accion=input(f"{nombre} seleccione jugar [J], tabla de posiciones [T], salir [S]: ").upper()

    if accion=="S":
        print("¡Adiós!")
    
def cartaCorrecta(carta1, carta2, carta3, nombre, posicionGanadora):
    opcionCarta=input("¿En cuál de las cartas está la reina de corazones? [I], [M], [D]: ").upper()
    

    while opcionCarta!="D" and opcionCarta!="M"  and opcionCarta!="I":
      opcionCarta=input("¿En cuál de las cartas está la reina de corazones? [I], [M], [D]: ").upper()
    
    
    if opcionCarta == posicionGanadora:
        puntosGanador=5
        print(f"{nombre}, la opcion {opcionCarta} es CORRECTA ¡Haz recibido +{puntosGanador} puntos!")
        fecha=datetime.now().strftime("%d/%m/%Y")
        hora=datetime.now().strftime("%H/%M")
        with open("puntajes.txt", "a") as puntaje:
            print(f"{nombre}, {puntosGanador} puntos. Jugada {fecha} {hora}", file=puntaje)
    elif opcionCarta =='I' or opcionCarta=='M':
        print("Lo siento perdedor(a) :-(")
        print("¡Gracias por jugar!")

    ordenFinal(carta1, carta2, carta3)

    
def tablaPosiciones():
    with open("puntajes.txt", "r") as puntajes:
        for points in puntajes:
            print(points.strip())
    
    
    

def ordenFinal(carta1, carta2, carta3):
        print("┌───┐ ┌───┐ ┌───┐")
        print(f"|{carta3[0]}  | |{carta2[0]}  | |{carta1[0]}  |")
        print(f"| {carta3[1]} | | {carta2[1]} | | {carta1[1]} |")
        print(f"|  {carta3[0]}| |  {carta2[0]}| |  {carta1[0]}|")
        print("└───┘ └───┘ └───┘")

jugar()