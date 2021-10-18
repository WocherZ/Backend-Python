import unittest
from main import TicTacGame


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        # Экземпляр игры
        self.game = TicTacGame()
        # Стартовое поле
        self.display_one = [["*", "*", "*"],
                            ["*", "*", "*"],
                            ["*", "*", "*"]]
        # Возможная вариация поле во время игры(без победы)
        self.display_two = [["1", "0", "1"],
                            ["*", "0", "*"],
                            ["0", "*", "1"]]
        # Возможная вариация поле во время игры(с победой одного из игроков)
        self.display_three = [["1", "*", "0"],
                              ["*", "1", "0"],
                              ["*", "0", "1"]]
        # Возможная вариация поле во время игры(с ничьёй)
        self.display_four = [["1", "1", "0"],
                             ["0", "0", "1"],
                             ["1", "0", "1"]]

    def test_valid_input(self):
        # Проверка корректного ввода
        self.assertTrue(self.game.validate_input('1 2'))
        self.assertTrue(self.game.validate_input('2 1'))
        self.assertTrue(self.game.validate_input(' 2   1  '))
        self.assertTrue(self.game.validate_input('1   3  '))

    def test_invalid_input(self):
        # Проверка некорректного ввода
        self.assertFalse(self.game.validate_input('1 4'))
        self.assertFalse(self.game.validate_input('4 3'))
        self.assertFalse(self.game.validate_input('1 2 \n'))
        self.assertFalse(self.game.validate_input('1 2 \t'))

    def test_get_step(self):
        # Проверка получения правильных координат
        self.assertEqual(self.game.get_step('1 1'), [0, 0])
        self.assertEqual(self.game.get_step('1 2'), [0, 1])
        self.assertEqual(self.game.get_step('3 2'), [2, 1])

    def test_check_step(self):
        # Проверка тестов на первом поле(display_one)
        self.assertTrue(self.game.check_step(self.display_one, 1, 1))
        self.assertTrue(self.game.check_step(self.display_one, 1, 2))

        # Проверка тестов на втором поле(display_two)
        self.assertFalse(self.game.check_step(self.display_two, 1, 1))
        self.assertFalse(self.game.check_step(self.display_two, 0, 0))
        self.assertTrue(self.game.check_step(self.display_two, 1, 0))

    def test_check_winner(self):
        # Проверка тестов проверки победителя
        # 1,2 поле - нет победы; 3 поле - победа
        self.assertFalse(self.game.check_winner(self.display_one))
        self.assertFalse(self.game.check_winner(self.display_two))
        self.assertTrue(self.game.check_winner(self.display_three))

    def test_check_draw(self):
        # Проверка тестов проверки на ничью(1,2,3 - нет ничьи; 4 поле - ничья)
        self.assertFalse(self.game.check_draw(self.display_one))
        self.assertFalse(self.game.check_draw(self.display_two))
        self.assertFalse(self.game.check_draw(self.display_three))
        self.assertTrue(self.game.check_draw(self.display_four))

    def tearDown(self) -> None:
        print("Test done!")


if __name__ == '__main__':
    unittest.main()
