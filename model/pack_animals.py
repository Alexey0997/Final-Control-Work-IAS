"""Модуль, реализующий класс PackAnimals (вьючные животные), наследуемый от класса Animals."""
from model.animals import Animals


class PackAnimals(Animals):
    """Конструктор класса PackAnimals, в котором:
        - id_type      - индивидуальный идентификатор вьючного животного;
        - type_animals - описание идентификатора (типа) животного;
        - kind_animals - вид животного."""
    def __init__(self, kind_animals):
        super().__init__(id_type=2, type_animals="вьючное животное")
        self.kind_animals = kind_animals

    def get_id_type(self):
        """Метод, возвращающий индивидуальный идентификатор вьючного животного (2)."""
        return 2

    def get_type_animals(self):
        """Метод, возвращающий описание идентификатора (типа) животного."""
        return "вьючное животное"

    def get_kind_animals(self):
        """Метод, возвращающий вид вьючного животного (лошадь, осёл или верблюд)."""
        return self.kind_animals

