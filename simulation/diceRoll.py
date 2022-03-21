import random
from .simulation import Simulation


class DiceRoll(Simulation):
    def __init__(self):
        Simulation.__init__(self)
        self.min_discrete_value = 1
        self.max_discrete_value = 6
        self.possible_discrete_values = list(range(self.min_discrete_value, self.max_discrete_value + 1))

    def simulate(self):
        return random.choice(self.possible_discrete_values)

