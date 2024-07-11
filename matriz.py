import csv

matriz = [
    [12,15,19,2,7],
    [24,56,9,1,0],
    [10,26,31,60,9]
]

def escribir_matriz_csv():
    with open ("matriz.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo)
        for fila in matriz:
            escritor.writerow(fila)

def encontrar_maximos(nombre_archivo):
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        matriz_leida = list(lector)
        
        for i, fila in enumerate(matriz_leida):
            fila_numeros = [int(num) for num in fila]  # Convertir elementos de la fila a enteros
            maximo = max(fila_numeros)
            minimo = min(fila_numeros)
            ic_max = fila_numeros.index(maximo)
            ic_min = fila_numeros.index(minimo)
            print(f"En la fila {i}:")
            print(f"   El máximo es {maximo} en la columna {ic_max}")

def encontrar_minimos(nombre_archivo):
    with open(nombre_archivo, 'r', newline='') as archivo:
        lector = csv.reader(archivo)
        matriz_leida = list(lector)
        
        for i, fila in enumerate(matriz_leida):
            fila_numeros = [int(num) for num in fila]  # Convertir elementos de la fila a enteros
            maximo = max(fila_numeros)
            minimo = min(fila_numeros)
            ic_max = fila_numeros.index(maximo)
            ic_min = fila_numeros.index(minimo)
            print(f"En la fila {i}:")
            print(f"   El mínimo es {minimo} en la columna {ic_min}\n")

def menu():
    escribir_matriz_csv()
    print("bienvenido")
    while True:    
        opc = int(input("1.maximo\n2.minimo\n"))
        if opc == 1:
            encontrar_maximos("matriz.csv")
        elif opc == 2:
            encontrar_minimos("matriz.csv")
        else:
            print("ingresa un valor valido")

menu()