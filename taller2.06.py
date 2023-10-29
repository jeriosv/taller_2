lista = []   # Definimos una lista vacía

k = 1
while True:       # Ingreso del usuario de los términos de la lista
    elemento = input("Ingrese el elemento No. " +  str(k)  + " de la lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    k += 1
    lista.append(str(elemento))

repetidos = False
for i in range(len(lista)):    # Buscar elementos repetidos en la lista
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            repetidos = True
            break
    if repetidos:
        break

print("La lista ingresada es: " + str(lista))  # Imprimir la lista

if repetidos:     # Imprimir resultado
    print('Sí existen elementos repetidos en la lista.')
else:
    print('No existen elementos repetidos en la lista.')