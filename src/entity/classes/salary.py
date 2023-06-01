from dataclasses import dataclass


def fabric_salary_hh(json_hh):
    """
    Функция получения данных о ЗП из JSON hh.
    """
    if json_hh is not None:
        return Salary(json_hh.get("currency"),
                      fabric_float_json(json_hh.get("from")),
                      fabric_float_json(json_hh.get("to")))
    else:
        return None


def fabric_salary_sj(currency, s_from, s_to):
    """
    Функция получения данных о ЗП из JSON sj.
    """
    return Salary(currency.upper(),
                  fabric_float_json(s_from),
                  fabric_float_json(s_to))


def fabric_float_json(json_object):
    """
    Функция переобразования данный с плавоющей точкой для работы с ЗП.
    """
    if json_object is not None:
        return float(json_object)
    return None


@dataclass
class Salary:  # Использование @dataclass
    currency: str
    s_from: float
    s_to: float

    def get_s_from(self):
        """Для обращения и работы с ЗП "от" вне класса"""
        return self.s_from

    def get_s_to(self):
        """Для обращения и работы с ЗП "до" вне класса"""
        return self.s_to

    def get_currency(self):
        """Для обращения и работы с курсом валют вне класса"""
        return self.currency

    def str(self):
        """Возвращение стройкой информацию о ЗП"""
        return f'в {self.currency}: от {self.s_from}, до {self.s_to}.'

    def __lt__(self, other):
        """
        Магический метод для сравнения со знаком "меньше <"
        """
        if other.s_to is None or other.s_to == 0:
            return True
        if self.s_to is None or self.s_to == 0:
            return False

        return other.s_to < self.s_to
