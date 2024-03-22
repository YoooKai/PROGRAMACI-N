# **********
# PALÍNDROMO
# **********


def is_palindrome(text):
    joined_lower_text = text.replace(' ', '').lower()
    reversed_text = joined_lower_text[::-1]
    return joined_lower_text == reversed_text
