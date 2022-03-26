from algorithm.Algorithm import Algorithm
from .sameNumberDiceOccurrenceSimulation import SameNumberDiceOccurrenceSimulation
from .approximateAreaOfCircle import ApproximateAreaOfCircle


class SimulationRunner(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self._test_data = [
            SameNumberDiceOccurrenceSimulation(),
            ApproximateAreaOfCircle()
        ]

    def exec_test(self, iteration, simulation_object):
        simulation_run = simulation_object.run()
        self._number_of_executions = simulation_run['number_of_trials'] * simulation_run['number_of_runs_per_trial']
        return simulation_run

