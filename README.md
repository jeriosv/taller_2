## Taller 2: desarrollado por "Los Pythoneros"


![ideogram (1)](https://github.com/jeriosv/taller_1/assets/142249529/5bd59e64-9074-4caf-beac-929549df998f)


Integrantes del equipo:
- Andrés Camilo Bustamante Guzmán
- Jhonatan Esteban Forero Velásquez
- Jaime Eduardo Ríos Villegas
 

1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. **Pista:** Utilice los operadores módulo (%) y división entera (//).

```python
numeros = []  # Definición de la lista numeros
def separarDigitos(num):  # Definición de la Función para separa los dígitos de un número
    while num > 0:  
        numeros.append(num%10)  # Operador módulo % para obtener el último dígito de num
        num = num // 10           # Operador de división entera "//" para eliminar el último dígito de num
    numeros.reverse()         # Invierte el orden de los elementos de la lista numeros
    print("Los dígitos separados del número ingresado son: " + str(numeros))            # Imprimir resultados
n = int(input("Ingrese un número entero para separar sus dígitos: "))  # Ingreso del usuario
separarDigitos(n)  # Llamado de la función como argumento pasando n
```

2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

```python
import math  # Importar el módulo math
n = float(input("Ingrese el número a calcular su parte entera y su parte decimal: "))  # Ingreso del usuario

parteEntera = math.trunc(n)     # math.trunc() obtiene la parte entera del número n
parteDecimal = n - parteEntera  # Restar la parte entera del número n

print("La parte entera del número " + str(n) + " es " + str(parteEntera) + " y su parte decimal es " + str(parteDecimal))  # Imprimir resultado
```

3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

```python
def numeroEspejo(numero):  # Definición de la función numeroEspejo
    numero_invertido = 0   # Inicializa variable en cero
    while numero > 0:      # Mientras el número sea mayor que cero
        digito = numero % 10  # Operador módulo % para obtener el último dígito de numero 
        numero_invertido = (numero_invertido * 10) + digito  # Se multiplica numero_invertido por 10 y se le suma digito para invertir el orden de los dígitos de numero 
        numero //= 10      # Se utiliza el operador de división entera "//" para eliminar el último dígito de "numero"
    return numero_invertido  # Retorna el número invertido

a = int(input("Ingrese el primer número:  "))  # Ingreso del usuario de a
b = int(input("Ingrese el segundo número: "))  # Ingreso del usuario de b

a_invertido = numeroEspejo(a)  # Llamado de la función

if a_invertido == b:           # Si el número invertido n_invertido es igual al número b
    print("Los números", a, "y", b, "sí son espejos.")  # Imprimir resultado afirmativo
else:
    print("Los números", a, "y", b, "no son espejos.")  # Imprimir resultado negativo
```

4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. **nota:** use *math* para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.
$$cos(x) \approx cos(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i}}{(2i)!}$$

```python
import math  # Se importa el módulo "math" que contiene funciones matemáticas

def aproximacion_coseno(x, n):  # Se define una función llamada "aproximacion_coseno" que toma dos argumentos: "x" y "n"
    aproximacion = 0  # Se inicializa la variable "aproximacion" en cero
    for i in range(n):  # Se utiliza un bucle "for" para iterar "n" veces
        termino = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)  # Se calcula el "i"-ésimo término de la serie de Taylor para el coseno y se almacena en la variable "termino"
        aproximacion += termino  # Se suma el "i"-ésimo término a la variable "aproximacion"
    return aproximacion  # Se devuelve la aproximación del coseno de "x" utilizando "n" términos de la serie de Taylor

x = float(input("Ingrese el valor de x: "))  # Se pide al usuario que ingrese el valor de "x" y se almacena en la variable "x" como un número de punto flotante

errores_deseados = [0.001, 0.1, 1, 10]  # Se define una lista de errores deseados

for error in errores_deseados:  # Se utiliza un bucle "for" para iterar sobre los errores deseados
    e = 0  # Se inicializa la variable "e" en cero
    while True:  # Se utiliza un bucle "while" infinito
        e += 1  # Se incrementa la variable "e" en uno en cada iteración
        aproximacion = aproximacion_coseno(x, e)  # Se llama a la función "aproximacion_coseno" con "x" y "e" como argumentos y se almacena el resultado en la variable "aproximacion"
        error_porcentual = abs((aproximacion - math.cos(x)) / math.cos(x)) * 100  # Se calcula el error porcentual entre la aproximación y el valor real del coseno de "x" y se almacena en la variable "error_porcentual"
        if error_porcentual <= error:  # Se utiliza una condición "if" para verificar si el error porcentual es menor o igual al error deseado
            break  # Si el error porcentual es menor o igual al error deseado, se sale del bucle "while"
    print("Aproximación: " + str(aproximacion))  # Se imprime en la pantalla la aproximación del coseno de "x" utilizando "e" términos de la serie de Taylor
    print("Valor real: " + str(math.cos(x)))  # Se imprime en la pantalla el valor real del coseno de "x"
    print("Con un error del " + str(error) + "% se necesitan " + str(e) + " términos de la serie")  # Se imprime en la pantalla el error deseado, el número de términos de la serie necesarios para alcanzar el error deseado y un mensaje indicando que se ha alcanzado el error deseado
    print("")  # Se imprime una línea en blanco para separar las salidas de cada iteración del bucle "for"
```

5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. **Pista:** Puede ser de utilidad chequear el [Algoritmo de Euclides](https://es.wikipedia.org/wiki/Algoritmo_de_Euclides) para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

```python
# Función para calcular el Máximo Común Divisor de dos números
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Función para calcular el Mínimo Común Múltiplo de dos números
def mcm(a, b):
    return a * b // mcd(a, b)

# Versión iterativa
def mcm_iterativo(a, b):
    return mcm(a, b)

# Versión recursiva
def mcm_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mcm_recursivo(b, a % b) * a // mcd(a, b)

# Imprimimos los resultados
if __name__ == "__main__":
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    print("El Mínimo Común Múltiplo de", a, "y", b, "es:", mcm_iterativo(a, b))
    print("El Mínimo Común Múltiplo de", a, "y", b, "es:", mcm_recursivo(a, b))
    
```

6. Desarrollar un programa que determine si en una lista existen o no elementos repetidos. **Pista:** Maneje valores booleanos y utilice el operador *in*.

```python
# Definimos una lista vacía para almacenar los elementos
lista = []

# Pedimos al usuario que ingrese los elementos de lista
while True:
    elemento = input("Ingrese un elemento (o presione Enter para terminar): ")
    if elemento == '':
        break
    lista.append(int(elemento))

# Buscamos elementos repetidos en la lista
repetidos = False
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            repetidos = True
            break
    if repetidos:
        break
# Imprimimos la lista
print(lista)
# Imprimimos el resultado
if repetidos:
    print('Existen elementos repetidos en la lista')
else:
    print('No existen elementos repetidos en la lista')
```

7. Desarrollar un programa que determine si en una lista se encuentra
una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

```python
# Definimos una lista vacía para almacenar las cadenas de caracteres
lista=[]

# Pedimos al usuario que ingrese las cadenas de caracteres hasta que ingrese 'fin'
while True:
    cadena = input("Ingrese una cadena de caracteres (o escriba 'fin' para terminar): ")
    # Si el usuario ingresa 'fin', salimos del bucle
    if cadena == 'fin':
        break
    # Agregamos la cadena a la lista
    lista.append(cadena)

# Definimos una función para contar las vocales en una cadena
def contar_vocales(cadena):
    # Definimos una lista con las vocales (mayúsculas y minúsculas)
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # Inicializamos el contador de vocales en 0
    contador = 0
    # Recorremos la cadena de caracteres
    for letra in cadena:
        # Si la letra es una vocal, aumentamos el contador
        if letra in vocales:
            contador += 1
    # Devolvemos el contador de vocales
    return contador

# Definimos una variable para indicar si encontramos una cadena con dos o más vocales
encontrado = False

# Recorremos la lista de cadenas de caracteres
for cadena in lista:
    # Contamos las vocales en la cadena
    num_vocales = contar_vocales(cadena)
    # Si la cadena tiene dos o más vocales, la imprimimos y cambiamos el valor de la variable encontrado
    if num_vocales >= 2:
        print(f"La cadena '{cadena}' tiene {num_vocales} vocales.")
        encontrado = True

# Si no encontramos ninguna cadena con dos o más vocales, imprimimos 'No existe'
if not encontrado:
    print('No existe')
```

8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. **Ejemplo:**
<center>
<table border="1">
<tr>
<td>
lista1: [1, 'Hola', -12.3 ,True]<br>
lista2: [11, -12.3, 'Hola', False]
</td>
</tr>
<tr>
<td>
salida: [1, True]
</td>
</tr>
</table>
</center>

```python
# Pedimos al usuario que ingrese los elementos de la primera lista
lista1 = []
while True:
    elemento = input("Ingrese un elemento para la primera lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    lista1.append(int(elemento))

# Pedimos al usuario que ingrese los elementos de la segunda lista
lista2 = []
while True:
    elemento = input("Ingrese un elemento para la segunda lista (o presione Enter para terminar): ")
    if elemento == '':
        break
    lista2.append(int(elemento))

# Creamos una lista vacía para almacenar los elementos que están en la primera lista pero no en la segunda lista
diferencia = []

# Recorremos la primera lista y verificamos si cada elemento está en la segunda lista
for elemento in lista1:
    esta_en_lista2 = False
    for elemento2 in lista2:
        if elemento == elemento2:
            esta_en_lista2 = True
            break
    if not esta_en_lista2:
        diferencia.append(elemento)

# Imprimimos los elementos que están en la primera lista pero no en la segunda lista
print("Los elementos que están en la primera lista pero no en la segunda lista son:", diferencia)
```


9. Resolver el punto 7 del [taller 1](https://github.com/fegonzalez7/pdc_unal_clase8) usando operaciones con vectores.

```python
# Pedir 5 números reales al usuario
numeros = []
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Calcular el promedio aritmético
promedio_aritmetico = sum(numeros) / len(numeros)

# Calcular la mediana
numeros_ordenados = sorted(numeros)
mediana = 0
if len(numeros_ordenados) % 2 == 0:
    # Si el número de elementos es par, se promedian los dos del centro
    indice_medio = len(numeros_ordenados) // 2
    mediana = (numeros_ordenados[indice_medio-1] + numeros_ordenados[indice_medio]) / 2
else:
    # Si el número de elementos es impar, se toma el del centro
    indice_medio = len(numeros_ordenados) // 2
    mediana = numeros_ordenados[indice_medio]

# Calcular el promedio multiplicativo
from functools import reduce
promedio_multiplicativo = reduce(lambda x, y: x * y, numeros) ** (1/len(numeros))

# Ordenar los números de forma ascendente y descendente
numeros_ascendente = sorted(numeros)
numeros_descendente = sorted(numeros, reverse=True)

# Calcular la potencia del mayor número elevado al menor número
mayor = max(numeros)
menor = min(numeros)
potencia = mayor ** menor

# Calcular la raíz cúbica del menor número
raiz_cubica = menor ** (1/3)

# Mostrar los resultados
print(f"El promedio aritmético es: {promedio_aritmetico}")
print(f"La mediana es: {mediana}")
print(f"El promedio multiplicativo es: {promedio_multiplicativo}")
print(f"Los números en orden ascendente son: {numeros_ascendente}")
print(f"Los números en orden descendente son: {numeros_descendente}")
print(f"El mayor número elevado al menor número es: {potencia}")
print(f"La raíz cúbica del menor número es: {raiz_cubica}")
```

10. Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser **retornada** por la función. Implemente la perspectiva de un *patrón de acumulación* y también de *comprensión de listas*. **Desafío:** Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). **Pista:** Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?

```python
# Pedimos al usuario que ingrese los datos de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        elemento = int(input(f"Ingrese el elemento ({i+1},{j+1}): "))
        fila.append(elemento)
    matriz.append(fila)

# Calculamos la mágica
suma_magica = 0
for i in range(n):
    suma_magica matriz[0][i]

# Verificamos si la suma de cada fila, columna y diagonal es igual a la suma mágica
es_magica = True
for i in range(n):
    # Verificamos la suma de la fila i
    suma_fila = 0
    for j in range(n):
        suma_fila += matriz[i][j]
    if suma_fila != suma_magica:
        es_magica = False
        break
    # Verificamos la suma de la columna i
    suma_columna = 0
    for j in range(n):
        suma_columna += matriz[j][i]
    if suma_columna != suma_magica:
        es_magica = False
        break
    # Verificamos la suma de la diagonal principal
    suma_diagonal_principal = 0
    for j in range(n):
        if i == j:
            suma_diagonal_principal += matriz[i][j]
    if suma_diagonal_principal != suma_magica:
        es_magica = False
        break
    # Verificamos la suma de la diagonal secundaria
    suma_diagonal_secundaria = 0
    for j in range(n):
        if i + j == n - 1:
            suma_diagonal_secundaria += matriz[i][j]
    if suma_diagonal_secundaria != suma_magica:
        es_magica = False
        break

# Imprimimos el resultado
if es_magica:
    print("La matriz es mágica")
else:
    print("La matriz no es mágica")
```

### Bono
11. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

```python

```



