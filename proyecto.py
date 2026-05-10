puntosGanador=10
print("Adivina dónde está la reina de corazones")

U=input("Ingrese su nombre de usuario: ").capitalize()

ac=input(f"{U} seleccione jugar [J], tabla de posiciones [T], salir [S]: ").upper()
#sea ac la accion que desea el usuario U

if ac!= "J" and ac!= "T" and ac!= "S":
    print("Opcion no disponible en el Juego.")
elif ac== "J":
  print(f"¡{U} mantén tus ojos bien abiertos mientras las cartas se mueven!")
  c1=["Q", "♥"]#carta ganadora
  c2=["8", "♣"]
  c3=["J", "♦"]
  print("┌───┐ ┌───┐ ┌───┐")
  print(f"|{c1[0]}  | |{c2[0]}  | |{c3[0]}  |")
  print(f"| {c1[1]} | | {c2[1]} | | {c3[1]} |")
  print(f"|  {c1[0]}| |  {c2[0]}| |  {c3[0]}|")
  print("└───┘ └───┘ └───┘")
  input("Presione enter: ")
  print("┌───┐ ┌───┐ ┌───┐")
  print(f"|   | |   | |   |")
  print(f"| ? | | ? | | ? |")
  print(f"|   | |   | |   |")
  print("└───┘ └───┘ └───┘")
  print("Intercambio izquierda (I) con la del medio (M)...")
  print("Intercambio derecha (D) con la del medio (M)...")
  print("Intercambio la del medio (M) con izquierda (I)...")
  print("Intercambio derecha (D) con izquierda (I)...")
  print("Intercambio izquierda (I) con derecha (D)...")
  opc=input("¿En cuál de las cartas está la reina de corazones? [I], [M], [D]: ").upper() 
  #sea opc Opcion de Carta Correcta
  
  
  if opc!="D" and opc!="M"  and opc!="I":
      print("No existe Carta en esa posición")
  else:
    #mostramos en el orden que quedaron las cartas
    print("┌───┐ ┌───┐ ┌───┐")
    print(f"|{c3[0]}  | |{c2[0]}  | |{c1[0]}  |")
    print(f"| {c3[1]} | | {c2[1]} | | {c1[1]} |")
    print(f"|  {c3[0]}| |  {c2[0]}| |  {c1[0]}|")
    print("└───┘ └───┘ └───┘")
    if opc == "D":
      print(f"La opcion {opc} es CORRECTA ¡Haz recibido +{puntosGanador} puntos!")
    elif opc =='I' or opc=='M':
      print("Lo siento perdedor(a) :-(")
      print("¡Gracias por jugar!")
    else: 
      print(f"La opcion {opc} no es correcta")

elif ac=="T":
  print("Top 5 de lo(a)s mejores:")
  print(f"1. {U}, {puntosGanador} puntos, Mejor jugada 2022-03-11 a las 10:58pm")
  print("2. Rodolfo, 8 puntos. Mejor jugada el 2026-03-12 a las 08:00am")
  print("3. Lucia, 7 puntos. Mejor jugada el 2026-02-10 a las 9:10pm")
  print("4. Rocio, 3 puntos. Mejor jugada el 2026-02-08 a las 10:13pm")
  print("5. Jhon, 2 puntos. Mejor jugada el 2026-03-07 a las 7:10pm")
elif ac=="S":
  print("¡Adiós!")
