import json  # импорт JSON

from src.entity.classes.vacancy import Vacancy, VacancyEncoder


def sorting(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортировка вакансий.
    """
    return sorted(vacancies)


def get_top(vacancies: list[Vacancy], top_count: int) -> list[Vacancy]:
    """
    Вывод количество отсортированныйх ваканcий по заданному количеству пользователя.
    """
    return sorting(vacancies)[:top_count]


def del_not_salary(vacancies_list):
    """
    Возвращает спискок без ЗП с None
    """
    if not vacancies_list:
        return

    result = []
    for entry in vacancies_list:
        if entry.get_salary() is not None and (
                entry.get_salary().get_s_from() is not None or entry.get_salary().get_s_to() is not None):
            result.append(entry)
    return result


def del_id(id: str, vacancies_list: list) -> None or list[Vacancy]:
    """
    Удаление вакансий по ID
    """
    if not vacancies_list:
        return

    result = []
    for entry in vacancies_list:
        if str(entry.get_id()) != str(id):
            result.append(entry)
    return result


def save(vacancies_list: list):
    """
    Сохранение конечного результата в формате JSON.
    """
    with open("parsed_data/result.json", 'w', encoding="utf-8") as file:
        result = "["
        for vacancy in vacancies_list:
            result = result + json.dumps(vacancy, cls=VacancyEncoder, indent=4, ensure_ascii=False) + ","
        result = result[:-1] + "]"
        file.write(result)


def currencys(vacancies_list):
    """
    Возвращает перечень валюты без повторений.
    """
    if not vacancies_list:
        return
    result = set()
    for entry in vacancies_list:
        if entry.get_salary() is not None:
            result.add(entry.get_salary().get_currency())
    return ", ".join(result)


def vacancies_list_from_currency(currency: str, vacancies_list: list) -> None or list:
    """
    Возвращает список ваканчий с выбранной валютой.
    """
    if not vacancies_list:
        return
    result = []
    for entry in vacancies_list:
        if entry.get_salary() is not None \
                and entry.get_salary().get_currency() is not None \
                and entry.get_salary().get_currency() == currency:
            result.append(entry)
    return result
