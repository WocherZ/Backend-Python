def print_attrs(cls):
    for attr in dir(cls):
        if not attr.startswith('_'):  # Если не внутренний и не служебный
            print(attr, getattr(cls, attr))


class CustomMeta:
    def __new__(cls, *args, **kwargs):
        print("Запустился new ClassMeta")
        new_class = type(args[0], args[1], args[2])
        if new_class:
            # print("Класс ", new_class)
            # print("Атрибуты в начале: ", new_class.__dict__)
            # print("Арги ", args)
            # print("Кварги ", kwargs)

            if args:
                if len(args) == 3:
                    for key, value in args[2].items():
                        if not (key[0:2] == '__' and key[-1: -3: -1] == '__'):
                            new_key = "custom_" + str(key)
                            setattr(new_class, new_key, value)
                            delattr(new_class, key)

            if kwargs:
                for key, value in kwargs.items():
                    new_key = "custom_" + str(key)
                    setattr(new_class, new_key, value)  # устанавливает значение value атрибута new_key
                    delattr(new_class, key)


            print("Атрибуты в конце: ", new_class.__dict__)
            print()
        return new_class

    def __init__(self):
        print("init CustomMeta")

    # call magic or init


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        print("Запустился init CustomClass")
        self.val = val

    def line(self):
        return 100


if __name__ == '__main__':

    #ex = CustomClass(val=89)

    #ex = CustomClass(89)
    #print(ex.__dict__)
    ex = CustomClass()

    print("Печать атрибутов: ")
    print_attrs(ex)
    print("Создался класс")

    # print(ex.custom_x)
    # print(ex.custom_line())
    # print(ex.custom_val)


    # print(ex.x)  # error
    # print(ex.val)  # error