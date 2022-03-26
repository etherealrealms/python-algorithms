from .diceRoll import DiceRoll
from .simulation import Simulation


class SameNumberDiceOccurrenceSimulation(Simulation):
    def __init__(self):
        Simulation.__init__(self)
        self._dice = DiceRoll()

    def simulate(self):
        return self._dice.simulate()
