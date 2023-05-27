from src.entity.classes.head_hunter import HeadHunterAPI
from src.entity.classes.super_job import SuperJobAPI
from src.entity.classes.vacancy import fabric_vacancy_HH, fabric_vacancy_SJ
from src.entity.utils import sorting, get_top


def main():
    """
    Запуск программы
    """
    # keyword = input("Введите ключевое слово для поиска вакансий: ")

    keyword = "Python"
    print(f'Идёт поиск по keyword: {keyword}!')
    hh_engine = HeadHunterAPI(keyword)
    sj_engine = SuperJobAPI(keyword)

    hh_saver = hh_engine.get_json_saver("parsed_data/hh_vacancies.json")
    sj_saver = sj_engine.get_json_saver("parsed_data/sj_vacancies.json")

    j_servers = None
    vacancys = []
    for page in range(1):
        print("!!!!")
        hh_vacancies = hh_engine.get_request().json()["items"]
        for vacancy in hh_vacancies:
            hh_saver.insert(vacancy)
        # print(hh_vacancies)

        sj_vacancies = sj_engine.get_request().json()["objects"]
        for vacancy in sj_vacancies:
            sj_saver.insert(vacancy)

        # j_servers = JServers([hh_saver, sj_saver])
        #
        for vacancy in hh_vacancies:
            vacancys.append(fabric_vacancy_HH(vacancy))
        for vacancy in sj_vacancies:
            vacancys.append(fabric_vacancy_SJ(vacancy))
            # j_servers = JServers(vacancy)

        # print(sj_vacancies)

    while True:

        command = input("Введите команду (sort, top, del_id, end, save): ")

        if command == "sort":
            vacancys = sorting(vacancys)
            print(vacancys)

        elif command == "top":
            hh_vacancies = get_hh_vacancies_list(hh_saver)
            sj_vacancies = get_sj_vacancies_list(sj_saver)

            all_vacancies = hh_vacancies + sj_vacancies

            top_count = int(input("Введите количество вакансий для вывода: "))

            top_vacancies = get_top(all_vacancies, top_count)
            for vacancy in top_vacancies:
                print(vacancy)
        elif command == "del_id":
            j_servers.prints()
            j_servers.deletes(int(input("Введите id: ")))

        elif command == "end":
            hh_saver.clear_data()
            sj_saver.clear_data()

            break
        else:
            print("Некорректная команда. Попробуйте ещё раз.")

        # continue_running = input("Хотите продолжить работу с программой? (y/n): ")

        # if continue_running.lower() == "n":
        #     hh_saver.clear_data()
        #     sj_saver.clear_data()
        #
        #     break


if __name__ == '__main__':
    main()
