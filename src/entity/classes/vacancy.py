import json
from dataclasses import dataclass

from _decimal import Decimal

from src.entity.classes.salary import fabric_salary_hh, fabric_salary_sj, Salary


def fabric_vacancy_hh(json):
    return Vacancy(str(json.get("id")), json.get("name"), json.get("alternate_url"), json.get("snippet.responsibility"),
                   json.get("area.name"), fabric_salary_hh(json.get("salary")), "HH")


def fabric_vacancy_sj(json):
    return Vacancy(str(json.get("id")), json.get("profession"), json.get("link"), json.get("candidat"),
                   json.get("town.title"), fabric_salary_sj(json.get("currency"), json.get("payment_from"),
                                                            json.get("payment_to")), "SJ")


class VacancyEncoder(json.JSONEncoder):
    def default(self, obj):
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

@dataclass()
class Vacancy:
    id: str
    title: str
    link: str
    description: str
    city: str
    salary: Salary
    key: str

    def getId(self):
        return self.id

    def getSalary(self):
        return self.salary

    def print_salary(self):
        print(" self.id= ", self.id, " self.title= ", self.title, " self.salary= ", self.salary)
    def print(self):
        description =''
        if self.description is not None:
            description = self.description.replace("\n", "")
        print(" self.id= ", self.id, " self.title= ", self.title, " self.link= ", self.link, " self.description= ",
              description, " self.city= ", self.city, " self.salary= ", self.salary, " self.key= ", self.key)

    def __gt__(self, other):
        print("Start gt")
        return self.salary > other.salary

    def __lt__(self, other):
        if other.salary is None:
            return True
        if self.salary is None:
            return False

        return self.salary.compare_total_mag_to(other.salary)
