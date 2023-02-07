class Stack:
    def __init__(self):
        self.stack = list()

    def __len__(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def show_element(self):
        return self.stack[-1] or None


def show_stack(stack):
    for index in range(len(stack)):
        print(stack.show_element(index), end=' ')
    print()


def input_some(stack):
    some_list = list(map(int, input('Введите числа: ').split()))
    for index, value in enumerate(some_list):
        stack.push(value)


def main():
    stack = Stack()
    input_some(stack)
    show_stack(stack)
    stack.pop()
    show_stack(stack)
    stack.pop()
    show_stack(stack)
    stack.push(5)
    show_stack(stack)
    stack.pop()
    stack.pop()
    stack.pop()
    show_stack(stack)
    stack.show_element(7)


if __name__ == "__main__":
    main()
