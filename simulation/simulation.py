import random

from datetime import datetime
from .monteCarlo import MonteCarlo


class Simulation(object):
    def __init__(self, number_of_times_per_trial=100, number_of_trials=10000):
        self._trial_runner = MonteCarlo(number_of_times_per_trial, number_of_trials)
        self.random_seed = datetime.now().timestamp()
        random.seed(self.random_seed)

    def run(self):
        return self._trial_runner.run(self)

    def simulate(self):
        pass

