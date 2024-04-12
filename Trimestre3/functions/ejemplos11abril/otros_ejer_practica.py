# supuesto exam

# Ejercicio de Clausura:
# Define una función contador_palabras que tome una cadena de texto como argumento y devuelva una función interna que cuenta el número
# de veces que aparece cada palabra en el texto. La función interna debería devolver un diccionario donde las claves son las palabras
# y los valores son sus conteos respectivos. Utiliza una clausura para lograr esto.


def contador_palabras(texto):
    palabras = texto.split()

    def contar():
        conteo = {}
        for palabra in palabras:
            conteo[palabra] = conteo.get(palabra, 0) + 1
        return conteo

    return contar


# Ejemplo de uso:
contar_palabras_en_texto = contador_palabras(
    'Este es un ejemplo de texto de prueba para contar palabras'
)
print(contar_palabras_en_texto())


# Ejercicio de Decoradores:
# Define un decorador llamado registro que imprima el nombre de la función decorada y los argumentos que recibe cada vez
# que se llama a esa función. Aplica este decorador a una función de tu elección y demuestra su uso.


def registro(func):
    def wrapper(*args, **kwargs):
        print(f'Llamada a {func.__name__} con argumentos: {args}, {kwargs}')
        return func(*args, **kwargs)

    return wrapper


@registro
def suma(a, b):
    return a + b


# Ejemplo de uso:
print(suma(3, 5))


# Ejercicio Recursivo:
# Escribe una función recursiva llamada invertir_lista que tome una lista como argumento y devuelva la lista invertida.
# No se permite el uso de bucles (for, while, etc.) en esta función.


def invertir_lista(lista):
    if not lista:
        return []
    return [lista[-1]] + invertir_lista(lista[:-1])


# Ejemplo de uso:
print(invertir_lista([1, 2, 3, 4, 5]))


# Ejercicio de Generador:
# Define un generador llamado numeros_pares que genere los primeros n números pares.
# La función debe tomar un argumento n que indique cuántos números pares se deben generar.


def generar_pares(n):
    contador = 0
    for i in range(0, n * 2):
        if i % 2 == 0:
            yield i
            contador += 1
        if contador == n:
            break


n = 5
for numero in generar_pares(n):
    print(numero)


# ----------------

# Ejercicio 1: Clausura

# Escribe una función llamada calcular_promedio que acepte una lista de números y devuelva una función
# # que calcula el promedio móvil de los últimos n números dados.


def calcular_promedio(n: int):
    valores = []

    def promedio_movil(num: float) -> float:
        valores.append(num)
        if len(valores) > n:
            valores.pop(0)
        return sum(valores) / len(valores)

    return promedio_movil


# Ejemplo de uso:
promedio_3 = calcular_promedio(3)
print(promedio_3(4))  # 4.0
print(promedio_3(6))  # 5.0
print(promedio_3(8))  # 6.0


# Ejercicio 2: Decoradores

# Escribe un decorador llamado registrar_tiempo que registre el tiempo que tarda una función decorada en ejecutarse
# y lo imprima después de cada llamada a la función.

import time


def registrar_tiempo(funcion):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f'La función {funcion.__name__} tardó {fin - inicio} segundos en ejecutarse.')
        return resultado

    return wrapper


@registrar_tiempo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Ejemplo de uso:
print(factorial(5))

# Ejercicio 3: Función Recursiva

# Escribe una función recursiva llamada fibonacci que calcule el término n de la secuencia de Fibonacci.


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Ejemplo de uso:
print(fibonacci(6))  # Salida esperada: 8

# Ejercicio 4: Generador

# Escribe un generador llamado generar_primos que genere números primos infinitamente.


def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generar_primos():
    num = 2
    while True:
        if es_primo(num):
            yield num
        num += 1


# Ejemplo de uso:
generador = generar_primos()
for _ in range(10):
    print(next(generador))
