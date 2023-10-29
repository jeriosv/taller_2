def matrizMagica(matriz:list) -> bool:
    m_len = len(matriz)
    suma_filas = []     # Sumar filas
    for i in range(m_len): 
        lst = matriz[i]
        suma = 0 
        for j in range(m_len):
            suma += lst[j]
        if len(suma_filas) == 0: 
            suma_filas.append(suma)
        elif suma_filas[-1] == suma:
            suma_filas.append(suma)
        else:
            return False
        
    suma_columnas = [] # Sumar columnas
    for i in range(m_len):
        suma = 0 
        for j in range(m_len):
            suma += matriz[i][j]
        if len(suma_columnas) == 0: 
            suma_columnas.append(suma)
        elif suma_columnas[-1] == suma:
            suma_columnas.append(suma)
        else:
            return False    

    if suma_filas != suma_columnas: # Comparar si las listas (que contienen los valores calculados para la suma de cada fila y columna), son iguales.
        return False                # Si no son iguales la función retorna False.
    
    suma_diagonal1 = 0      # Calcular la suma de la diagonal
    shifter = 0
    for i in range(m_len):
        suma_diagonal1 += matriz[i][shifter]
        shifter += 1  

    suma_diagonal2 = sum([row[len(matriz) - 1 - i] for i, row in enumerate(matriz)]) # se halla la suma de la diagonal izq-der (se implementaron técnicas novedosas ya que era practicamente lo mismo que para la otra diagonal).

    for i in range(m_len): # Comparar si las listas de las diagonales son iguales a la suma_columnas
        if suma_columnas[i] != suma_diagonal1 and suma_columnas != suma_diagonal2:
            return  False

    return True
    
if __name__ == "__main__":
    matriz = []
    n = int(input("Ingrese el tamaño de la matriz (matriz cuadrada): ")) # Ingreso del tamaño de la matriz cuadrada
    for x in range(n):
        lista = []
        for y in range(n):
            elemento = int(input(f"Ingrese el elemento ({x+1},{y+1}): "))
            lista.append(elemento)
        matriz.append(lista)
    respuesta = matrizMagica(matriz)

    if respuesta == True :    # Imprimir resultado
        print("La matriz sí es mágica.")
    else:
        print("La matriz no es mágica.")