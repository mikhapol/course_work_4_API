from src.entity.classes.abstract import AbstractVacancyAPI
import requests
import os

SJ_API_KEY = os.getenv('SJ_API_KEY')


class SuperJobAPI(AbstractVacancyAPI):
    """
    Класс для взаимодействия с API SuperJob
    """

    def __init__(self, keyword, page=1):
        self.url = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {
            "keywords": keyword,
            "page": page
        }

    def get_request(self):
        header = {'X-Api-App-Id': SJ_API_KEY}
        return requests.get(self.url, headers=header, params=self.params)

