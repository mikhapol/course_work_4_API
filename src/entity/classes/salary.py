import json
from _pydecimal import Decimal
from dataclasses import dataclass


def fabric_salary_hh(json):
    if json is not None:
        return Salary(json.get("currency"), fabric_decimal(json.get("from")), fabric_decimal(json.get("to")))
    else:
        return None


def fabric_decimal(jsonObject):
    if jsonObject is not None:
        return Decimal(jsonObject)
    return None


def fabric_salary_sj(currency, s_from, s_to):
    return Salary(currency.upper(), Decimal(s_from), Decimal(s_to))


class SalaryEncoder(json.JSONEncoder):
    def default(self, obj):
        print("tl23ktgio23jgoiijog")
        if isinstance(obj, Salary):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

@dataclass()
class Salary:
    currency: str
    s_from: Decimal
    s_to: Decimal

    def getSFrom(self):
        return self.s_from

    def getSTo(self):
        return self.s_to

    def getCurrency(self):
        return self.currency

    def compare_total_mag_to(self, other):
        if other.s_to is None or other.s_to.compare(Decimal('0')) == 0:
            return True
        if self.s_to is None or self.s_to.compare(Decimal('0')) == 0:
            return False

        return self.s_to.compare(other.s_to) == 1
