from game import Game
from players import *

from itertools import combinations

if __name__ == '__main__':
    num_matches = 10
    game = Game(matches=num_matches, mistakes_probability=0)
    players = [Cooperator(), Cheater(), Copycat(), Grudger(), Detective(), CopyKitten()]

    player_pairs = combinations(players, 2)
    for player1, player2 in player_pairs:
        game.play(player1, player2)

    game.top3()
