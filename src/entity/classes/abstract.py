from abc import ABC, abstractmethod
from src.entity.classes.json_saver import JSONSaver


class AbstractVacancyAPI(ABC):
    """AbstractVacancyAPI - абстрактный базовый класс для API, который определяет метод """

    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_json_saver(file_name):
        return JSONSaver(file_name)

