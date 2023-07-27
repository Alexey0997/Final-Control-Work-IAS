"""Модуль реализует класс AnimalsRegistry, предназначенный для учета животных."""
from tabulate import tabulate
from model.horses import Horses
from model.camels import Camels
from model.donkeys import Donkeys
from model.cats import Cats
from model.dogs import Dogs
from model.hamsters import Hamsters


class AnimalsRegistry:
    """Конструктор класса AnimalsRegistry, который создает новый экземпляр класса и инициализирует
       переменную __log_registry пустым списком."""
    def __init__(self):
        self.__log_registry = []

    def get_log_registry(self):
        """Метод, возвращающий журнал учета."""
        return self.__log_registry

    def number_of_animals(self):
        """Метод, возвращающий количество элементов в журнале учета."""
        return len(self.__log_registry)

    def __add_cat(self, name, command, birth_date, id_animal=None):
        """Метод добавления животного в таблицу "Кошки"."""
        cat = Cats(id_animal, name, command, birth_date)
        self.__log_registry.append(cat)

    def __add_dog(self, name, command, birth_date, id_animal=None):
        """Метод добавления животного в таблицу "Собаки"."""
        dog = Dogs(id_animal, name, command, birth_date)
        self.__log_registry.append(dog)

    def __add_hamster(self, name, command, birth_date, id_animal=None):
        """Метод добавления животного в таблицу "Хомячки"."""
        hamster = Hamsters(id_animal, name, command, birth_date)
        self.__log_registry.append(hamster)

    def __add_horse(self, name, command, birth_date, id_animal=None):
        """Метод добавления животного в таблицу "Лошади"."""
        horse = Horses(id_animal, name, command, birth_date)
        self.__log_registry.append(horse)

    def __add_camel(self, name, command, birth_date, id_animal=None):
        """Метод добавления животного в таблицу "Верблюды"."""
        camel = Camels(id_animal, name, command, birth_date)
        self.__log_registry.append(camel)

    def __add_donkey(self, name, command, birth_date, id_animal=None):
        """Метод добавления животного в таблицу "Ослы"."""
        donkey = Donkeys(id_animal, name, command, birth_date)
        self.__log_registry.append(donkey)

    __function_add_animal = {'кошка': __add_cat, 'собака': __add_dog, 'хомячок': __add_hamster,
                             'лошадь': __add_horse, 'осёл': __add_donkey, 'верблюд': __add_camel}

    def add_animal(self, kind, name, command, birth_date):
        """Метод добавления животного в базу данных."""
        for key, value in self.__function_add_animal.items():
            if key == kind:
                value(self, name, command, birth_date)
                break

    @property
    def tabl_registry(self):
        """Метод выводит данные журнала учета в табличной форме."""
        headers = ['№', 'ТИП ЖИВОТНОГО', 'ВИД ЖИВОТНОГО', 'КЛИЧКА',
                   'ПЕРЕЧЕНЬ ОСВОЕННЫХ КОМАНД', 'ДАТА РОЖДЕНИЯ']
        tabl = [[i, animal.get_type_animals(), animal.get_kind_animals(), animal.get_name(),
                 animal.get_command(), animal.get_birth_date()]
                for i, animal in enumerate(self.__log_registry, start=1)]
        return tabulate(tabl, headers=headers, tablefmt="mixed_grid", stralign='left')

    def list_kind_pets(self):
        """Метод формирования множества домашних животных."""
        kind_pets = set()
        for item in self.__log_registry:
            if item.get_id_type() == 1:
                kind_pets.add(item.get_kind_animals())
        return kind_pets

    def list_kind_pack(self):
        """Метод формирования множества вьючных животных."""
        kind_pack = set()
        for item in self.__log_registry:
            if item.get_id_type() == 2:
                kind_pack.add(item.get_kind_animals())
        return kind_pack

    def find_animal(self, index):
        """Метод поиска животного по индексу."""
        return self.__log_registry[index]

    def get_command(self, index):
        """Метод просмотра списка команд, которым обучено животное."""
        return self.__log_registry[index].get_command()

    def add_command(self, index, commands):
        """Метод добавления новых команд, которым обучено животное."""
        self.__log_registry[index].add_command(commands)
