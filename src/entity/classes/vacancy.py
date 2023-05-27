from dataclasses import dataclass

from src.entity.classes.salary import fabric_salary_hh, fabric_salary_sj, Salary


def fabric_vacancy_HH(json):
    return Vacancy(json.get("id"), json.get("name"), json.get("alternate_url"), json.get("snippet.responsibility"),
                   json.get("area.name"), fabric_salary_hh(json.get("salary")), "HH")


def fabric_vacancy_SJ(json):
    return Vacancy(json.get("id"), json.get("profession"), json.get("link"), json.get("candidat"),
                   json.get("town.title"),
                   fabric_salary_sj(json.get("currency"), json.get("payment_from"), json.get("payment_to")), "SJ")


@dataclass()
class Vacancy:
    id: str
    title: str
    link: str
    description: str
    city: str
    # Зарплата
    salary: Salary
    key: str

    # __slots__ = ["__id", "__title", "__link", "__description", "__salary", "__city", "__key"]

    def __init__(self, id, title, link, description, city, salary, key) -> None:
        self.id = str(id)
        self.title = title
        self.link = link
        self.description = description
        self.city = city
        # Зарплата
        self.salary = salary
        self.key = key

    #
    # def __repr__(self):
    #     return self.__str__()
    #
    # def __str__(self):
    #     return " self.id= ", self.id, " self.title= ", self.title, " self.link= ", self.link, " self.description= ", \
    #         self.description, " self.city= ", self.city, " self.salary= ", self.salary, " self.key= ", self.key

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):

        if other.salary is None or other.salary.s_to is None:
            return False
        if self.salary is None or self.salary.s_to:
            return True

        return self.salary.compare_total_mag_to(other.salary)
