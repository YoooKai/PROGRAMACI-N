#clausura que trocee caddenas
def mslice(window_size: int=1):
    text_slices = []
    def helper(text: str) -> list[str]:
        for cutpos in range(0, len(text), window_size):
            text[cutpos:cutpos+window_size]
            text_slices.append(slice)
        return text_slices
    return helper
    s3 = mslice(3)
    s3('Hola amigos estoy cansado')

#como función generadora
def mslice(window_size: int=1):
    def helper(text: str):
        for cutpos in range(0, len(text), window_size):
            yield text[cutpos:cutpos+window_size]
    return helper

#función recursiva
def rslice(text: str, window: int)-> list[str]:
    if len(text) == 0:
        return []
    return [text[0:window]] + rslice(text[window:], window)
