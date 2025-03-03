# Matriz 3x3
matriz = [
    [9, 4, 2],
    [12, 5, 8],
    [3, 6, 9]
]

filas = 3
columnas = 3

# Función para ordenar una fila específica usando Bubble Sort
def ordenar_fila(matriz, fila):
    for i in range(columnas - 1):
        for j in range(columnas - 1 - i):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 1

ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
