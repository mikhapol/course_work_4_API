from _pydecimal import Decimal
from dataclasses import dataclass


def fabric_salary_hh(json):
    if json is not None:
        # print(json.get("to"))
        # return Salary(json.get("currency"), Decimal(json.get("from")), Decimal(json.get("to")))
        return Salary(json.get("currency"), json.get("from"), json.get("to"))
    else:
        return None


def fabric_salary_sj(currency, s_from, s_to):
    return Salary(currency.upper(), Decimal(s_from), Decimal(s_to))


@dataclass()
class Salary:
    currency: str
    s_from: Decimal
    s_to: Decimal

    def compare_total_mag_to(self, other):
        print(other)
        print(self.s_to)
        print(type(other))
        print(type(other.s_tos))
        print(type(self.s_to))
        if other.s_to is None:
            return False
        if self.s_to is None:
            return True

        return self.s_to.compare_total_mag(other.s_to)
