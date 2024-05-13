from __future__ import annotations


class DNA:
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'

    def __init__(self, sequence: str):
        self.sequence = sequence

    def __str__(self):
        return str(self.sequence)

    @property
    def adenines(self) -> int:
        """Número de adeninas de la secuencia de ADN"""
        return self.sequence.count(self.ADENINE)

    @property
    def cytosines(self) -> int:
        """Número de citosinas de la secuencia de ADN"""
        return self.sequence.count(self.CYTOSINE)

    @property
    def guanines(self) -> int:
        """Número de guaninas de la secuencia de ADN"""
        return self.sequence.count(self.GUANINE)

    @property
    def thymines(self) -> int:
        """Número de timinas de la secuencia de ADN"""
        return self.sequence.count(self.THYMINE)

    def __add__(self, other: DNA) -> DNA:
        """Se define la suma de dos secuencias de ADN como el máximo de cada base nitrogenada
        (base a base). Por ejemplo 'T' sería mayor que 'A'.
        Si las secuencias no tienen la misma longitud, habrá que aplicar el máximo base a base
        hasta donde se pueda, y completar el resto de la secuencia con la parte que falte, bien
        de la primera o bien de la segunda secuencia, en función de cuál sea mayor.
        """
        DNA_sequence = []
        for base_a, base_b in zip(self.sequence, other.sequence):
            if base_a > base_b:
                DNA_sequence.append(base_a)
            else:
                DNA_sequence.append(base_b)

        if len(self.sequence) < len(other.sequence):
            DNA_sequence.extend(other.sequence[len(self.sequence) :])
        elif len(self.sequence) > len(other.sequence):
            DNA_sequence.extend(self.sequence[len(other.sequence) :])

        return DNA(''.join(DNA_sequence))

    def __len__(self):
        """Longitud de la secuencia de ADN"""
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        """Porcentaje de aparición de cada base con respecto al total.
        Se devuelve un diccionario donde la clave será la base nitrogenada
        y el valor será el porcentaje."""
        return {
            DNA.ADENINE: self.adenines / len(self) * 100,
            DNA.CYTOSINE: self.cytosines / len(self) * 100,
            DNA.GUANINE: self.guanines / len(self) * 100,
            DNA.THYMINE: self.thymines / len(self) * 100,
        }

    def __mul__(self, other: DNA) -> DNA:
        """Se define la multiplicación de dos secuencias de ADN como una nueva cadena
        de ADN donde aparecen las bases que son iguales (posición a posición)"""
        DNA_result = ''
        for sequence_a, sequence_b in zip(self.sequence, other.sequence):
            if sequence_a == sequence_b:
                DNA_result += sequence_a
        return DNA(DNA_result)

    @classmethod
    def build_from_file(cls, path: str) -> DNA:
        """Construye una secuencia de ADN a partir de un fichero.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        with open(path) as f:
            return DNA(f.readline())

    def dump_to_file(self, path: str) -> None:
        """Vuelca una secuencia de ADN a un fichero de salida.
        El formato del fichero es tener una única línea con todas las bases
        una detrás de otra."""
        with open(path, 'w') as f:
            f.write(self.sequence)

    def __getitem__(self, index: int) -> str:
        """Devuelve la base que ocupa la posición 'index'"""
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        """Fija la base 'base' en la posición 'index'"""
        acceptable_bases = ['A', 'C', 'G', 'T']
        sequence_list = list(self.sequence)
        if base in acceptable_bases:
            sequence_list[index] = base
        else:
            sequence_list[index] = acceptable_bases[0]
        self.sequence = ''.join(sequence_list)
