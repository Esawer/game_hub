import requests


class Player:
    def __init__(self, player_name: str, player_score=0):
        self.player_name = player_name
        self.player_score = player_score

    def move(self):
        while True:
            letter = input("letter: ")

            if len(letter) == 1:
                return letter
            else:
                print("another try")


class Board:
    def __init__(self, b_word: str, b_state: str):
        self.b_word = b_word
        self.b_state = b_state

    def __str__(self):
        return self.b_state

    def change(self, letter):
        for i in range(len(self.b_state)):
            if self.b_word[i] == letter and self.b_state[i] == '*':
                self.b_state = list(self.b_state)
                self.b_state[i] = letter
                self.b_state = "".join(self.b_state)
                return True
        else:
            return False

    def check_win(self):
        return self.b_word == self.b_state


class Game:
    def __init__(self, num_of_players: int):
        self.num_of_players = num_of_players

    def game_on(self):
        game_on = True
        player_list = []
        tries = 10

        for i in range(self.num_of_players):
            player_list.append(Player(f'Player {i}'))

        while True:

            try:

                url = 'https://random-word-api.herokuapp.com/word?number=1'
                data = requests.get(url)

                if data.status_code == 200:
                    data = data.json()

                    if len(data[0]) >= 5:
                        board = Board(data[0], '*' * len(data[0]))
                        break

            except Exception as e:
                print(f"error - {e}")

        while game_on:

            if tries > 0:
                for i in range(len(player_list)):
                    print(f"\n{player_list[i].player_name} try: ")
                    print(board)

                    if board.change(player_list[i].move()):
                        print(board)
                    else:
                        print("bad luck buddy")
                        tries -= 1

                    if board.check_win():
                        game_on = False
                        print("fin")
                        break

            else:
                game_on = False
                print("game over")


game = Game(2)
game.game_on()
