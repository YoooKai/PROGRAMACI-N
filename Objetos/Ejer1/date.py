from __future__ import annotations


class Date:
    DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    DAYS = ['DOMINGO', 'LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'SÁBADO', 'DOMINGO']
    MONTHS = [
        'ENERO',
        'FEBRERO',
        'MARZO',
        'ABRIL',
        'MAYO',
        'JUNIO',
        'JULIO',
        'AGOSTO',
        'SEPTIEMPRE',
        'OCTUBRE',
        'NOVIEMBRE',
        'DICIEMBRE',
    ]

    def __init__(self, day: int, month: int, year: int):
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        """
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year: int) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month == 2 and Date.is_leap_year(year):
            return 29
        return Date.DAYS_OF_MONTH[month - 1]

    def get_delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        ...
        leap_year_days = 366
        avg_year_days = 365
        total_days = 0
        # años
        for year in range(1900, self.year):
            if self.is_leap_year(year):
                total_days += leap_year_days
            else:
                total_days += avg_year_days
        # meses
        for month in range(1, self.month):
            total_days += Date.DAYS_OF_MONTH[month - 1]
        # días
        total_days += self.day

        return total_days

    @property
    def weekday(self) -> int:
        """Día de la semana de la fecha (0 para domingo, ..., 6 para sábado)."""
        total_days = self.get_delta_days()
        total_days += 1
        total_days % 7
        return total_days

    @property
    def is_weekend(self) -> bool:
        return self.weekday == 0 or self.weekday == 6

    @property
    def short_date(self) -> str:
        """02/09/2003"""
        return f'{self.day:02}/{self.month}/{self.year}'

    def __str__(self):
        """MARTES 2 DE SEPTIEMBRE DE 2003"""

        return f'{self.DAYS[self.weekday]} {self.day} DE {self.month}'

    def __add__(self, days: int) -> Date:
        """Sumar un número de días a la fecha"""

        if days >= 365:
            old_year = self.year
            self.year += days // 365
            for year in range(old_year, self.year):
                if self.is_leap_year(year):
                    self.days += 1

    def __sub__(self, other: Date | int) -> int | Date:
        """Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha"""

    pass

    def __lt__(self, other) -> bool:
        if self.year < other.year:
            return True
        if self.month < other.month:
            return True
        if self.day < other.day:
            return True
        return False

    def __gt__(self, other) -> bool:
        if self.year > other.year:
            return True
        if self.month > other.month:
            return True
        if self.day > other.day:
            return True
        return False

    def __eq__(self, other) -> bool:
        return self.year == other.year and self.month == other.month and self.day == other.day






----
---


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
        for sequence_a, sequence_b in zip(self.sequence, other.sequence):
            if sequence_a > sequence_b:
                DNA_sequence.append(sequence_a)
            elif sequence_b > sequence_a:
                DNA_sequence.append(sequence_b)

        return DNA(''.join(DNA_sequence))

    def __len__(self):
        """Longitud de la secuencia de ADN"""
        return len(self.sequence)

    def stats(self) -> dict[str, float]:
        """Porcentaje de aparición de cada base con respecto al total.
        Se devuelve un diccionario donde la clave será la base nitrogenada
        y el valor será el porcentaje."""
        percent_divisor = len(self) * 100
        return {
            DNA.ADENINE: self.adenines / percent_divisor,
            DNA.CYTOSINE: self.cytosines / percent_divisor,
            DNA.GUANINE: self.guanines / percent_divisor,
            DNA.THYMINE: self.thymines / percent_divisor,
        }

    def __mul__(self, other: DNA) -> DNA:
        """Se define la multiplicación de dos secuencias de ADN como una nueva cadena
        de ADN donde aparecen las bases que son iguales (posición a posición)"""
        DNA_result = []
        for sequence_a, sequence_b in zip(self.sequence, other.sequence):
            if sequence_a == sequence_b:
                DNA_result.append(sequence_a)
        return DNA(str(DNA_result))

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
        with open(path) as f:
            f.write(self.sequence)

    def __getitem__(self, index: int) -> str:
        """Devuelve la base que ocupa la posición 'index'"""
        return self.sequence[index]

    def __setitem__(self, index: int, base: str) -> None:
        """Fija la base 'base' en la posición 'index'"""
        acceptable_bases = ['A', 'C', 'G', 'T']
        if base not in acceptable_bases:
            self.sequence[index] == acceptable_bases[0]
        else:
            self.sequence[index] == base

