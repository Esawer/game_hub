import copy
import random


class Game:
    def __init__(self, _classic_mode: bool):
        self._classic_mode = _classic_mode

    def game_run(self):
        game_on = True
        b_size = 5

        if not self._classic_mode:
            while True:
                try:
                    b_size = int(input("size: "))

                    if not 50 > b_size > 4:
                        print("Change the numer.")
                    else:
                        break

                except Exception as e:
                    print(f"Error - {e}")

        p_location = [random.randint(0, b_size - 1), random.randint(0, b_size - 1)]

        while True:
            k_location = [random.randint(0, b_size - 1), random.randint(0, b_size - 1)]

            if k_location[0] != p_location[0] + 1 and k_location[0] != p_location[0] - 1 and k_location[1] != \
                    p_location[1] - 1 and k_location[1] != p_location[1] + 1 and k_location != p_location:
                break

        board = Board(size=b_size, _key_location=k_location)
        player = Player(_player_location=p_location)

        while game_on:
            board.draw_board(player.player_location)
            old_pos = copy.copy(player.player_location)

            while True:
                try:
                    direction = int(input("top,right,bottom,left 1-4: "))

                    if 5 > direction > 0:
                        player.move(direction, b_size)
                        break

                except Exception as e:
                    print(f"Error - {e}")

            if player.player_location == board.key_location:
                print("hurrah - key found!")
                game_on = False
            else:
                d1 = abs(old_pos[0] - board.key_location[0]) + abs(old_pos[1] - board.key_location[1])
                d2 = abs(player.player_location[0] - board.key_location[0]) + abs(
                    player.player_location[1] - board.key_location[1])

                if d2 < d1:
                    print("ciepło")
                else:
                    print("zimno")


class Board:
    def __init__(self, size: int, _key_location: list[int]):
        self.size = size
        self._key_location = _key_location

    def draw_board(self, p_pos: list[int]):
        for i in range(self.size):
            for j in range(self.size):
                print(" # ", end="") if p_pos != [j, i] else print(" @ ", end="")
            print("\n")

    @property
    def key_location(self):
        return self._key_location


class Player:
    def __init__(self, _player_location: list[int]):
        self._player_location = _player_location

    def move(self, direction: int, size: int):
        size -= 1

        match direction:
            case 1:
                if self._player_location[1] > 0: self._player_location[1] -= 1

            case 2:
                if self._player_location[0] < size: self._player_location[0] += 1

            case 3:
                if self._player_location[1] < size: self._player_location[1] += 1

            case 4:
                if self._player_location[0] > 0: self._player_location[0] -= 1

            case default:
                print("you cannot move there!")

    @property
    def player_location(self):
        return self._player_location


game = Game(True)
game.game_run()
