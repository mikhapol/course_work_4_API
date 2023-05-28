from src.entity.classes.head_hunter import HeadHunterAPI
from src.entity.classes.super_job import SuperJobAPI
from src.entity.classes.vacancy import fabric_vacancy_hh, fabric_vacancy_sj
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
    all_vacancies = []
    for page in range(1):
        # print("!!!!")
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
            all_vacancies.append(fabric_vacancy_hh(vacancy))
        for vacancy in sj_vacancies:
            all_vacancies.append(fabric_vacancy_sj(vacancy))
            # j_servers = JServers(vacancy)

        # print(sj_vacancies)

    while True:

        command = input("Введите команду (sort, top, del_id, end, save): ")

        if command == "sort":
            all_vacancies = sorting(all_vacancies)
            print(all_vacancies)

        elif command == "top":
            # hh_vacancies = get_hh_vacancies_list(hh_saver)
            # sj_vacancies = get_sj_vacancies_list(sj_saver)
            #
            # all_vacancies = hh_vacancies + sj_vacancies

            top_count = int(input("Введите количество вакансий для вывода: "))

            top_vacancies = get_top(all_vacancies, top_count)
            for vacancy in top_vacancies:
                print(vacancy)

        elif command == "del_id":
            j_servers.prints_id()
            j_servers.del_id(int(input("Введите id: ")))

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
