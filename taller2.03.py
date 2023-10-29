def numeroEspejo(numero):  # Definición de la función numeroEspejo
    numero_invertido = 0   # Inicializa variable en cero
    while numero > 0:      # Mientras el número sea mayor que cero
        digito = numero % 10  # Operador módulo % para obtener el último dígito de numero 
        numero_invertido = (numero_invertido * 10) + digito  # Se multiplica numero_invertido por 10 y se le suma digito para invertir el orden de los dígitos de numero 
        numero //= 10         # Se utiliza el operador de división entera "//" para eliminar el último dígito de "numero"
    return numero_invertido   # Retorna el número invertido

a = int(input("Ingrese el primer número:  "))  # Ingreso del usuario de a
b = int(input("Ingrese el segundo número: "))  # Ingreso del usuario de b

a_invertido = numeroEspejo(a)  # Llamado de la función

if a_invertido == b:           # Si el número invertido n_invertido es igual al número b
    print("Los números", a, "y", b, "sí son espejos.")  # Imprimir resultado afirmativo
else:
    print("Los números", a, "y", b, "no son espejos.")  # Imprimir resultado negativo