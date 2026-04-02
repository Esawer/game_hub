import random
from copy import deepcopy
import re


class Player:
    def __init__(self, name: str):
        self.name = name

    def move(self, size):
        return [int(input(f"position x; 0 - {size - 1}: ")), int(input(f"position y; 0 - {size - 1}: "))]


class Board:
    def __init__(self, size: int, board_state):
        self.size = size
        self.board_state = board_state

    def board_draw(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board_state[i][j], end=" ")
            print("\n")

    def check(self, p_pos, player1_turn: bool):
        player_number = 1 if player1_turn else 2

        if self.board_state[int(p_pos[0])][int(p_pos[1])] == 0:
            self.board_state[int(p_pos[0])][int(p_pos[1])] = player_number
        else:
            return False

        b = deepcopy(self.board_state)
        c = []
        d = []
        row = int(p_pos[0])
        col = int(p_pos[1])

        for i in range(self.size):
            for j in range(self.size):
                b[i][j] = self.board_state[j][i]

        while True:
            row_checker = row
            col_checker = col

            while True:
                if row_checker > 0 and col_checker > 0:
                    row_checker -= 1
                    col_checker -= 1
                else:
                    while True:
                        c.append(self.board_state[row_checker][col_checker])
                        if row_checker < self.size - 1 and col_checker < self.size - 1:
                            row_checker += 1
                            col_checker += 1
                        else:
                            break
                    row_checker = row
                    col_checker = col
                    break

            while True:
                if row_checker > 0 and col_checker < self.size - 1:
                    row_checker -= 1
                    col_checker += 1
                else:
                    while True:
                        d.append(self.board_state[row_checker][col_checker])
                        if row_checker < self.size - 1 and col_checker > 0:
                            row_checker += 1
                            col_checker -= 1
                        else:
                            break

                    break
            break

        for i in [[a for a in self.board_state[row]], [a for a in b[col]], c, d]:
            if re.search(rf"({player_number}){{3,}}", "".join(map(lambda x: str(x), i))):
                print(f"Player {'1' if player1_turn else '2'} has won!")
                return 'win'

        for i in [[a for a in self.board_state[row]], [a for a in b[col]], c, d]:
            if '0' in "".join(map(lambda x: str(x), i)):
                break
        else:
            return 'tie'

        return True


class Game:
    def __init__(self, classic_mode: bool = True):
        self.classic_mode = classic_mode

    def game_run(self):
        game_on = True
        b_size = 3

        player_1_turn = bool(random.randint(0, 1))
        player_1 = Player("a")
        player_2 = Player("b")
        player_list = [player_2, player_1]

        if not self.classic_mode:
            while True:
                try:
                    b_size = int(input("board size (3-8): "))

                    if 3 <= b_size <= 8:
                        break
                    else:
                        print("other size.")

                except Exception as e:
                    print(f"error - {e}")

        board = Board(b_size, [[0 for _ in range(b_size)] for _ in range(b_size)])
        board.board_draw()

        while game_on:
            p_pos = player_1.move(b_size) if player_1_turn else player_2.move(b_size)

            game_state = board.check(p_pos, player_1_turn)

            if game_state in ['tie', 'win']:
                game_on = False

            if game_state:
                board.board_draw()
                player_1_turn = not player_1_turn


game = Game(True)
game.game_run()
