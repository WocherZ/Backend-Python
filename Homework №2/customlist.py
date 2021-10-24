import copy


class CustomList(list):
    def __init__(self, array):
        super().__init__()
        self.data = array.copy()

    def __str__(self):
        return str(self.data)

    def __getitem__(self, item):  # оператор индексирования
        return self.data[item]

    def __len__(self):  # функция len()
        return len(self.data)

    def __setitem__(self, key, value):  # назначение элемента по индексу
        self.data[key] = value

    def __add__(self, other):  # оператор сложения если объект - операнд слева
        print("Вызвался оператор сложения слева")
        other = other.copy()
        result = []
        max_size = max(len(self.data), len(other))

        if len(self.data) < max_size:
            self.extend(max_size)
        elif len(other) < max_size:
            if type(other) == list:
                for i in range(max_size - len(other)):
                    other.append(0)
            else:
                other.extend(max_size)

        for i in range(max_size):
            result.append(self.data[i] + other[i])

        return CustomList(result)

    def __radd__(self, other):  # оператор сложения если объект - операнд справа
        print("Вызвался оператор сложения справа")
        other = other.copy()
        result = []
        max_size = max(len(self.data), len(other))

        if len(self.data) < max_size:
            self.extend(max_size)
        elif len(other) < max_size:
            if type(other) == list:
                for i in range(max_size-len(other)):
                    other.append(0)
            else:
                other.extend(max_size)

        for i in range(max_size):
            result.append(self.data[i] + other[i])

        return CustomList(result)

    def __sub__(self, other):
        print("Вызвался оператор вычитания слева")
        other = other.copy()
        result = []
        max_size = max(len(self.data), len(other))

        if len(self.data) < max_size:
            self.extend(max_size)
        elif len(other) < max_size:
            if type(other) == list:
                for i in range(max_size - len(other)):
                    other.append(0)
            else:
                other.extend(max_size)

        for i in range(max_size):
            result.append(self.data[i] - other[i])

        return CustomList(result)

    def __rsub__(self, other):
        print("Вызвался оператор вычитания справа")
        other = other.copy()
        result = []
        max_size = max(len(self.data), len(other))

        if len(self.data) < max_size:
            self.extend(max_size)
        elif len(other) < max_size:
            if type(other) == list:
                for i in range(max_size - len(other)):
                    other.append(0)
            else:
                other.extend(max_size)

        for i in range(max_size):
            result.append(other[i] - self.data[i])

        return CustomList(result)

    def extend(self, size):  # дополнение нулями  листа
        if len(self.data) < size:
            for i in range(size - len(self.data)):
                self.data.append(0)
        print("CustomList после добавления: ", self.data)

    def __del__(self):
        del self.data




ar = [1, 2, 3]
example = CustomList(ar)
ar.append(7)
example1 = CustomList(ar)
print("Первый список: ", example)  # [1, 2, 3]
print("Второй список: ", example1)  # [1, 2, 3, 7]

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

print("Первый список: ", example)  # [1, 2, 3]
print("Второй список: ", example1)  # [1, 2, 3, 7]