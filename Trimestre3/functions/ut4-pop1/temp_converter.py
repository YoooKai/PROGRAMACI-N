# ************************
# CONVERSOR DE TEMPERATURA
# ************************


def temp_converter(source: str):
    def helper(temp: float) -> float | None:
        match source:
            case 'c2f':
                return (temp * 9 / 5) + 32
            case 'f2c':
                return (temp - 32) * (5 / 9)
            case _:
                return None

    return helper


def run(source: str, temp: float) -> float | None:
    converter = temp_converter(source)
    result = round(converter(temp), 2)
    return result
