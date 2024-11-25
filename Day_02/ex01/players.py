class Player:
    def __init__(self):
        self.moves_history = []
        self._current_move = None

    def __str__(self):
        return self.__class__.__name__

    def move(self, other):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def update_state(self):
        self.moves_history.append(self._current_move)

    def reset(self):
        self.moves_history = []
        self._current_move = None


class Cooperator(Player):
    def move(self, other):
        self._current_move = 'Cooperate'
        return self._current_move


class Cheater(Player):
    def move(self, other):
        self._current_move = 'Cheat'
        return self._current_move


class Copycat(Player):
    def move(self, other):
        if not self.moves_history:
            self._current_move = 'Cooperate'
        else:
            self._current_move = other.moves_history[-1]
        return self._current_move


class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.__cheater_detected = False

    def move(self, other):
        if 'Cheat' in other.moves_history:
            self.__cheater_detected = True

        self._current_move = 'Cheat' if self.__cheater_detected else 'Cooperate'
        return self._current_move

    def reset(self):
        super().reset()
        self.__cheater_detected = False


class Detective(Player):
    def __init__(self):
        super().__init__()
        self.__detective_strategy = ['Cooperate', 'Cheat', 'Cooperate', 'Cooperate']
        self.__cheater_detected = False

    def move(self, other):
        if self.__detective_strategy:
            self._current_move = self.__detective_strategy.pop(0)
        elif self.__cheater_detected:
            self._current_move = other.moves_history[-1]
        else:
            self._current_move = 'Cheat'

        if 'Cheat' in other.moves_history:
            self.__cheater_detected = True

        return self._current_move

    def reset(self):
        super().reset()
        self.__detective_strategy = ['Cooperate', 'Cheat', 'Cooperate', 'Cooperate']
        self.__cheater_detected = False


class Copykitten(Player):
    def move(self, other):
        if not self.moves_history:
            self._current_move = 'Cooperate'
        elif other.moves_history[-2:] == ['Cheat', 'Cheat']:
            self._current_move = 'Cheat'
        else:
            self._current_move = 'Cooperate'
        return self._current_move
