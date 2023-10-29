lista=[]                  # Definimos una lista vacía 

k = 1
while True:               # Ingreso del usuario de las cadenas de caracteres
    cadena = input("Ingrese la cadena de caracteres No. " +  str(k)  + " de la lista (o presione Enter para terminar): ")
    if cadena == '':      # Si el usuario ingresa Enter, salimos del bucle
        break
    k += 1
    lista.append(cadena)   # Agregar la cadena a la lista

def cuentaVocales(cadena): # Función para contar las vocales
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # Lista de vocales
    contador = 0           # Inicializar contador
    for letra in cadena:   # Recorrer la cadena en busqueda de vocales
        if letra in vocales:
            contador += 1
    return contador        # Retorna el número de vocales en una cadena de caracteres

encontrado = False
print("Las cadenas que tienen 2 o más vocales son:")

for cadena in lista:       # Recorrer la lista de cadenas de caracteres
    cantidadVocales = cuentaVocales(cadena)   
    if cantidadVocales >= 2: # Si la cadena tiene dos o más vocales, imprimir y cambiar encontrado a true
        print(f"La cadena '{cadena}' tiene {cantidadVocales} vocales.")
        encontrado = True

if not encontrado:         # Imprimir resultado negativo
    print("No existe.")