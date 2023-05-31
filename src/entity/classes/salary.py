import json
from _pydecimal import Decimal
from dataclasses import dataclass


def fabric_salary_hh(json_hh):
    if json_hh is not None:
        return Salary(json_hh.get("currency"), fabric_float_json(json_hh.get("from")), fabric_float_json(json_hh.get("to")))
    else:
        return None


def fabric_salary_sj(currency, s_from, s_to):
    return Salary(currency.upper(), fabric_float_json(s_from), fabric_float_json(s_to))


def fabric_float_json(json_object):
    if json_object is not None:
        return float(json_object)
    return None


@dataclass
class Salary:
    currency: str
    s_from: float
    s_to: float

    def get_s_from(self):
        return self.s_from

    def get_s_to(self):
        return self.s_to

    def get_currency(self):
        return self.currency

    def str(self):
        return f'в {self.currency}: от {self.s_from}, до {self.s_to}.'

    def __lt__(self, other):
        if other.s_to is None or other.s_to == 0:
            return True
        if self.s_to is None or self.s_to == 0:
            return False

        return self.s_to > other.s_to
