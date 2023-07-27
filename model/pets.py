"""Модуль, реализующий класс Pets (домашние животные), наследуемый от класса Animals."""
from model.animals import Animals


class Pets(Animals):
    """Конструктор класса Pets, в котором:
        - id_type      - индивидуальный идентификатор вьючного животного;
        - type_animals - описание идентификатора (типа) животного;
        - kind_animals - вид животного."""
    def __init__(self, kind_animals):
        super().__init__(id_type=1, type_animals="домашнее животное")
        self.__kind_animals = kind_animals

    def get_id_type(self):
        """Метод, возвращающий индивидуальный идентификатор домашнего животного (1)."""
        return 1

    def get_type_animals(self):
        """Метод, возвращающий описание типа животного."""
        return "домашнее животное"

    def get_kind_animals(self):
        """Метод, возвращающий вид домашнего животного (кошка, собака или хомячок)."""
        return self.__kind_animals

