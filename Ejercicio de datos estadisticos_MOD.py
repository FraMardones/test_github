def media_geométrica_manual(data):
    producto = 1
    for valor in data:
        producto *= valor
    return producto ** (1 / len(data))

a = [50,3,1,20,4]
media_geométrica_manual = media_geométrica_manual(a)
print(media_geométrica_manual)  # Resultado: 3.73 (aproximadamente)

matriz = [
    [85, 45, 1, 7, 9],
    [12, 52, 9, 151, 56],
    [76, 10, 56, 99, 9]
]

for lista in matriz:
    maximo = max(lista)
    i_f = matriz.index(lista)
    ic_max = lista.index(maximo)
    minimo = min(lista)
    ic_min = lista.index(minimo)
    print(f"El máximo es {maximo} que se encuentra en la fila {i_f} y la columna {ic_max}")
    print(f"El mínimo es {minimo} que se encuentra en la fila {i_f} y la columna {ic_min}\n")


def calcular_promedio(lista):
    total = sum(lista)
    cantidad = len(lista)
    return total / cantidad

mi_lista = [10, 20, 30, 40, 50]
promedio = calcular_promedio(mi_lista)
print(f"El promedio es: {promedio:.2f}")