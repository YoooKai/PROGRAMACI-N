# DECORADORES
# Los decoradores en Python son funciones que envuelven otras funciones para extender su funcionalidad sin modificar su código.
# Los decoradores son una forma elegante de modificar o extender el comportamiento de una función.


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Antes de ejecutar la función')
        result = func(*args, **kwargs)
        print('Después de ejecutar mi función')
        return result

    return wrapper


@my_decorator
def my_func():
    print('Esta es la función a decorar')


my_func()


# -------------función para añadir 1----------


def my_decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1

    return wrapper


@my_decor
def add(x, y):
    return x + y


# -------------función para añadir num personalizado, o el tipo de valor para decorar----------
def suc(num=1):
    def my_decor(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + num

        return wrapper

    return my_decor


@suc(num=5)
def add(x, y):
    return x + y


print(add(3, 5))


# -----------------------imprime mensajes antes de ejecutar func-----------------------------------------
def imprimir_argumentos(funcion):
    def wrapper(*args, **kwargs):
        print('Argumentos posicionales:', args)
        print('Argumentos de palabra clave:', kwargs)
        resultado = funcion(*args, **kwargs)
        return resultado

    return wrapper


@imprimir_argumentos
def suma(a, b):
    return a + b


# ----------------contar llamadas---------------
def count_calls(func):
    calls = 0

    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        result = func(*args, **kwargs)
        print(f'Se ha llamado a esta función {calls} veces')
        return result

    return wrapper


# ----------- divisor inteliogente
def smart_divide(func):
    def wrapper(a, b):
        print('I am going to divide', a, 'and', b)
        if b == 0:
            print('Whoops! cannot divide')
            return

        return func(a, b)

    return wrapper


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)

divide(2, 0)

# multiples decoradores


def star(func):
    def inner(*args, **kwargs):
        print('*' * 15)
        func(*args, **kwargs)
        print('*' * 15)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print('%' * 15)
        func(*args, **kwargs)
        print('%' * 15)

    return inner


@star
@percent
def printer(msg):
    print(msg)


printer('Hello')

# ***************
# %%%%%%%%%%%%%%%
# Hello
# %%%%%%%%%%%%%%%
# ***************

# verificar que sean nums int, usando no resultado de func a decorar sino sus args


def assert_int(func):
    def wrapper(value1: int, value2: int, /) -> int | float | None:
        if isinstance(value1, int) and isinstance(value2, int):
            return func(value1, value2)
        return None

    return wrapper


@assert_int
def _sum(a, b):
    return a + b


# ---------comprobar que todos los argus sean de x tipo (deco con paramtros)
def assert_type(atype):
    def decorator(func):
        def wrapper(*args, **kwargs):
            all_args_with_atype = all(isinstance(a, atype) for a in args)
            all_kwargs_with_atype = all(isinstance(a, atype) for a in kwargs.values())
            if all_args_with_atype and all_kwargs_with_atype:
                return func(*args, **kwargs)
            return None

        return wrapper

    return decorator


@assert_type(float)
def _sum(a, b):
    return a + b


# determina que sean positivos y numerales y func factorial


def assert_positive(func):
    def wrapper(*args, **kwargs):
        # Verificar los argumentos posicionales
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                return 0
        # Verificar los argumentos nominales
        for kwarg, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                return 0
        # Llamar a la función original si todos los argumentos son positivos
        return func(*args, **kwargs)

    return wrapper


@assert_positive
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)
