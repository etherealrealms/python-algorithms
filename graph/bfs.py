from algorithm.Algorithm import Algorithm
from .data_structure.directed import DirectedGraph


class BreadthFirstSearch(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self._test_data = [
            {
                'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                'edges': [('A', 'B'), ('A', 'C'), ('B', 'D'), ('A', 'G'), ('B', 'H'), ('H', 'A'), ('C', 'E'), ('D', 'E'), ('D', 'F')]
            },
        ]
        self._visited_nodes = {}

    def is_visited_node(self, node):
        return not self._visited_nodes.get(node.get_name()) is None

    def bfs(self, root_node, graph):
        self._visited_nodes = {}
        queue = [root_node.get_name()]
        exploration_str = f'Graph: {str(graph)}\n\n'

        while len(queue) > 0:
            self._number_of_executions += 1
            node_name = queue.pop(0)
            node = graph.get_node_with_name(node_name)

            if root_node == node:
                self._visited_nodes[node_name] = node
                exploration_str += f'{str(node)} [root_node]  ---->\n'

            children_nodes = graph.get_direct_children_of_node(node)

            did_visit_children = False

            for child_node in children_nodes:
                self._number_of_executions += 1

                if not self.is_visited_node(child_node):
                    did_visit_children = True
                    child_node_name = child_node.get_name()
                    exploration_str += f'{str(child_node)}  ----> '
                    self._visited_nodes[child_node_name] = child_node
                    queue.append(child_node_name)

            if did_visit_children:
                exploration_str += '\n'

        exploration_str += '[complete]'
        return exploration_str

    def exec_test(self, iteration, test_datum):
        graph = DirectedGraph(test_datum['nodes'], test_datum['edges'])
        return self.bfs(graph.get_node_with_name(test_datum['nodes'][0]), graph)
