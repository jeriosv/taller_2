import math             # Importan el módulo math

def aproxCoseno(x, n):  # Función aproximación del coseno
    aproximacion = 0    # Inicializar variable en cero
    for i in range(n):  # Utilizar un bucle for hasta n términos
        termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)  # Calcular i-ésimo término de la serie de Taylor para el coseno
        aproximacion += termino  # Sumar el i-ésimo término a la variable 
    return aproximacion          # Retornar la aproximacion de los n terminos

x = float(input("Ingrese el valor de x, para aproximar coseno de x: "))  # Ingreso del usuario

errores_deseados = [0.001, 0.1, 1, 10]  # Lista de errores esperados

for error in errores_deseados:  # Bucle for para iterar segun el error esperado
    e = 0                       # Inicializar e en cero
    while True:                 # Bucle infinito
        e += 1                  # Aumentar e en 1
        aproximacion = aproxCoseno(x, e)  # Llamado de la funcion de aproximacion de coseno
        error_porcentual = abs((aproximacion - math.cos(x)) / math.cos(x)) * 100  # Cálculo del error porcentual
        if error_porcentual <= error:  # Si el error porcentual es menor al error deseado
            break               # Salir del bucle infinito
    print("Aproximación de coseno de x: " + str(aproximacion))  # Imprimir la aproximación por series de Taylor
    print("Valor real de coseno de x:   " + str(math.cos(x)))   # Imprimir el valor real de coseno de x
    print("Con un error de " + str(error) + "% se necesitan " + str(e) + " términos de la serie\n")  # Imprimir los términos necesarios