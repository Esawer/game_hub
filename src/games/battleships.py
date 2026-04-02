import random


class Player:
    def __init__(self, player_name: str, player_ships=None):
        self.player_ships = []
        self.player_name = player_name

    def move(self):
        print(f'{self.player_name} - choose your target: ')
        while True:
            try:

                p_x = int(input('x: '))
                p_y = int(input('y: '))

                if 10 > p_x >= 0 and 10 > p_y >= 0:
                    return [p_x, p_y]

            except Exception as e:
                print(f'error - {e}')

    def add_ship(self, ship):
        self.player_ships.append(ship)

    def remove_ship(self, ship):
        self.player_ships.remove(ship)

    def lose_condition(self):
        return len(self.player_ships) == 0


class Board:
    def __init__(self, board_size: int, board_state):
        self.board_size = board_size
        self.board_state = board_state

    def check(self, p_move, is_vertical: bool, ship_size: int):
        if is_vertical:
            if p_move[1] + ship_size > self.board_size: return False

            for i in range(p_move[1], p_move[1] + ship_size):
                if self.board_state[i][p_move[0]] != '0': return False

        else:
            if p_move[0] + ship_size > self.board_size: return False

            for i in range(p_move[0], p_move[0] + ship_size):
                if self.board_state[p_move[1]][i] != '0': return False

        return True

    def add_ship(self, ship):
        if ship.is_vertical:
            for i in range(ship.ship_pos[1], ship.ship_pos[1] + ship.ship_size):
                self.board_state[i][ship.ship_pos[0]] = ship

        else:
            for i in range(ship.ship_pos[0], ship.ship_pos[0] + ship.ship_size):
                self.board_state[ship.ship_pos[1]][i] = ship

    def draw_board(self, battle=False):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if battle:
                    if self.board_state[i][j] in ['0', 'X', 'M']:
                        print(self.board_state[i][j], end="")
                    else:
                        print('0', end="")

                else:
                    if self.board_state[i][j] in ['0', 'X', '@']:
                        print(self.board_state[i][j], end="")
                    elif self.board_state[i][j] == 'M':
                        print('0', end="")
                    else:
                        print('@', end="")
            print("\n")


class Ship:
    def __init__(self, ship_size: int, ship_type: str, ship_segments, ship_pos, is_vertical: bool):
        self.is_vertical = is_vertical
        self.ship_size = ship_size
        self.ship_type = ship_type
        self.ship_segments = ship_segments
        self.ship_pos = ship_pos

    def hit(self, hit_pos):
        if self.is_vertical:
            self.ship_segments[hit_pos[1] - self.ship_pos[1]] = False
        else:
            self.ship_segments[hit_pos[0] - self.ship_pos[0]] = False

        return not (True in self.ship_segments)


class Game:
    def __init__(self, b_size=10):
        self.b_size = b_size

    def game_on(self):
        game_on = True
        player_list = [Player('Player 2'), Player('Player 1')]
        board_list = [Board(self.b_size, [['0' for _ in range(self.b_size)] for _ in range(self.b_size)]),
                      Board(self.b_size, [['0' for _ in range(self.b_size)] for _ in range(self.b_size)])]

        player_1_turn = bool(random.randint(0, 1))
        vessels = {'0': ['aircraft carrier', 1, 5]}
        # , '1': ['destroyer', 2, 4],
        # '2': ['submarine', 2, 3], '3': ['escort ship', 2, 2]
        num_of_ships = []
        len_of_ships = []

        for j in vessels.items():
            for k in range(j[1][1]):
                num_of_ships.append(j[1][0])
                len_of_ships.append(j[1][2])

        board_list[player_1_turn].draw_board()

        while True:
            print(f'{player_list[player_1_turn].player_name} place your vessels.')

            for i in range(len(num_of_ships)):
                while True:
                    try:
                        print(f"place your {num_of_ships[i]}: ")
                        pos = [int(input('x: ')), int(input('y: '))]
                        is_vertical = input('vertical placement (y/n): ').lower() == 'y'

                        if board_list[player_1_turn].check(pos, is_vertical, len_of_ships[i]):
                            print("ok")
                            player_list[player_1_turn].add_ship(
                                Ship(len_of_ships[i], num_of_ships[i], ([True] * len_of_ships[i]), pos, is_vertical))
                            board_list[player_1_turn].add_ship(player_list[player_1_turn].player_ships[i])
                            board_list[player_1_turn].draw_board()
                            break
                        else:
                            print('change coordinates')

                    except Exception as e:
                        print(f"error - {e}")

                    if len(player_list[player_1_turn].player_ships) == len(num_of_ships):
                        break

            player_1_turn = not player_1_turn

            if len(player_list[0].player_ships) == len(num_of_ships) and len(player_list[1].player_ships) == len(
                    num_of_ships):
                break

        while game_on:
            p_shot = player_list[player_1_turn].move()
            e_ship = board_list[not player_1_turn].board_state[p_shot[1]][p_shot[0]]

            board_list[not player_1_turn].draw_board(True)
            if e_ship not in ['0', 'X', 'M']:
                if e_ship.hit(p_shot):
                    player_list[not player_1_turn].remove_ship(e_ship)

                board_list[not player_1_turn].board_state[p_shot[1]][p_shot[0]] = 'X'

                if player_list[not player_1_turn].lose_condition():
                    game_on = False
                    print(f"{player_list[player_1_turn].player_name} has won!")
                else:
                    print('shoot again!')
            else:
                print('miss')
                if e_ship not in ['X', 'M']:
                    board_list[not player_1_turn].board_state[p_shot[1]][p_shot[0]] = 'M'
                player_1_turn = not player_1_turn


game = Game()
game.game_on()
