# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text):
    num_vowels = 0
    VOWELS = 'aiueo'
    for char in text:
        if char in VOWELS:
            return num_vowels + 1
