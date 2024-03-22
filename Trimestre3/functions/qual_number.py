def get_qual_number(n: int):
    result = []
    val = 0
    for char in reversed(str(n)):
        val += char
        if len(val) == 3:
            result.append(f'{val},')
            val = 0
    return str(reversed(result))


print(get_qual_number(134123))
