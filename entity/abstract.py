from abc import ABC, abstractmethod


class AbstractVacancyAPI(ABC):
    """AbstractVacancyAPI - абстрактный базовый класс для API, который определяет метод """
    @abstractmethod
    def get_vacancies(self, search_vacancy):
        """get_vacancies() для получения списка вакансий."""
        pass


class AbstractVacancyManager(ABC):
    """
    Абстрактные методы:
    `add_vacancy` - добавление
    `get_vacancies` - получение
    `delete_vacancies` - удаление
    """
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancies(self, vacancy):
        pass