class TicTacGame():
    def __init__(self):
        self.field_size = 3
        self.display = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        self.players = []
        self.game = False
        self.win_combs = (
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((2, 0), (1, 1), (0, 2))
            )

    def show_board(self, display):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if j != 2:
                    print(display[i][j], end='')
                else:
                    print(display[i][j])

    def start_play(self):
        print("Это игра КРЕСТИКИ-НОЛИКИ!")
        name1 = input("Введите имя первого игрока: \n")
        name2 = input("Введите имя второго игрока: \n")
        print("Первый игрок ходит единицами; Второй - ноликами")
        print("Вводите координаты ячеек куда хотите сходить по примеру: "
              "1 строка 2 столбец - '1 2'")
        self.players = [name1, name2]
        self.game = True

    def validate_input(self, step):
        step = step.strip()
        if len(step) == 3 and step[1] == ' ':
            if step[0].isdigit() and step[2].isdigit():
                if 0 < int(step[0]) < 4 and 0 < int(step[2]) < 4:
                    return True
                else:
                    print("Введены неверные координаты клетки.")
            else:
                print("Некорректный ввод. Вы уверены, что ввели число?")
        else:
            print("Введена неверная строка.")
        return False

    def get_step(self, step):
        step = step.strip()
        coordinates = [int(step[0]) - 1, int(step[2]) - 1]
        return coordinates

    def check_step(self, display, x, y):
        if display[x][y] == "*":
            return True
        return False

    def start_game(self):
        self.start_play()
        player = 0
        while self.game:
            self.show_board(self.display)
            step = input(f"Ходит {self.players[player]}: \n")

            if self.validate_input(step):
                coordinates = self.get_step(step)
                x, y = coordinates[0], coordinates[1]
                if self.check_step(self.display, x, y):
                    if player == 0:
                        self.display[x][y] = 1
                        player = 1
                    elif player == 1:
                        self.display[x][y] = 0
                        player = 0
                else:
                    print("Это клетка уже занята! Выберите другую")

                if self.check_winner(self.display):
                    self.show_board(self.display)
                    print(f"Выиграл {self.players[not player]}!")
                    self.game = False
                elif self.check_draw(self.display):
                    self.show_board(self.display)
                    print("Ничья!")
                    self.game = False

            else:
                print("Попробуйте ещё раз")

        print("Конец Игры")

    def check_winner(self, display):
        for win_comb in self.win_combs:
            last_field = 0
            k = 1
            for field in win_comb:
                current_field = display[field[0]][field[1]]
                if last_field and last_field != current_field or current_field == "*":
                    k = 0
                    break
                last_field = current_field
            if k:
                return True
        return False

    def check_draw(self, display):
        for i in range(self.field_size):
            for j in range(self.field_size):
                if display[i][j] == "*":
                    return False
        return True


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
