from random import randint
from algorithm.Algorithm import Algorithm

max_number_of_nodes = 100


def generate_list_of_randomized_int(number_of_ints):
    randomized_ints = []

    for i in range(0, number_of_ints):
        randomized_ints.append(randint(0, max_number_of_nodes))

    return randomized_ints


class Heap(Algorithm):
    def __init__(self):
        Algorithm.__init__(self)
        self.nodes = []
        self._test_data = [
            generate_list_of_randomized_int(100),
        ]

    def parent_index(self, i):
        node_length = len(self.nodes)
        proposed_index = (i - 1) // 2
        return proposed_index if proposed_index < node_length else None

    def left_child_index(self, i):
        node_length = len(self.nodes)
        proposed_index = (2 * i) + 1
        return proposed_index if proposed_index < node_length else None

    def right_child_index(self, i):
        node_length = len(self.nodes)
        proposed_index = 2 * (i + 1)
        return proposed_index if proposed_index < node_length else None

    def insert(self, value):
        self.nodes.append(value)
        new_node_index = len(self.nodes) - 1

        new_node_parent_index = self.parent_index(new_node_index)

        while new_node_index > 0 and self.nodes[new_node_index] > self.nodes[new_node_parent_index]:
            self.nodes[new_node_parent_index], self.nodes[new_node_index] = (
                self.nodes[new_node_index], self.nodes[new_node_parent_index]
            )
            new_node_index = self.parent_index(new_node_index)
            new_node_parent_index = self.parent_index(new_node_index)

    def get_greater_child_index(self, node_index):
        right_child_index = self.right_child_index(node_index)
        left_child_index = self.left_child_index(node_index)
        current_node = self.nodes[node_index]

        if right_child_index is not None and self.nodes[right_child_index] > current_node:
            return right_child_index
        elif left_child_index is not None and self.nodes[left_child_index] > current_node:
            return left_child_index

        return 0

    def delete(self):
        if len(self.nodes) == 0:
            return None

        last_node = self.nodes.pop()
        root_node = self.nodes[0]
        self.nodes[0] = last_node
        trickle_node_index = 0

        while True:
            greater_child_index = self.get_greater_child_index(trickle_node_index)

            if greater_child_index == 0:
                break

            self.nodes[greater_child_index], self.nodes[trickle_node_index] = (
                self.nodes[trickle_node_index], self.nodes[greater_child_index]
            )
            trickle_node_index = greater_child_index

        return root_node

    def exec_test(self, iteration, test_datum):
        print(f'Inserting {len(self._test_data[iteration])} items into the heap...\n')

        for node_value in test_datum:
            print(f'Inserting {node_value}...')
            self.insert(node_value)

        print(f'Node List: {self.nodes}\n')

        number_of_nodes = len(self.nodes)

        for i in range(0, number_of_nodes):
            deleted_node = self.delete()
            print(f'Deleted node: {deleted_node}')

