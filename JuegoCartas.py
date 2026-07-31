from datetime import datetime
import random
from tabulate import tabulate


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
    
    posiciones = {"I": "Q♥", "M": "8♣", "D": "J♦"}
    
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

    cartaCorrecta(nombre, posicionGanadora, posiciones, existe) #le mando existe para que compare,  viene de linea 64

def jugar():

    print("Adivina dónde está la reina de corazones")
    nombre=input("Ingrese su nombre de usuario: ").capitalize()
    accion=input(f"{nombre} seleccione jugar [J], tabla de posiciones [T], salir [S]: ").upper()

    while accion!="S":

        if accion!="S" and accion!="T" and accion!="J":
            print("Opcion no disponible en el Juego.")
        elif accion== "J":
            existe=jugador(nombre) #Le mando nombre para que compare en el archivo, me retorna True o False en existe
            mostrarCartas(nombre, existe) #Le mando existe a funcion mostrarCartas para que lo envie a cartaCorrecta y sume puntos si existe.
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
    
    puntosGanador=5 #puntos por partida Ganada
    fecha=datetime.now().strftime("%d/%m/%Y")
    hora=datetime.now().strftime("%H:%M")

    if opcionCarta == posicionGanadora:
        puntosTotal=0

        #El siguiente if y else solo verifican si existe o no, en caso de que si le suma los puntos, en caso de que no le dan su primer puntaje 
        if existe: #si existe == True le suma puntosGanador a los puntos que tiene
                puntos=sumarPuntos() #esa funcion retorna un dic con nombre: puntos
                #EJ: puntos={"Luis": 25}
                puntosTotal=(puntos[nombre])+5
                ##EJ: si "Luis" existe entonces puntosTotal=(puntos[nombre])+5 seria puntosTotal=(puntos["Luis"])+5 y como del dic puntos["Luis"]=25 entonces puntosTotal=30
        else:#si el jugador no existe
            puntosTotal=puntosGanador

        print(f"{nombre}, la opcion {opcionCarta} es CORRECTA ¡Has recibido +{puntosGanador} puntos!")
        

        with open("puntajes.txt", "r") as puntaje:
            lineas=[]
            for i in puntaje: #Recorro el archivo para verficar si el usuario ya ha jugado o no.
                if i.split(",")[0].strip()==nombre: #Si al comparar el inicio de i con nombre (recordar que el formato es "nombre, punto ........") es True entonces agrego a la lista Lineas el jugador con sus puntos nuevos
                    lineas.append(f"{nombre}, {puntosTotal} puntos. Jugada {fecha} {hora}\n")
                else: #Si la comparacion es False lo agrego tal cual esta a la lista lineas
                    lineas.append(i)

        if not existe: #si es un jugador nuevo en el juego 
            lineas.append(f"{nombre}, {puntosTotal} puntos. Jugada {fecha} {hora}\n")



        with open("puntajes.txt", "w") as puntaje: #Reescribo el archivo, con W se borra todo y con el for recorro la lista y lo agrego al archivo
            for i in lineas:
                puntaje.write(i)
            

    elif opcionCarta =='I' or opcionCarta=='M':
        print("Lo siento perdedor(a) :-(")
        print("¡Gracias por jugar!")

    
    ordenFinal(posiciones)
    

def tablaPosiciones():
    lista = []

    with open("puntajes.txt", "r") as puntajes:
        for puntos in puntajes:
            lista.append(puntos.strip())#Recorro el archivo y guardo cada linea en la lista
    print(lista)
    lista.sort(key=lambda x: int(x.split(",")[1].split()[0]), reverse=True) #Ordeno por el puntaje accediendo a el con x.split(",")[1].split()[0] 

    with open("puntajes.txt", "w") as puntaje:#Reescribo el archivo borrando todo y vaceando la lista en el
        for i in lista:
            puntaje.write(i + "\n")


    tabla=[]
    for i, dato in enumerate(lista, start=1):
        datos=dato.split(",")
        nombre=datos[0]
        datos2=datos[1].split(".") 
        puntos=datos2[0] 
        jugada=datos2[1].split()
        hora=jugada[-1]
        fecha=jugada[-2]
        tabla.append([i,nombre, puntos, fecha, hora])

    print("\n--------Tabla de posiciones--------\n")

    print(tabulate(
        tabla, 
        headers=["Posicion", "Nombre", "Puntos Obtenidos", "Fecha Ultima jugada", "Hora Ultima jugada"],
        tablefmt="grid"
        ))
    print()
        


    """" Por si no funciona el tabulate
    with open("puntajes.txt", "r") as puntaje:#Muestro los puntajes
        print("\n--------Tabla de posiciones--------\n")
        for i in puntaje:
            print(i, end="")
        print()
    """
        

def jugador(nombre):
    with open("puntajes.txt", "r") as archivo:
        existe=False
        for i in archivo: #Recorro el archivo, si existe lo hago True y salgo del recorrido
            if i.split(",")[0].strip() == nombre:
                existe=True
                break
    return existe #Retorno True o False para usar en 

def sumarPuntos():
    with open("puntajes.txt", "r") as archivo:
        puntos={} #Diccionario que solo guardara nombre y puntos
        for i in archivo:
            i=i.strip()
            if i=="":
                continue
            jugador=i.split(",")
            puntosJugador=jugador[1].split()
            puntos[jugador[0]]=int(puntosJugador[0]) #jugador[0] guarda el nombre y puntosJugador[0] guarda el puntaje y eso lo agrego al diccionario
        return puntos

def ordenFinal(posiciones):#Muestro el orden final de cartas

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