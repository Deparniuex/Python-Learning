from dataclasses import dataclass, field


@dataclass
class Vector:
    __vector_list: list = field(default_factory=list)

    def index_appeal(self, index):
        try:
            print("Элемент массива:", self.__vector_list[index])
        except IndexError:
            print("Вне диапазона")

    def __len__(self):
        return len(self.__vector_list)

    def __str__(self):
        return f"Вектор: {self.__vector_list}"

    def display_info(self):
        print(self.__str__())

    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError("Неверный тип данных.")
        for index, value in enumerate(self.__vector_list):
            self.__vector_list[index] *= other
        return self

    def __truediv__(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError("Неверный тип данных.")
        for index, value in enumerate(self.__vector_list):
            self.__vector_list[index] /= other
        return self

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Неверный тип данных.")
        for index, value in enumerate(self.__vector_list):
            self.__vector_list[index] -= other.as_list()[index]
        return self

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Неверный тип данных.")
        for index, value in enumerate(self.__vector_list):
            self.__vector_list[index] += other.as_list()[index]
        return self

    def as_list(self):
        return self.__vector_list


def input_vector():
    while True:
        try:
            vector = Vector([int(i) for i in input("Введите значения элементов вектора: ").split()])
            print(vector)
        except ValueError:
            print("Введены некоректные данные")
            continue
        return vector


def menu():
    vector1 = input_vector()
    while True:
        print("Menu: ")
        print("\t Проверка обращения к элементу с контролем выхода за пределы массива. - 1 ")
        print("\t Поэлементное сложения двух векторов. - 2 ")
        print("\t Поэлементное вычитания двух векторов. - 3 ")
        print("\t Умножение на скаляр. - 4")
        print("\t Деление на скаляр. - 5 ")
        print("\t Завершить программу - 6 ")
        input_inf = int(input("Введите запрос: "))
        if input_inf == 1:
            while True:
                try:
                    vector1.index_appeal(int(input("Введите индекс: ")))
                    break
                except ValueError:
                    print('Неверный тип заданного индекса')
                    continue
        elif input_inf == 2:
            while True:
                vector2 = input_vector()
                if len(vector1) == len(vector2):
                    print("Сложение вектора: ", vector1 + vector2)
                    break
                else:
                    print("Разные длинны векторов")

        elif input_inf == 3:
            while True:
                vector2 = input_vector()
                if len(vector1) == len(vector2):
                    print("Вычитание вектора: ", vector1 - vector2)
                    break
                else:
                    print("Разные длинны векторов")

        elif input_inf == 4:
            while True:
                try:
                    scalar = int(input("Введите скаляр: "))
                    print(vector1 * scalar)
                    break
                except ValueError:
                    print('Неверный тип')
        elif input_inf == 5:
            while True:
                try:
                    scalar = int(input("Введите скаляр: "))
                    print(vector1 / scalar)
                    break
                except ValueError:
                    print('Неверный тип')
        elif input_inf == 6:
            exit(0)
        else:
            print("Неверный запрос")


def main():
    menu()


if __name__ == "__main__":
    main()
