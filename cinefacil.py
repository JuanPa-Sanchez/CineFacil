reservaciones={}
while True:
    nombre=str(input("Ingrese su nombre: "))
    pelicula=str(input("Ingrese la funcion a la que desea entrar: "))
    boletos=int(input("Ingrese la cantidad de boletos que desea comprar: "))
    total=boletos*30
    print("Resumen")
    print(f"Nombre: {nombre}\nPelicula: {pelicula}\nTotal a pagar: {total}")
    reservaciones["Reserva"]={
        "Nombre": nombre,
        "Pelicula": pelicula,
        "Total": total
    }
    try:
        pregunta=str(input("Desea hacer otra reservacion: (SI/NO) "))
        if pregunta.lower()=="si":
            continue
        elif pregunta.lower()=="no":
            print(reservaciones)
            print("Saliendo...")
            break
    except ValueError:
        print("Respuesta no valida")
        pregunta=str(input("Desea hacer otra reservacion: (SI/NO) "))