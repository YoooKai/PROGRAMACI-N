# ********
# PANGRAMA
# ********


def is_pangram(text):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    text_uniquechars = set(text.lower())
    for char in text_uniquechars:
        if char in ALPHABET:
            ALPHABET = ALPHABET.replace(char, '')
    return len(ALPHABET) == 0
