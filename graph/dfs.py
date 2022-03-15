from algorithm.Algorithm import Algorithm
from .data_structure.directed import DirectedGraph


class DepthFirstSearch(Algorithm):
    graph_counter = 0

    def __init__(self):
        Algorithm.__init__(self)

        self._test_data = [
            {
                'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                'edges': [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F')]
            },
        ]

    def exec_test(self, iteration, test_datum):
        print(test_datum)
        return DirectedGraph(test_datum['nodes'], test_datum['edges'])


