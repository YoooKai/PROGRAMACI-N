# *********************************
# SEPARANDO MAYÚSCULAS Y MINÚSCULAS
# *********************************


def split_case(words):
    upper_words = []
    lower_words = []
    for word in words:
        if word.isupper():
            lower_words.append(word)
        elif word.islower():
            upper_words.append(word)
    return upper_words, lower_words
