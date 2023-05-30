import json
from dataclasses import dataclass

from _decimal import Decimal

from src.entity.classes.salary import fabric_salary_hh, fabric_salary_sj, Salary


def fabric_vacancy_hh(json):
    return Vacancy(str(json.get("id")), json.get("name"), json.get("alternate_url"),
                   json.get("snippet", {}).get("responsibility"), json.get("area", {}).get("name"),
                   fabric_salary_hh(json.get("salary")), "HH")


def fabric_vacancy_sj(json):
    return Vacancy(str(json.get("id")), json.get("profession"), json.get("link"), json.get("candidat"),
                   json.get("town", {}).get("title"), fabric_salary_sj(json.get("currency"), json.get("payment_from"),
                                                                       json.get("payment_to")), "SJ")


class VacancyEncoder(json.JSONEncoder):
    def default(self, obj: str):
        print("start default")
        print(obj)
        print(type(obj))
        if isinstance(obj, Vacancy):
            print("!$!$@@#!")
            return obj.__dict__
        if isinstance(obj, Salary):
            return obj.__dict__
        if isinstance(obj, Decimal):
            return
        return json.JSONEncoder.default(self, obj)


@dataclass
class Vacancy:
    id: str
    title: str
    link: str
    description: str
    city: str
    salary: Salary
    key: str

    def get_id(self):
        return self.id

    def get_salary(self):
        return self.salary

    def print_vacancy(self):
        print(f'{self.key}, ID-{self.id}. ВАКАНСИЯ: {self.title}. ГОРОД: {self.city}. ЗП: {self.salary.print_sal()}')

    def __gt__(self, other):
        print("Start gt")
        return self.salary > other.salary

    def __lt__(self, other):
        if other.salary is None:
            return True
        if self.salary is None:
            return False

        return self.salary.compare_total_mag_to(other.salary)
