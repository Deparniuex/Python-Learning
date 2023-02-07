# лаб4 - 13

class SymbString(object):
    _string: str
    _name: str

    def get_name(self):
        return self._name

    def __init__(self, string: str, name: str):
        self._string = string
        self._name = name

    def __str__(self):
        return f"Символьная строка \"{self._name}\": {self._string}"

    def __add__(self, other):
        if not isinstance(other, SymbString):
            raise TypeError("Неверный тип данных")
        return SymbString(self._string + other._string, self._name)


class DecString(SymbString):
    def __init__(self, number: str, name):
        super().__init__(str(number), name)

    def __str__(self):
        return f"Десятичная строка \"{self._name}\": {self._string}"

    def __add__(self, other):
        if isinstance(other, DecString):
            return DecString(str(int(self._string) + int(other._string)), self._name)
        elif isinstance(other, SymbString):
            return SymbString(self._string + other._string, self._name)
        else:
            raise TypeError("Неверный тип данных")


class Factory(object):
    @staticmethod
    def create_string(string: str, name: str):
        nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        final_string = string.strip()
        for i in range(len(final_string)):
            if not nums.__contains__(final_string[i]): # a in b where b = [1, ...]
                return SymbString(string, name)
        return DecString(string, name)

def sum(list_of_objects, name_index, name_index2):
    list_of_objects[name_index] = list_of_objects[name_index] + list_of_objects[name_index2]


def summary_elements(list_of_objects: list, name: str, name2: str):
    flag = 0
    if len(list_of_objects) == 0:
        print("Нет объектов")
        return
    name_index = 0
    name_index2 = 0
    for i, val in enumerate(list_of_objects):
        if val.get_name() == name and flag == 0:
            name_index = i
            flag = 1
        if val.get_name() == name2 and flag == 1:
            name_index2 = i
            flag = 2
    if flag == 2:
        sum(list_of_objects, name_index, name_index2)
        return True
    else:
        return False


def show_elements(list_of_objects):
    if len(list_of_objects) == 0:
        print("Пусто")
        return
    for i, val in enumerate(list_of_objects):
        print(val, end='')
        if i == len(list_of_objects) - 1:
            print()
        else:
            print(", ", end='')


def delete_element(list_of_objects: list, name: str):
    for i, val in enumerate(list_of_objects):
        if val.get_name() == name:
            list_of_objects.pop(i)
            return True
    return False


def menu():
    list_of_objects = []
    while True:
        print("Menu: ")
        print("\t 1. Add object")
        print("\t 2. Delete object")
        print("\t 3. Work with object")
        print("\t 4. Show objects")
        print("\t 5. Exit")
        input_inf = int(input("Введите запрос: "))
        if input_inf == 1:
            list_of_objects.append(Factory.create_string(input('Введите строку: '), input('Введите идентификатор: ')))
        elif input_inf == 2:
            name_ind = input('Введите имя удаляемого объекта: ')
            if delete_element(list_of_objects, name_ind):
                print('Объект удален')
            else:
                print('Объект не удален')
        elif input_inf == 3:
            name_ind = input('Введите имя первого объекта: ')
            name_ind2 = input('Введите имя второго объекта: ')

            if summary_elements(list_of_objects, name_ind, name_ind2):
                print('Сложение выполнено')
            else:
                print('Сложение не выполнено')

        elif input_inf == 4:
            show_elements(list_of_objects)
        elif input_inf == 5:
            exit(0)
        else:
            print("Неверный запрос")


def main():
    menu()


if __name__ == "__main__":
    main()
