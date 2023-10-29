numeros = []                    # Definición de la lista numeros
def separarDigitos(num):        # Definición de la Función para separa los dígitos de un número
    while num > 0:  
        numeros.append(num%10)  # Operador módulo % para obtener el último dígito de num
        num = num // 10         # Operador de división entera "//" para eliminar el último dígito de num
    numeros.reverse()           # Invierte el orden de los elementos de la lista numeros
    print("Los dígitos separados del número ingresado son: " + str(numeros)) # Imprimir resultados
n = int(input("Ingrese un número entero para separar sus dígitos: "))        # Ingreso del usuario
separarDigitos(n)               # Llamado de la función como argumento pasando n