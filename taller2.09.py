numeros = []
for i in range(5):     # Ingreso del usuario de 5 numeros reales
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

promedioAritmetico = sum(numeros) / len(numeros)   # Calcular el promedio aritmético

numerosOrdenados = sorted(numeros)  # Calcular la mediana
mediana = 0
if len(numerosOrdenados) % 2 == 0:  # Si el número de elementos es par, se promedian los dos del centro
    indiceMedio = len(numerosOrdenados) // 2
    mediana = (numerosOrdenados[indiceMedio-1] + numerosOrdenados[indiceMedio]) / 2
else:                                # Sino, el número de elementos es impar, se toma el del centro
    indiceMedio = len(numerosOrdenados) // 2
    mediana = numerosOrdenados[indiceMedio]

from functools import reduce         # Calcular el promedio multiplicativo
promedioMultiplicativo = reduce(lambda x, y: x * y, numeros) ** (1/len(numeros))

numerosAscendente = sorted(numeros) # Ordenar los números de forma ascendente y descendente
numerosDescendente = sorted(numeros, reverse=True)

mayor = max(numeros)                 # Calcular la potencia del mayor número elevado al menor número
menor = min(numeros)
potencia = mayor ** menor

raizCubica = menor ** (1/3)         # Calcular la raíz cúbica del menor número

print(f"El promedio aritmético es: {promedioAritmetico}")    # Imprimir resultados
print(f"La mediana es:             {mediana}")
print(f"El promedio multiplicativo es:        {promedioMultiplicativo}")
print(f"Los números en orden ascendente son:  {numerosAscendente}")
print(f"Los números en orden descendente son: {numerosDescendente}")
print(f"El mayor número elevado al menor número es: {potencia}")
print(f"La raíz cúbica del menor número es:   {raizCubica}")