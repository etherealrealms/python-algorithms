from search.binarySearch import BinarySearch
from generators.power_set.exponential import PowerSetExponential
from sort.selectionSort import SelectionSort
from sort.mergeSort import MergeSort


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
            MergeSort
        ]
    )

