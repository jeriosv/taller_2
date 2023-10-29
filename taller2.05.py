def mcd(a, b): # Función para calcular el Máximo Común Divisor de dos números
    while b:
        a, b = b, a % b
    return a

def mcm(a, b): # Función para calcular el Mínimo Común Múltiplo de dos números
    return a * b // mcd(a, b)

def mcmIterativo(a, b): # Función iterativa para calcular el Mínimo Común Múltiplo de dos números
    return mcm(a, b)

def mcmRecursivo(a, b): # Función recursiva para calcular el Mínimo Común Múltiplo de dos números
    if b == 0:
        return a
    else:
        return mcmRecursivo(b, a % b) * a // mcd(a, b)

if __name__ == "__main__":
    a = int(input("Ingrese el primer número:  "))    # Ingreso del usuario 
    b = int(input("Ingrese el segundo número: "))
    print("El Mínimo Común Múltiplo de", a, "y", b, "con perspectiva iterativa es:", mcmIterativo(a, b))  # Imprimir resultados
    print("El Mínimo Común Múltiplo de", a, "y", b, "con perspectiva recursiva es:", mcmRecursivo(a, b))