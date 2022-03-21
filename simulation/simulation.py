import random
from datetime import datetime


class Simulation(object):
    def __init__(self):
        self.random_seed = datetime.now().timestamp()
        random.seed(self.random_seed)

    def simulate(self):
        pass
