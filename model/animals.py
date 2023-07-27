"""Модуль, реализующий родительский класс Animals."""
from abc import ABC, abstractmethod


class Animals(ABC):
    """Конструктор класса Animals, в котором:
        - id_type      - индивидуальный идентификатор типа животного;
        - type_animals - описание типа животного."""
    def __init__(self, id_type, type_animals):
        self.__id_type = id_type
        self.__type_animals = type_animals

    @abstractmethod
    def get_id_type(self):
        """Абстрактный метод, возвращающий индивидуальный идентификатор типа животного (1 или 2)."""

    @abstractmethod
    def get_type_animals(self):
        """Абстрактный метод, возвращающий описание типа животного (доммшнее или вьючное)."""
