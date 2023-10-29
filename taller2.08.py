lista1 = []
k = 1
while True:    # Ingreso del usuario de los terminos de la primera lista
    elemento = input("Ingrese el elemento No. " +  str(k)  + " para la primera lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    k += 1
    lista1.append(str(elemento))

lista2 = []
k = 1
while True:    # Ingreso del usuario de los terminos de la segunda lista
    elemento = input("Ingrese el elemento No. " +  str(k)  + " para la segunda lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    k += 1
    lista2.append(str(elemento))

diferentes = []   # Lista vacía para almacenar los elementos que están en la primera lista pero no en la segunda lista

for elemento in lista1:    # Recorrer la primera lista y verificamos si cada elemento está en la segunda lista
    esta_en_lista2 = False
    for elemento2 in lista2:
        if elemento == elemento2:
            esta_en_lista2 = True
            break
    if not esta_en_lista2:
        diferentes.append(elemento)

print("La primer lista ingresada es:  " + str(lista1))  # Imprimir la lista 1
print("La segunda lista ingresada es: " + str(lista2))  # Imprimir la lista 2
print("Los elementos que están en la primera lista pero no en la segunda lista son:", diferentes) # Imprimir resultados