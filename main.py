from search.binarySearch import BinarySearch
from generators.power_set.exponential import PowerSetExponential
from sort.selectionSort import SelectionSort
from sort.mergeSort import MergeSort
from hashTables.hashTable import HashTable
from dynamic.fibonacci import Fibonacci
from graph.dfs import DepthFirstSearch
from graph.bfs import BreadthFirstSearch
from graph.binaryTree import BinaryTree

from simulation.simulationRunner import SimulationRunner


def test_algorithms(algorithm_classes):
    for algorithm_class in algorithm_classes:
        algorithm = algorithm_class()
        algorithm.test()


if __name__ == '__main__':
    test_algorithms(
        [
            BinarySearch,
            PowerSetExponential,
            SelectionSort,
            MergeSort,
            HashTable,
            Fibonacci,
            DepthFirstSearch,
            BreadthFirstSearch,
            SimulationRunner,
            BinaryTree,
        ]
    )

