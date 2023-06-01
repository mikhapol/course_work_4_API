from abc import ABC, abstractmethod
import json
import os


class Saver(ABC):
    """
    Абстрактный метод для добавления информации в загрузочный JSON
    """
    @abstractmethod
    def insert(self, data):
        pass


class FileManagerMixin:
    @staticmethod
    def _connect(filename) -> None:

        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(json.dumps([]))

    @staticmethod
    def _open_file(filename) -> list:

        with open(filename, 'r', encoding="utf-8") as file:
            return json.load(file)


class JSONSaver(Saver, FileManagerMixin):
    """
    Класс для работы с загрузочным файлом json.
    """

    def __init__(self, file_path) -> None:
        self.data_file = file_path

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self._connect(self.__data_file)

    def insert(self, data) -> None:
        """Добавление и сохранение в загрузочный файл JSON"""
        file_data = self._open_file(self.__data_file)
        file_data.append(data)
        self.save(file_data)

    def clear_data(self) -> None:
        """Метод очищения файла JSON."""
        with open(self.__data_file, "w") as file:
            file.write(json.dumps([]))

    def save(self, result: list) -> None:
        """Метод для реализации сохранения данных в JSON в читаемый вид"""
        with open(self.__data_file, 'w', encoding="utf-8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
