"""Модуль, реализующий класс Dogs (собаки), наследуемый от класса Pets."""
from model.pets import Pets


class Dogs(Pets):
    """Конструктор класса Donkeys, в котором:
        - name       - имя животного;
        - command    - команды, которым обучено животное;
        - birth_date - дата рождения;
        - id_animal  - вид животного."""
    def __init__(self, id_animal, name, command, birth_date):
        super().__init__(kind_animals="собака")
        self.__name = name
        self.__command = command
        self.__birth_date = birth_date
        self.__id_animal = id_animal

    def get_id_animal(self):
        """Метод, возвращающий вид животного."""
        return self.__id_animal

    def get_command(self):
        """Метод, возвращающий команды, которым обучено животное."""
        return self.__command

    def add_command(self, new_commands):
        """Метод, добавляющий команды, которым обучено животное."""
        if self.__command == '' or self.__command == 'не обучено':
            self.__command = new_commands
        else:
            self.__command = self.__command + ', ' + new_commands

    def get_name(self):
        """Метод, возвращающий имя животного."""
        return self.__name

    def get_birth_date(self):
        """Метод, возвращающий дату рождения животного."""
        return self.__birth_date

    def __str__(self):
        """Метод, определяющий порядок вывода данных о животном."""
        return f'{self.get_kind_animals()} {self.__name}\nкоманды: {self.__command}\n' \
               f'{self.__birth_date}'

