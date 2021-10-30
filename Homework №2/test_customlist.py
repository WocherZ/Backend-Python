import unittest
from .customlist import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self) -> None:
        self.array1 = CustomList([1, 2, 3])
        self.array2 = CustomList([3, 2, 1, 3, 4])
        self.list1 = [1, 2, 3]
        self.list2 = [3, 2, 1, 3, 4]
        self.res_add = CustomList([4, 4, 4, 3, 4])
        self.res_sub = CustomList([-2, 0, 2, -3, -4])
        self.res_extend = CustomList([1, 2, 3, 0, 0])
        self.res_sum1 = 6
        self.res_sum2 = 13

    def test_add(self):
        self.assertEqual(self.array1 + self.list2, self.res_add)
        self.assertEqual(self.list2 + self.array1, self.res_add)
        self.assertEqual(self.array2 + self.list1, self.res_add)
        self.assertEqual(self.list1 + self.array2, self.res_add)
        self.assertEqual(self.array1 + self.array2, self.res_add)

    def test_sub(self):
        self.assertEqual(self.array1 - self.list2, self.res_sub)
        self.assertEqual(self.list2 - self.array1, self.res_sub)
        self.assertEqual(self.array1 - self.array2, self.res_sub)

    def test_iadd(self):
        self.array1 += self.list2
        self.assertEqual(self.array1, self.res_add)

    def test_isub(self):
        self.array1 -= self.list2
        self.assertEqual(self.array1, self.res_sub)

    def test_comparison(self):
        self.assertTrue(self.array2 > self.array1)
        self.assertFalse(self.array2 < self.array1)
        self.assertTrue(self.array2 >= self.array1)
        self.assertFalse(self.array2 <= self.array1)

        self.assertTrue(self.array2 > self.list1)
        self.assertFalse(self.array2 < self.list1)
        self.assertTrue(self.array2 >= self.list1)
        self.assertFalse(self.array2 <= self.list1)

        self.assertTrue(self.list2 > self.array1)
        self.assertFalse(self.list2 < self.array1)
        self.assertTrue(self.list2 >= self.array1)
        self.assertFalse(self.list2 <= self.array1)

    def test_extend(self):
        self.array1.extend(5)
        self.assertEqual(self.array1, self.res_extend)

    def test_sum_elements(self):
        self.assertEqual(self.array1.sum(), self.res_sum1)
        self.assertEqual(self.array2.sum(), self.res_sum2)


if __name__ == '__main__':
    unittest.main()
