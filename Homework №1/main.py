class TicTacGame():
    def __init__(self):
        self.display = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        self.players = []


    def show_board(self, display):
        for i in range(3):
            for j in range(3):
                if j != 2:
                    print(display[i][j], end='')
                else:
                    print(display[i][j])


    def start_play(self):
        print("Это игра КРЕСТИКИ-НОЛИКИ!")
        print("Введите имя первого игрока:")
        name1 = input()
        print("Введите имя второго игрока:")
        name2 = input()
        print("Первый игрок ходит единицами; Второй - ноликами")
        print("Вводите координаты ячеек куда хотите сходить по примеру: 1 строка 2 столбец - '1 2'")
        self.players = [name1, name2]


    def validate_input(self, step):
        step = step.replace(' ', '')
        if len(step) == 2 and step.isdigit():
            if 0 < int(step[0]) < 4 and 0 < int(step[1]) < 4:
                return True
            else:
                return False
        else:
            return False


    def get_step(self, step):
        coordinates = [int(step[0]) - 1, int(step[2]) - 1]
        return coordinates


    def check_step(self, display, x, y):
        if display[x][y] == "*":
            return True
        return False


    def start_game(self):
        Game = True
        self.start_play()
        player = 0
        while Game:
            self.show_board(self.display)
            if player == 0:
                print("Ходит первый игрок:")
            if player == 1:
                print("Ходит второй игрок:")

            step = input()
            if self.validate_input(step):
                coordinates = self.get_step(step)
                x = coordinates[0]
                y = coordinates[1]
                if self.check_step(self.display, x, y):
                    if player == 0:
                        self.display[x][y] = 1
                        player = 1
                    elif player == 1:
                        self.display[x][y] = 0
                        player = 0
                else:
                    print("Это поле уже занято! Выберите другое")

                if self.check_winner(self.display):
                    self.show_board(self.display)
                    self.print_win(player)
                    Game = False
                elif self.check_draw(self.display):
                    self.show_board(self.display)
                    print("Ничья!")
                    Game = False

            else:
                print("Некорректный ввод! Попробуйте ещё раз")

        print("Конец Игры")


    def check_winner(self, display):
        for i in range(3):
            if display[i][0] == display[i][1] == display[i][2] != "*":
                return True
            if display[0][i] == display[1][i] == display[2][i] != "*":
                return True

        if display[1][1] == display[0][0] == display[2][2] != "*":
            return True
        if display[1][1] == display[2][0] == display[0][2] != "*":
            return True

        return False


    def check_draw(self, display):
        for i in range(3):
            for j in range(3):
                if display[i][j] == "*":
                    return False
        return True


    def print_win(self, player):
        if player == 0:
            print(f"Выиграл {self.players[1]}!")
        else:
            print(f"Выиграл {self.players[0]}!")


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
