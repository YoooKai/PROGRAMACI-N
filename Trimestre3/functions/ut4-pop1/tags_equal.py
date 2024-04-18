# **********************
# ETIQUETAS EQUIVALENTES
# **********************


def get_tagname(tag: str) -> str:
    return tag.strip('<>').split()[0].lower()


def run(tag1: str, tag2: str):
    return get_tagname(tag1) == get_tagname(tag2)
