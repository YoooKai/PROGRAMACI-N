# ****************************
# REDONDEANDO CON UN DECORADOR
# ****************************


def cround(num_decimals: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return round(func(*args, **kwargs), num_decimals)

        return wrapper

    return decorator


@cround(2)
def avg(values: list) -> float:
    return sum(values) / len(values)


if __name__ == '__main__':
    avg([6, 3, 9, 3, 5, 4, 5, 7, 2, 3, 6])
