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
