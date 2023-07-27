"""Модуль реализует класс Console, обеспечивающий взаимодействие с пользователем."""
from datetime import datetime
from view.abstract_view import View
from view.counter import Counter


class Console(View):
    __working = False

    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        self.presenter = presenter

    def start(self):
        """Метод формирует главное меню и запускает алгоритмы работы с базой данных."""
        self.__working = True
        read_db = self.presenter.read_db()
        if read_db == "Ok":
            while self.__working:
                print('\n\tГЛАВНОЕ МЕНЮ:')
                print('\tОткрыть реестр животных          -> нажмите 1\n'
                      '\tДобавить животное в базу данных  -> нажмите 2\n'
                      '\tВывести данные о животном        -> нажмите 3\n'
                      '\tИзменить список команд           -> нажмите 4\n'
                      '\tЗавершить работу с базой данных  -> нажмите 5\n')
                user_choice = self.__get_menu_number(5, '\tВаше решение: ')
                match user_choice:
                    case "1":
                        print("\n                                  Ж У Р Н А Л    У Ч Е Т А    Ж И В О Т Н Ы Х")
                        print(self.presenter.get_tabl_registry())
                    case "2":
                        self.__add_type_animals()
                    case "3":
                        self.__show_animal()
                    case "4":
                        self.__add_command()
                    case "5":
                        self.__working = False
        else:
            print(read_db)

    def __add_type_animals(self):
        """Метод предлагает пользователю выбрать тип животного для добавления в бузу данных"""
        print('\n\tУКАЖИТЕ ТИП ЖИВОТНОГО, КОТОРОЕ ХОТИТЕ ДОБАВИТЬ В БАЗУ ДАННЫХ:')
        print('\tДомашние животные       -> нажмите 1\n'
              '\tВьючные животные        -> нажмите 2\n'
              '\tВозврат в главное меню  -> нажмите 3')
        user_choice = self.__get_menu_number(3, "\n\tВаше решение: ")
        match user_choice:
            case "1":
                self.__add_animal(user_choice, self.presenter.all_kinds_pets())
            case "2":
                self.__add_animal(user_choice, self.presenter.all_kinds_pack())
            case "3":
                return

    def __add_animal(self, type_id, kinds):
        """Метод позволяет добавить экземпляр выбранного вида животных"""
        print(f'\n\tДОСТУПНЫ ДЛЯ ДОБАВЛЕНИЯ СЛЕДУЮЩИЕ ВИДЫ ЖИВОТНЫХ: {kinds}\n')
        kind = input('\tУкажите вид животного, которое хотите добавить в базу данных: ').lower()
        if kind in kinds:
            name = input('\tВведите имя животного: ').capitalize()
            command = input('\tВведите через запятую список команд, которым обучено животное: ')
            birth_date = self.__get_date('\tВведите дату рождения животного (ГГГГ-ММ-ДД): ')
            if self.__save_animal(kind, name, command, birth_date):
                self.presenter.add_animal(kind, name, command, birth_date)
                print(self.presenter.save_animal_into_bd(type_id, kind, name, command, birth_date))
        else:
            print("\n\tДобавление указанного вида животных не предусмотрено.")
            return

    @staticmethod
    def __get_menu_number(size: int, text: str):
        """Метод возвращает номер пункта меню и проверяет корректность ввода данных"""
        while True:
            user_input = input(text)
            if (user_input.isdigit() and
                    1 <= int(user_input) <= size):
                return user_input
            print(f"\n\tВведено некорректное значение. Укажите число от 1 до {size}.")

    @staticmethod
    def __save_animal(kind, name, command, birth_date):
        """Метод выводит пользователю введенные данные для проверки и принятия решения об их сохранении."""
        print(f'\n\tВы ввели следующие данные о животном:\n\t\t- {kind} {name}\n\t\t- обучен командам: {command}'
              f'\n\t\t- дата рождения: {birth_date}')
        user_choice = input('\tСохранить изменения? (д/н): ').lower()
        if user_choice in ['да', 'д', 'y', 'yes']:
            with Counter() as counter:
                if name != '' and command != '' and birth_date != '':
                    counter.add()
                    print(f"\tКоличество добавленных животных: {counter.count}")
                else:
                    raise Exception('\tВведены некорректные значения.')
            return True
        else:
            print('\tДанные не сохранены.\n')
            return False

    @staticmethod
    def __get_date(text):
        """Метод проверяет введенную пользователем дату на соответствие формату "ГГГГ-ММ-ДД"."""
        while True:
            user_input = input(text)
            if user_input:
                try:
                    datetime.strptime(user_input, "%Y-%m-%d")
                    return user_input
                except ValueError:
                    print('\tНекорректный ввод. Укажите дату в формате "ГГГГ-ММ-ДД".')

    def __show_animal(self):
        """Метод выводит сведения о животном по номеру в регистре."""
        print("\n\tВЫВОД ДАННЫХ О ЖИВОТНОМ:")
        user_input = self.__get_menu_number(self.presenter.size_registry(),
                                            "\tВведите регистранционный номер животного: ")
        index = int(user_input) - 1
        print(f"\tВ базе данных имеются следующие сведения о животном с номером {index + 1}:\n\t")
        print(self.presenter.find_animal(index))
        return

    def __add_command(self):
        """Метод реализует добавление новых команд для животного."""
        print("\n\tДОБАВЛЕНИЕ НОВЫХ КОМАНД:")
        user_input = self.__get_menu_number(self.presenter.size_registry(),
                                            "\tВведите регистранционный номер животного: ")
        index = int(user_input) - 1
        print(f'\tЖивотное обучено следующим командам: {self.presenter.get_command(index)}.')
        user_answer = input('\tДобавить команду?(д/н): ')
        if user_answer in ['да', 'д', 'y', 'yes']:
            commands = input('\tВведите через запятую новые команды: ')
            self.presenter.add_command(index, commands)
            print(self.presenter.save_command(index))
        else:
            print('\tОперация отклонена.')
            return
