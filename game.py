import random


class Game:
    def __init__(self, words):
        self.words: list = list(set(words))
        random.shuffle(self.words)
        self.current_player = 0
        self.players = []
        self.round_count = 0

        self.initiate_players()

    def initiate_players(self):
        num_of_players = int(input('Number of players: '))

        for i in range(num_of_players):
            self.players.append(Player())

        self.current_player = int(input(f'Pick current player out of {dict(enumerate(self.players))}: '))

    def game(self):
        try:
            while True:
                score = {i: i.points for i in self.players}
                print(f'Score: {score}')

                word = [self.words.pop() for i in range(3)]

                print(f'Round {self.round_count}, {self.players[self.current_player]} reads "{word}"')

                keyboard = input(f'Input answerer from {dict(enumerate(self.players))}: ')

                if len(self.words) == 0:
                    raise KeyboardInterrupt

                if keyboard != '':
                    self.players[int(keyboard)].points += 1
                    self.players[self.current_player].points += 1
                    self.current_player = int(keyboard)
                    self.round_count += 1

        except KeyboardInterrupt:
            print('Final score:')
            score = {i: i.points for i in self.players}
            print(f'{score}')


class Player:
    def __init__(self):
        self.name = input('Input name: ')
        self.points = 0

    def __repr__(self):
        return self.name


def import_file(file) -> list:
    f = open(file)

    words = []

    for i in f.readlines():
        if '\t' in i:
            words.append(i.split('\t')[0])

    return words
