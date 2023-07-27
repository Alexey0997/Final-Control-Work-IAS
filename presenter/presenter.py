"""Модуль реализует класс Presenter."""
from db_manager.sqlite_manager import SqLiteManager
from model import AnimalsRegistry
from view.abstract_view import View


class Presenter:
    """Конструктор класса Presenter."""
    def __init__(self, view: View, log_registry: AnimalsRegistry, data: SqLiteManager):
        self.view = view
        self.log_registry = log_registry
        self.view.set_presenter(self)
        self.data = data

    def read_db(self):
        """Метод подключения к базе данных."""
        return self.data.read_db(self.log_registry)

    def get_tabl_registry(self):
        """Метод вывода журнала регистрации животных."""
        return self.log_registry.tabl_registry

    def all_kinds_pets(self):
        """Метод вывода данных о доступных видах домашних животных."""
        return self.log_registry.list_kind_pets()

    def all_kinds_pack(self):
        """Метод вывода данных о доступных видах вьючных животных."""
        return self.log_registry.list_kind_pack()

    def add_animal(self, kind, name, command, birth_date):
        """Метод вывода данных о животном."""
        self.log_registry.add_animal(kind, name, command, birth_date)

    def save_animal_into_bd(self, type_id, kind, name, command, birth_date):
        """Метод сохранения изменений в базе данных."""
        return self.data.save_animal(type_id, kind, name, command, birth_date)

    def find_animal(self, index):
        """Метод вывода данных о животном по индексу."""
        return self.log_registry.find_animal(index)

    def get_command(self, index):
        """Метод вывода данных о командах, освоенных животным."""
        return self.log_registry.get_command(index)

    def add_command(self, index, commands):
        """Метод добавления новых команд."""
        self.log_registry.add_command(index, commands)

    def size_registry(self):
        """Метод определения количества элементов в регистре."""
        return self.log_registry.number_of_animals()

    def save_command(self, index):
        """Метод сохранения изменений в перечне команд, освоенных животным."""
        return self.data.save_command(index, self.log_registry)