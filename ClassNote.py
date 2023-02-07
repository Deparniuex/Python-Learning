# 7var -> next
class Note:
    _subname: str
    _name: str
    _phone_number: str
    _date_birth: list

    def get_birth(self):
        return self._date_birth

    def __init__(self, subname, name, phone_number, date_birth):
        self._subname = subname
        self._name = name
        self._phone_number = phone_number
        self._date_birth = date_birth

    def __str__(self):
        return f"\nФамилия: {self._subname}, Имя: {self._name}, Номер телефона: {self._phone_number}, Дата рождения: {self._date_birth}"


def is_correct_birth():
    while True:
        date_birth = input('Введите дату рождения(dd.mm.yy): ')
        if date_birth:
            if date_birth.count('.') == 2:
                date_array = date_birth.split('.')
                try:
                    date_array = [int(i) for i in date_array]
                    return date_array
                except ValueError:
                    print('Некорректные данные')
            else:
                print('Некорректный формат даты.')
        else:
            date_birth = 'Не указано'
            return date_birth


def is_correct_name(name: str, state: str):
    while True:
        if name.strip():
            if name.isnumeric():
                print("Имя не должно содержать цифр.")
                name = input(f'Введите {state}: ')
            else:
                return name
        else:
            name = 'Не указано'
            return name


def is_correct_number(phone_number: str):
    while True:
        if phone_number.strip():
            if phone_number.isnumeric():
                return phone_number
            else:
                print('Номер телефона содержит некорректные символы.')
                phone_number = input('Введите номер телефона: ')
        else:
            phone_number = 'Не указано'
            return phone_number


def show_list_of_objects(list_of_objects: list):
    if list_of_objects:
        for index, value in enumerate(list_of_objects):
            print(value)
    else:
        print('Список пуст')


def show_date_birth(list_of_objects: list, date_birth: list):
    flag = 0
    for index, value in enumerate(list_of_objects):
        if value.get_birth() == date_birth:
            print(list_of_objects[index])
            flag = 1
    if flag != 1:
        print('Одинаковых данных нет.')


def input_notes(list_of_objects: list):
    subname = is_correct_name(input('Введите фамилию: '), 'фамилию')
    name = is_correct_name(input('Введите имя: '), 'имя')
    phone_number = is_correct_number(input('Введите номер телефона(Должно содержать только цифры): '))
    date_birth = is_correct_birth()
    return Note(subname, name, phone_number, date_birth)


def menu():
    list_of_objects = []
    while True:
        print('Меню')
        print('\t Для ввода данных нажмите: 1')
        print('\t Для вывода данных нажмите: 2')
        print('\t Для вывода данных с заданным днем рождения нажмите: 3')
        print('\t Завершение программы: 4')
        inf_input = input('Введите запрос: ')
        if (inf_input == '1'):
            list_of_objects.append(input_notes(list_of_objects))
        elif (inf_input == '2'):
            show_list_of_objects(list_of_objects)
        elif (inf_input == '3'):
            show_date_birth(list_of_objects, is_correct_birth())
        elif (inf_input == '4'):
            exit(0)
        else:
            print('Некорректный запрос')


def main():
    menu()


if __name__ == "__main__":
    main()
