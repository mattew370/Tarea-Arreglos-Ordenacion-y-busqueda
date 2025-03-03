#matriz 3x3
matriz = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]

posicion = None

def buscar_valor_en_matriz(matriz, valor_buscar):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == valor_buscar:
                return (i, j)
    return None


valor_buscar = int(input("Ingrese el número que desea buscar: "))


posicion = buscar_valor_en_matriz(matriz, valor_buscar)


if posicion:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion}")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")