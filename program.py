"""Модуль реализует класс Program, обеспечивающий запуск всех элементов программы."""
from db_manager.sqlite_manager import SqLiteManager
from model.animals_registry import AnimalsRegistry
from presenter.presenter import Presenter
from view.console import Console


class Program:
    def start(self):
        self.view.start()

    def __init__(self):
        self.registry = AnimalsRegistry()
        self.view = Console()
        self.data = SqLiteManager('human_friends.db')
        Presenter(self.view, self.registry, self.data)

