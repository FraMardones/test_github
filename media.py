import csv
try:    
    with open ("datos.csv", "x", newline="") as datos:
        escritor = csv.writer(datos)
        escritor.writerow(["Numeros"])
except FileExistsError:
    pass

def ingresar_datos():
    while True:
        try:
            numeros = float(input("Ingrese un número (presione una letra para terminar): "))
            with open("datos.csv", "a", newline="") as datos:
                escritor = csv.writer(datos)
                escritor.writerow([numeros])
        except ValueError:    
            print("Datos ingresados correctamente")
            break


def media():
    with open("datos.csv","r",newline="") as datos:
        lector = csv.reader(datos)
        valores = []
        for fila in lector:
            valores.append(float(fila[0]))
        producto = 1
        for valor in valores:
            producto *= valor
        media_geometrica = producto ** (1/len(valores)) if valores else 0
        print(f"el resultado de la media geometrica es: {media_geometrica}")

def salir():
    print("Nos vemos")
    exit()

def menu():
    print("Bienvenido")
    while True:
        opc = int(input("Elija una opcion\n1.Ingresar datos\n2.leer media\n3.Salir\nSeleccione: "))
        if opc == 1:
            ingresar_datos()
        elif opc == 2:
            media()
        elif opc == 3:
            salir()
        else:
            print("ingrese una opcion valida")
    
menu()