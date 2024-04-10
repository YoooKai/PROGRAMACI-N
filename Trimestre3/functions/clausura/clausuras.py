# closure: devuelve la función interna de una función externa. Permite usar las variables dela función externa y usarlas de nuevo una vez se ha salido de la func.

def make_multiplier(x: int):
    def multiplier(n: int):
        return x * n
    return multiplier

m4 = make_multiplier(4)
m4(7) # 4 * 7


## otro ejemplo
def closure(parametro):
    def funAretornar():
        return parametro+1
    return funAretornar
recibeFunc=closure(8)
result = recibeFunc()
print(result)

## otro ejemplo de que sea mayor que 0
def closure_validador(a, b):
    def validar():
        if a>0 and b>0:
            return True
        return False
    return validar
validado = closure_validador(4, 5)
print(validado())


# otro ejemplo

def enter_number_outer():
    numbers = []
    def enter_numbers_inner(x):
        numbers.append(x)
        print(numbers)
    return enter_numbers_inner

enter_num = enter_number_outer()
enter_num(3)
enter_num(7)

# contar
def init_count():
    count = 0
    def add(amount):
        nonlocal count
        count += amount
    return add
add = init_count()
add(3)
add(6)

# imprimir hi
def outer_func():
    message = 'HII'
    def inner_func():
        print(message)
    return inner_func
res_func = outer_func()
print(res_func())

#recibiendo mensaje
def outer_func(mensaje):
    message = mensaje
    def inner_func():
        print(message)
    return inner_func
hey_func = outer_func
print(outer_func())

#luces tráfico
def create_traffic_light_validator():
    traffic_light_colors = ('GREEN', 'RED', 'ORANGE')
    def is_valid_light(color):
        if color.lower() in list(map(str.lower, traffic_light_colors)):
            return True
        return False
    return is_valid_light
validator = create_traffic_light_validator()
print(validator('GREEN'))
print(validator('BLUE'))

# función generadora de números pares
def numeros_pares():
    num_par = 0
    def gen_pares():
        nonlocal num_par
        num_par += 2
        print(num_par)
    return gen_pares
generador = numeros_pares()
generador()

# contador
def contador():
    counter = 0
    def contar():
        nonlocal counter
        counter +=1
    return contar

contador_llamadas = contador()
contador_llamadas()

#promedio de una secuencia de números. 
#Sin embargo, en lugar de pasar todos los números de una vez, deseas poder pasar un número a la vez y obtener el promedio actualizado después de cada llamada.
# La función debe mantener el estado del número total de elementos y la suma acumulada de los números para calcular el promedio.

def crear_calculador_promedio():
    numeros = []
    suma_total = 0
    
    def calcular_promedio_actual(nuevo_numero):
        nonlocal suma_total
        numeros.append(nuevo_numero)
        suma_total += nuevo_numero
        promedio_actual = suma_total / len(numeros)
        return promedio_actual
    
    return calcular_promedio_actual

#  una función que te permita calcular la suma acumulada de una secuencia de números.
def crear_suma_acumulada ():
    suma_total = 0
    def calcular_suma_acumulada(numero):
        nonlocal suma_total
        suma_total+= numero
        return suma_total
    return calcular_suma_acumulada


# una función llamada gestor_nombres que funcione de esta manera utilizando una clausura. 
#La función debe tener métodos para agregar un nombre a la lista, obtener la lista completa de nombres y borrar todos los nombres de la lista.

def gestor_nombres():
    nombres = []
    
    def agregar_nombre(nombre):
        nonlocal nombres
        nombres.append(nombre)
        return nombres
    
    def obtener_nombres():
        nonlocal nombres
        return nombres
    
    def borrar_nombres():
        nonlocal nombres
        nombres.clear()
        return nombres
    
    return agregar_nombre, obtener_nombres, borrar_nombres

# Definir la función gestor_nombres y obtener sus métodos
agregar_nombre, obtener_nombres, borrar_nombres = gestor_nombres()

# Agregar nombres a la lista
agregar_nombre("Juan")
agregar_nombre("María")
agregar_nombre("Pedro")

# Obtener la lista completa de nombres
lista_nombres = obtener_nombres()
print("Lista de nombres:", lista_nombres)

# Borrar todos los nombres de la lista
borrar_nombres()
print("Lista de nombres después de borrar:", obtener_nombres())
