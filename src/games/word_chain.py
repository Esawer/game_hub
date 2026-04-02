import random
import requests


class Board:
    def __init__(self, player_turn: str, word_chain: str):
        self.player_turn = player_turn
        self.word_chain = word_chain

    def change_turn(self, p_name: str):
        print(f"{p_name}'s turn.")

    def add_word(self, word: str):
        self.word_chain += word + " -> "


class Player:
    def __init__(self, player_score: int, player_name: str):
        self.player_score = player_score
        self.player_name = player_name

    def player_move(self):
        return input("word: ")


class Game:
    def __init__(self, words: list[str]):
        self.words = words

    def game_run(self):
        game_on = True
        first_game = True
        player_1_turn = bool(random.randint(0, 1))
        board = Board("", "")
        player_1 = Player(0, "Andrew")
        player_2 = Player(0, 'Bob')
        player_list = [player_2, player_1]

        while game_on:
            board.change_turn(player_list[int(player_1_turn)].player_name)

            while True:
                word = str(player_1.player_move() if player_1_turn else player_2.player_move())
                print(f"{board.word_chain}")
                url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
                data = requests.get(url)

                if (data.status_code == 200 and word not in self.words and first_game) or (
                        data.status_code == 200 and word not in self.words and word[0] == self.words[-1][
                    -1] and not first_game):
                    self.words.append(word)
                    board.add_word(word)
                    player_list[int(player_1_turn)].player_score += len(word)
                    player_1_turn = not player_1_turn
                    first_game = False
                    print(f"{player_1.player_name}; {player_1.player_score}")
                    print(f"{player_2.player_name}; {player_2.player_score}")
                    print(f"{board.word_chain}")
                    break
                else:
                    print("another word!")
                    continue


game = Game([])
game.game_run()
