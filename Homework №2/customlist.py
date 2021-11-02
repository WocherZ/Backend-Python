class CustomList(list):
    def __init__(self, array):
        super().__init__()
        self.data = array.copy()

    def __str__(self):  # строковое представление
        return str(self.data)

    def __getitem__(self, item):  # оператор индексирования
        return self.data[item]

    def __len__(self):  # функция len()
        return len(self.data)

    def __setitem__(self, key, value):  # назначение элемента по индексу
        self.data[key] = value

    def __add__(self, other):  # оператор сложения если объект - операнд слева
        result = []
        first = CustomList(self.data)
        if type(other) == list:
            second = CustomList(other)
        else:
            second = CustomList(other.data)
        # first и second - два кастомных листа на основе операндов
        max_size = max(len(first), len(second))

        if len(first) < max_size:
            first.extend(max_size)
        elif len(second) < max_size:
            second.extend(max_size)

        for i in range(max_size):
            result.append(first[i] + second[i])

        return CustomList(result)

    def __radd__(self, other):  # оператор сложения если объект - операнд справа
        result = []
        first = CustomList(self.data)
        if type(other) == list:
            second = CustomList(other)
        else:
            second = CustomList(other.data)
        # first и second - два кастомных листа на основе операндов
        max_size = max(len(first), len(second))

        if len(first) < max_size:
            first.extend(max_size)
        elif len(second) < max_size:
            second.extend(max_size)

        for i in range(max_size):
            result.append(first[i] + second[i])

        return CustomList(result)

    def __sub__(self, other):  # оператор вычитания если объект - операнд слева
        result = []
        first = CustomList(self.data)
        if type(other) == list:
            second = CustomList(other)
        else:
            second = CustomList(other.data)
        # first и second - два кастомных листа на основе операндов
        max_size = max(len(first), len(second))

        if len(first) < max_size:
            first.extend(max_size)
        elif len(second) < max_size:
            second.extend(max_size)

        for i in range(max_size):
            result.append(first[i] - second[i])

        return CustomList(result)

    def __rsub__(self, other):  # оператор вычитания если объект - операнд справа
        result = []
        first = CustomList(self.data)
        if type(other) == list:
            second = CustomList(other)
        else:
            second = CustomList(other.data)
        # first и second - два кастомных листа на основе операндов
        max_size = max(len(first), len(second))

        if len(first) < max_size:
            first.extend(max_size)
        elif len(second) < max_size:
            second.extend(max_size)

        for i in range(max_size):
            result.append(second[i] - first[i])

        return CustomList(result)

    def __iadd__(self, other):  # оператор +=
        result = []
        first = CustomList(self.data)
        if type(other) == list:
            second = CustomList(other)
        else:
            second = CustomList(other.data)
        # first и second - два кастомных листа на основе операндов
        max_size = max(len(first), len(second))

        if len(first) < max_size:
            first.extend(max_size)
        elif len(second) < max_size:
            second.extend(max_size)

        for i in range(max_size):
            result.append(first[i] + second[i])

        return CustomList(result)

    def __isub__(self, other):  # оператор -=
        result = []
        first = CustomList(self.data)
        if type(other) == list:
            second = CustomList(other)
        else:
            second = CustomList(other.data)
        # first и second - два кастомных листа на основе операндов
        max_size = max(len(first), len(second))

        if len(first) < max_size:
            first.extend(max_size)
        elif len(second) < max_size:
            second.extend(max_size)

        for i in range(max_size):
            result.append(first[i] - second[i])

        return CustomList(result)

    def __lt__(self, other):  # оператор <
        if type(other) == list:
            second = CustomList(other)
        else:
            second = other

        if self.sum() < second.sum():
            return True
        else:
            return False

    def __gt__(self, other):  # оператор >
        if type(other) == list:
            second = CustomList(other)
        else:
            second = other

        if self.sum() > second.sum():
            return True
        else:
            return False

    def __le__(self, other):  # оператор <=
        if type(other) == list:
            second = CustomList(other)
        else:
            second = other

        if self.sum() <= second.sum():
            return True
        else:
            return False

    def __ge__(self, other):  # оператор >=
        if type(other) == list:
            second = CustomList(other)
        else:
            second = other

        if self.sum() >= second.sum():
            return True
        else:
            return False

    def sum(self):  # сумма элементов
        result = 0
        for i in range(len(self.data)):
            result += self.data[i]
        return result

    def extend(self, size):  # дополнение нулями  листа
        if len(self.data) < size:
            for i in range(size - len(self.data)):
                self.data.append(0)

    def __del__(self):  # удаление
        del self.data



if __name__ == '__main__':

    ar = [1, 2, 3]
    example = CustomList(ar)
    print(example.extend(5))
    print()
    ar = [1, 2, 3]
    example1 = CustomList(ar)
    print("Первый список: ", example)
    print("Второй список: ", example1)
    print("Сложение первого со вторым: ", end="")
    res = example + example1
    print(res)

    print("Сложение второго с первым: ", end="")
    res = example + example1
    print(res)

    print("Вычитание из второго первого: ", end="")
    res = example - example1
    print(res)

    print("Вычитание из первого второго: ", end="")
    res = example1 - example
    print(res)

    print("Первый список: ", example)
    print("Второй список: ", example1)