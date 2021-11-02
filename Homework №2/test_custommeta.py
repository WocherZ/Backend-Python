import unittest
from custommeta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        print("Запустился init CustomClass")
        self.val = val

    def line(self):
        return 100


class TestCustomMeta(unittest.TestCase):
    def setUp(self) -> None:
        self.ex1 = CustomClass()
        self.ex2 = CustomClass(val=89)
        self.ex3 = CustomClass(89)


    def test_get_attr(self):
        self.assertEqual(self.ex1.custom_x, 50)
        self.assertEqual(self.ex2.custom_x, 50)
        self.assertEqual(self.ex3.custom_x, 50)

    def test_get_method(self):
        self.assertEqual(self.ex1.custom_line(), 100)
        self.assertEqual(self.ex2.custom_line(), 100)
        self.assertEqual(self.ex3.custom_line(), 100)

    def test_get_value(self):
        # self.assertEqual(self.ex1.custom_val, 99)  # hasn't attribute
        # self.assertEqual(self.ex2.custom_val, 89)
        # self.assertEqual(self.ex3.custom_val, 89)  # hasn't attribute
        ...


if __name__ == '__main__':
    unittest.main()
