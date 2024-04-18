# *******************
# CREANDO OPERACIONES
# *******************


def make_oper(oper: str):
    def ioper(a, b):
        match oper:
            case 'add':
                return a + b
            case 'sub':
                return a - b
            case 'mul':
                return a * b
            case 'div':
                return a / b
            case _:
                return None

    return ioper


def run(oper: str, num1: int, num2: int) -> float:
    return make_oper(oper)(num1, num2)
