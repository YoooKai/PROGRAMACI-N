# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************


def result_as_status(func):
    def wrapper(*args, **kwargs):
        status, result = func(*args, **kwargs)
        return dict(status=status, result=result)

    return wrapper


@result_as_status
def run(values: list):
    s = 0
    for value in values:
        if isinstance(value, int):
            s += value
        else:
            return False, 'Not int value found'
    return True, s


if __name__ == '__main__':
    run([3, 4, 2])
