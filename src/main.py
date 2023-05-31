from src.entity.classes.head_hunter import HeadHunterAPI
from src.entity.classes.super_job import SuperJobAPI
from src.entity.classes.vacancy import fabric_vacancy_hh, fabric_vacancy_sj
from src.entity.vacancy_utils import sorting, get_top, del_id, del_not_salary, currencys, vacancies_list_from_currency, \
    save


def main():
    """
    Запуск программы
    """
    keyword = input("Введите ключевое слово для поиска вакансий: ").title()
    # keyword = "Python"

    print(f'Идёт поиск по keyword: "{keyword}"!')
    hh_engine = HeadHunterAPI(keyword)
    sj_engine = SuperJobAPI(keyword)

    hh_saver = hh_engine.get_json_saver("parsed_data/hh_vacancies.json")
    sj_saver = sj_engine.get_json_saver("parsed_data/sj_vacancies.json")

    vacancies_list = []
    for page in range(1):
        hh_vacancies = hh_engine.get_request().json()["items"]
        for vacancy in hh_vacancies:
            hh_saver.insert(vacancy)

        sj_vacancies = sj_engine.get_request().json()["objects"]
        for vacancy in sj_vacancies:
            sj_saver.insert(vacancy)

        for vacancy in hh_vacancies:
            vacancies_list.append(fabric_vacancy_hh(vacancy))
        for vacancy in sj_vacancies:
            vacancies_list.append(fabric_vacancy_sj(vacancy))
        print(f"Найдено: HH = {len(hh_vacancies)}, SJ = {len(sj_vacancies)} вакансий!")

    while True:

        command = input("""Введите команду: <sort> - сортировка по ЗП "ДО".
                 <top> - ТОП по количеству.
                    <del_s> - удаление если ЗП неизвестно.
                    <del_id> - удаление по ID.
                 <currency> - выборка вакансий по валюте.
                 <save> - сохренение в файл JSON.
                 <end> - завершение с очистка загрузочных файлов JSON.\nВАШ ВЫБОР: """).lower()

        if command == "sort":
            vacancies_sort = sorting(vacancies_list)
            for vacancy in vacancies_sort:
                vacancy.print_vacancy()
            print(f'ИТОГО: {len(vacancies_sort)}')

        elif command == "top":
            top_count = int(input("Введите количество вакансий для вывода: "))
            top_vacancies = get_top(vacancies_list, top_count)
            for vacancy in top_vacancies:
                vacancy.print_vacancy()
            print(f'ИТОГО: {len(top_vacancies)}')

        elif command == "del_s":
            vacancies_list = del_not_salary(vacancies_list)
            for vacancy in vacancies_list:
                vacancy.print_vacancy()
            print(f'ИТОГО: {len(vacancies_list)}')

        elif command == "del_id":
            for vacancy in vacancies_list:
                vacancy.print_vacancy()
            print(len(vacancies_list))
            vacancies_list = del_id(input("Введите id: "), vacancies_list)
            for vacancy in vacancies_list:
                vacancy.print_vacancy()
            print(f'ИТОГО: {len(vacancies_list)}')

        elif command == "currency":
            print(currencys(vacancies_list))
            vacancies_currencys = vacancies_list_from_currency(input("Введите валюту: "), vacancies_list)
            for vacancy in vacancies_currencys:
                vacancy.print_vacancy()
            print(f'ИТОГО: {len(vacancies_currencys)}')

        elif command == "save":
            save(vacancies_list)

        elif command == "end":
            hh_saver.clear_data()
            sj_saver.clear_data()
            break

        else:
            print("Некорректная команда. Попробуйте ещё раз.")


if __name__ == '__main__':
    main()
