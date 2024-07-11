import csv
import time
import random
import os


archivos_csv = ["pedidos.csv", "pedidosSB.txt", "pedidosCT.txt", "pedidosBU.txt"]
encabezados = ["Nro.pedido", "Cliente", "Direccion", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"]

try:
    with open ("pedidos.csv","x",newline="") as pedidos1:
        writer = csv.writer(pedidos1)
        writer.writerows(encabezados)
except FileExistsError:
    pass


for archivo in archivos_csv:
    try:
        with open(archivo, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(encabezados)
    except FileExistsError:
        pass

def registropedidos(): 
    numeropedido = random.randint(1,1000)
    os.system("cls")
    saco5kg = 0
    saco10kg = 0
    saco20kg = 0
    cantidad = 0
    sector = 0
    numeropedido +=1
    cliente = input("Ingrese su nombre y apellido: ")
    direccion = input("Ingrese su direccion: ")
    while True:   
        sector = int(input("Ingrese su sector\n1.San Bernardo\n2.Calera de Tango\n3.Buin\nSeleccione: "))
        if sector == 1:
            sector = "San Bernardo"
            break
        elif sector == 2:
            sector = "Calera de Tango"
            break
        elif sector == 3:
            sector = "Buin"
            break
        else:
            print("Ingrese una opcion valida")
    otromas = 0
    while otromas != 2:        
        comida = int(input("¿Que sacos quiere?\n1.Saco 5kg\n2.Saco 10kg\n3.Saco 20kg\n"))
        if comida == 1:
            cantidad = int(input("Cuantos sacos quiere?\n"))
            saco5kg += cantidad
            otromas = int(input("¿Quiere otro tipo de comida? 1(si)/2(no)\nElija: "))
        elif comida == 2:
            cantidad = int(input("Cuantos sacos quiere?\n"))
            saco10kg += cantidad
            otromas = int(input("¿Quiere otro tipo de comida? 1(si)/2(no)\nElija: "))
        elif comida == 3:
            cantidad = int(input("Cuantos sacos quiere?\n"))
            saco20kg += cantidad
            otromas = int(input("¿Quiere otro tipo de comida? 1(si)/2(no)\nElija: "))
        else:
            print("Debe ingresar un numero entero positivo")
    with open ("pedidos.csv","a",newline="") as pedidos1:
        escritorpedidos = csv.writer(pedidos1)
        escritorpedidos.writerows([
            [numeropedido,cliente,direccion,sector,saco5kg,saco10kg,saco20kg]
        ])
    
    with open ("pedidos.csv","r",newline="") as pedidos1:
        lectorpedidos = csv.reader(pedidos1)
        next(lectorpedidos)

        pedidosSB = [encabezados]
        pedidosCT = [encabezados]
        pedidosBU = [encabezados]

        for row in lectorpedidos:
            if row[3] == "San Bernardo":
                pedidosSB.append(row)
            elif row[3] == "Calera de Tango":
                pedidosCT.append(row)
            elif row[3] == "Buin":
                pedidosBU.append(row)
        
    with open ("pedidosSB.txt","w",newline="") as sector1:
        escritorSB = csv.writer(sector1)
        escritorSB.writerows(pedidosSB)
    with open ("pedidosCT.txt","w",newline="") as sector2:
        escritorCT = csv.writer(sector2)
        escritorCT.writerows(pedidosCT)
    with open ("pedidosBU.txt","w",newline="") as sector3:
        escritorBU = csv.writer(sector3)
        escritorBU.writerows(pedidosBU)

    print("Ha sido registrado con exito")

def listado():
    print("Cargando...")
    time.sleep(1)
    with open ("pedidos.csv", "r",newline="") as pedidos:
        lectorpedidos = csv.reader(pedidos)
        for i in lectorpedidos:
            print(*i)
            time.sleep(0.5)

def hojaDeRuta():
    while True:
        os.system("cls")
        ruta_eleccion = int(input("Que ruta quiere ver?\n1.San Bernardo\n2.Calera de Tango\n3.Buin\nSeleccione: "))
        if ruta_eleccion == 1:
            with open ("pedidosSB.txt","r",newline="") as sector1:
                lector = csv.reader(sector1)
                for i in lector:
                    print(*i)
                    time.sleep(0.5)
                break
        elif ruta_eleccion == 2:
            with open ("pedidosCT.txt","r",newline="") as sector2:
                lector = csv.reader(sector2)
                for i in lector:
                    print(*i)
                    time.sleep(0.5)
                break
        elif ruta_eleccion == 3:
            with open ("pedidosBU.txt","r",newline="") as sector3:
                lector = csv.reader(sector3)
                for i in lector:
                    print(*i)
                    time.sleep(0.5)
                break
        else:
            print("Ingrese una opcion valida")
            time.sleep(1)

def menu():
    print("Bienvenido a Catpremium!!")
    while True:    
        opc = int(input("-------------------\nElija una opcion porfavor\n1.Registrar pedido\n2.Listar todos los pedidos\n3.Imprimir hoja de ruta\n4.Salir del programa\n-----------------\nSeleccione: "))
        if opc == 1:
            registropedidos()
        elif opc == 2:
            listado()
        elif opc == 3:
            hojaDeRuta()
        elif opc == 4:
            print("Nos vemos!!")
            break
        else:
            print("Elija una opcion valida")
            time.sleep(2)
            os.system("cls")
menu()
