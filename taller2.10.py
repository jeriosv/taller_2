def multiplosDe3(lista):   # Función para el cálculo de si es multiplo de 3
    return [i for i in lista if i % 3 == 0]                                                     
                                
if __name__ == "__main__":
  lista=[]
  n = int(input("Ingrese la cantidad de elementos de la lista: "))  # Ingreso del usuario de cantidad de elementos de la lista
  for i in range(n):                                                # Ingreso de elementos por el usuario
    numero = int(input("Ingrese un número a la lista: "))
    lista.append(numero)                                            # Agrega elementos a la lista
  multiplos=multiplosDe3(lista)                                     # Llamado de la función
  print("La lista ingresada es: " + str(lista))                     # Imprimir lista ingresada
  print("Los números múltiplos de 3 son: " + str(multiplos))        # Imprimir resultados