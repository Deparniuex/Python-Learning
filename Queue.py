class Queue:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return f'Очередь:{self.list}'

    def add(self, new):
        self.list.append(new)

    def delete(self):
        self.list.pop(0)

    def out(self, el):
        self.list.pop(el)

    def swap(self, a, b):
        self.list[a], self.list[b] = self.list[b], self.list[a]


def inp():
    while True:
        try:
            return int(input())
        except ValueError:
            print("Введенное значение неккоректно")


def inp_menu(n):
    while True:
        try:
            ch = int(input())
            if ((ch > n) or (ch <= 0)):
                print("Данного действия нет")
                continue
            return ch
        except ValueError:
            print("Введенное значение неккоректно")


def menu():
    print("Создание очереди\nВведите значения в очередь: ")
    list = Queue(input().split())
    while True:
        print(
            "-------------------------\n\tВыбор действия:\n[1]Добавление в очередь\n[2]Удаление из очереди\n[3]Удаление элемнта из очереди по индексу\n[4]Показать значения элементов в очереди\n[5]Поменять два элемена местами\n[6]Выход\n-------------------------")
        ch = inp_menu(6)
        if ch == 6:
            return None
        elif ch == 1:
            print("Введите желаемое значение")
            list.add(input())
        elif ch == 2:
            while True:
                try:
                    list.delete()
                    print("Первый элемент очереди удалён")
                    break
                except IndexError:
                    print("Очередь пуста")
        elif ch == 3:
            print("Введите индекс элемента, который удаляется")
            while True:
                try:
                    list.out(inp())
                    print("Элемент очереди удалён")
                    break
                except IndexError:
                    if len(list.list) == 0:
                        print("Очередь пуста")
                        break
                    else:
                        print("Указанного индекса нет")
        elif ch == 4:
            print(list)
        elif ch == 5:
            print("Введите два индекса, которые поменять местами")
            while True:
                try:
                    list.swap(inp(), inp())
                    break
                except IndexError:
                    print("Заданные индексы введены некорректно")


def main():
    menu()
    print("Работа программы завершена.")
    input()


if __name__ == "__main__":
    main()
