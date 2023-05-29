import json

from src.entity.classes.vacancy import Vacancy, VacancyEncoder


def sorting(vacancies) -> list[Vacancy]:
    return sorted(vacancies)


def get_top(vacancies: list[Vacancy], top_count: int) -> list[Vacancy]:
    return sorting(vacancies)[:top_count]


def del_id(id, vacancies_list):
    if not vacancies_list:
        return

    result = []
    for entry in vacancies_list:
        if str(entry.getId()) != str(id):
            result.append(entry)
    return result


def save_result(vacancies_list):
    with open("parsed_data/result", 'w') as file:
        print(vacancies_list[0])
        print("!!#!@43124")
        print(json.dumps(vacancies_list[0], cls=VacancyEncoder))
        file.write(json.loads(vacancies_list))


def vac_currency(currency, vacancies_list):
    if not vacancies_list:
        return
    result = []
    for entry in vacancies_list:
        if entry.getSalary() is not None \
                and entry.getSalary().getCurrency() is not None \
                and entry.getSalary().getCurrency() == currency:
            result.append(entry)
    return result


def currencys(vacancies_list):
    if not vacancies_list:
        return
    result = set()
    for entry in vacancies_list:
        if entry.getSalary() is not None:
            result.add(entry.getSalary().getCurrency())
    return result


def del_zp(vacancies_list):
    if not vacancies_list:
        return

    result = []
    for entry in vacancies_list:
        if entry.getSalary() is not None and (
                entry.getSalary().getSFrom() is not None or entry.getSalary().getSTo() is not None):
            result.append(entry)
    return result

#
# def get_hh_vacancies_list(json_saver) -> list[HHVacancy]:
#     vacancies = [
#         HHVacancy(
#             title=vacancy["name"],
#             link=vacancy["alternate_url"],
#             description=vacancy["snippet"],
#             salary=vacancy["salary"]["from"] if vacancy.get("salary") else None)
#
#         for vacancy in json_saver.select()]
#
#     return vacancies

#
# def get_sj_vacancies_list(json_saver) -> list[SJVacancy]:
#     vacancies = [
#
#         SJVacancy(
#             title=vacancy["profession"],
#             link=vacancy["link"],
#             description=vacancy["candidat"],
#             salary=vacancy["payment_from"])
#
#         for vacancy in json_saver.select()]
#     return vacancies
