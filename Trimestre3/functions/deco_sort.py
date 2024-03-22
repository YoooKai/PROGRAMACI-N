def sort(asc=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if asc:
                return sorted(result)
            else:
                return sorted(result, reverse=True)

        return wrapper

    return decorator


@sort()
def extract_evens(*values):
    return (v for v in values if v % 2 == 0)


print(extract_evens(1, 4, 6, 6, 7, 8, 12))
