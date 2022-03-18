from algorithm.Algorithm import Algorithm
from .data_structure.directed import DirectedGraph


class DepthFirstSearch(Algorithm):
    graph_counter = 0

    def __init__(self):
        Algorithm.__init__(self)

        self._test_data = [
            {
                'nodes': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                'edges': [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('D', 'G')]
            },
        ]
        self._visited_nodes = {}

    def is_visited_node(self, node):
        return not self._visited_nodes.get(node.get_name()) is None

    def dfs(self, root_node, graph):
        self._visited_nodes = {}
        stack = [root_node.get_name()]
        exploration_str = f'Graph: {str(graph)}\n\n'

        while len(stack) > 0:
            node_name = stack.pop()
            node = graph.get_node_with_name(node_name)

            if not self.is_visited_node(node):
                self._number_of_executions += 1
                self._visited_nodes[node_name] = node

                if root_node == node:
                    exploration_str += f'{str(node)} [root_node]  ---->\n'
                else:
                    exploration_str += f'{str(node)}  ----> '

                children_nodes = graph.get_direct_children_of_node(node)

                for child_node in children_nodes:
                    self._number_of_executions += 1
                    if not self.is_visited_node(child_node):
                        stack.append(child_node.get_name())

                if len(children_nodes) == 0:
                    exploration_str = exploration_str + '[end of branch]\n'

        exploration_str += '[complete]'
        return exploration_str

    def exec_test(self, iteration, test_datum):
        graph = DirectedGraph(test_datum['nodes'], test_datum['edges'])
        return self.dfs(graph.get_node_with_name(test_datum['nodes'][0]), graph)


