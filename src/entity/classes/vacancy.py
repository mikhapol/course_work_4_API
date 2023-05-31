import json
from dataclasses import dataclass

from _decimal import Decimal

from src.entity.classes.salary import fabric_salary_hh, fabric_salary_sj, Salary


def fabric_vacancy_hh(json_hh):
    return Vacancy(str(json_hh.get("id")), json_hh.get("name"), json_hh.get("alternate_url"),
                   json_hh.get("snippet", {}).get("responsibility"), json_hh.get("area", {}).get("name"),
                   fabric_salary_hh(json_hh.get("salary")), "HH")


def fabric_vacancy_sj(json_sj):
    return Vacancy(str(json_sj.get("id")), json_sj.get("profession"), json_sj.get("link"), json_sj.get("candidat"),
                   json_sj.get("town", {}).get("title"), fabric_salary_sj(json_sj.get("currency"), json_sj.get("payment_from"),
                                                                          json_sj.get("payment_to")), "SJ")


class VacancyEncoder(json.JSONEncoder):
    def default(self, obj: str):
        if isinstance(obj, Vacancy):
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
        salary = "неизвестна."
        if self.salary is not None:
            salary = self.salary.str()
        print(f'{self.key}, ID: {self.id}. ВАКАНСИЯ: {self.title}. ГОРОД: {self.city}. ЗП {salary}')

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        if other.salary is None:
            return True
        if self.salary is None:
            return False

        return self.salary.__lt__(other.salary)
