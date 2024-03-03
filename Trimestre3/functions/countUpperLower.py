def count_l_and_u(example):
    upper_chars = 0
    lower_chars = 0
    for char in example:
        if char.isupper():
            upper_chars += 1
        elif char.islower():
            lower_chars += 1
    print(f'Tiene {upper_chars} mayúsculas y {lower_chars} minúsculas')
    return upper_chars, lower_chars


example = 'Mis Perros SoN Lo MÁs BoNiTo dEL Mundo'
count_l_and_u(example)
