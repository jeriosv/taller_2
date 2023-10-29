import math                     # Importar el módulo math
n = float(input("Ingrese el número a calcular su parte entera y su parte decimal: "))  # Ingreso del usuario

parteEntera = math.trunc(n)     # math.trunc() obtiene la parte entera del número n
parteDecimal = n - parteEntera  # Restar la parte entera del número n

print("La parte entera del número " + str(n) + " es " + str(parteEntera) + " y su parte decimal es " + str(parteDecimal))  # Imprimir resultado