from collections import Counter
import random


class Game(object):

    def __init__(self, matches=10, mistakes_probability=0):
        if not isinstance(matches, int):
            raise TypeError('matches must be an integer')
        self._matches = matches
        self._mistakes_probability = mistakes_probability
        self._registry = Counter()
        self._score_map = {
            ('Cooperate', 'Cooperate'): (2, 2),
            ('Cheat', 'Cheat'): (0, 0),
            ('Cheat', 'Cooperate'): (3, -1),
            ('Cooperate', 'Cheat'): (-1, 3)
        }

    def play(self, player1, player2):
        for _ in range(self._matches):
            move1 = player1.move(player2)
            move2 = player2.move(player1)

            if random.random() <= self._mistakes_probability:
                move1 = 'Cheat' if move1 == 'Cooperate' else 'Cooperate'
            if random.random() <= self._mistakes_probability:
                move2 = 'Cheat' if move2 == 'Cooperate' else 'Cooperate'

            player1_score, player2_score = self._score_map[(move1, move2)]
            self._registry[player1] += player1_score
            self._registry[player2] += player2_score

            player1.update_state()
            player2.update_state()

        player1.reset()
        player2.reset()

    def top3(self):
        for player, score in self._registry.most_common(3):
            print(player, score)
