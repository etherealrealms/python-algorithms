from random import randint
from graph.data_structure.tree.treeNode import TreeNode
from algorithm.Algorithm import Algorithm

max_number_of_nodes = 1000
max_number_of_tests = 1


def generate_list_of_randomized_int(number_of_ints):
    randomized_ints = []

    for i in range(0, number_of_ints):
        randomized_ints.append(randint(0, max_number_of_nodes))

    return randomized_ints


class BinaryTree(Algorithm):
    def __init__(self, root_node=None):
        Algorithm.__init__(self)

        self._search_data = [
            generate_list_of_randomized_int(100),
        ]
        self._test_data = []
        self._test_count = 0
        self.root_node = root_node
        self.number_of_nodes = 0 if root_node is None else 1

    def insert(self, value, node=None):
        self.number_of_nodes += 1

        if self.root_node is None:
            self.root_node = TreeNode(value)
            return self.root_node

        current_node = node if node is not None else self.root_node

        current_node_value = current_node.value

        if value > current_node_value:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self.insert(value, current_node.right_child)
        elif value < current_node_value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self.insert(value, current_node.left_child)

    def return_next_greatest_node_of_deleted_node_sub_branch(self, node, node_to_delete):
        """
        Follow the node to delete all the way down its left branch to grab the least
        greatest value X of the node relative to the current node to delete
        :param node: TreeNode
        :param node_to_delete: TreeNode
        :return: TreeNode
        """
        self._number_of_executions += 1
        if node.left_child:
            node.left_child = self.return_next_greatest_node_of_deleted_node_sub_branch(node.left_child, node_to_delete)
            return node

        # Once we find this node delete the node by overwriting its value with X
        node_to_delete.value = node.value
        return node.right_child

    def delete(self, value, current_node):
        """
        Deletes the node in the tree and returns the node it has deleted or None if the node is not found in the tree
        :param value: TreeNode
        :param current_node:TreeNode
        :return: TreeNode
        """

        self._number_of_executions += 1
        if current_node is None:
            return current_node

        current_node_value = current_node.value

        if value > current_node_value:
            self.delete(value, current_node.right_child)
            return current_node
        elif value < current_node_value:
            self.delete(value, current_node.left_child)
            return current_node

        # the current node value must be == to the value and therefore is the one we wish to delete
        if current_node.left_child is None:
            return current_node.right_child
        elif current_node.right_child is None:
            return current_node.left_child

        # we have children in both the left and right child so we need to replace the nodes right child with the least
        # great node
        current_node.right_child = self.return_next_greatest_node_of_deleted_node_sub_branch(
            current_node.right_child, current_node
        )
        return current_node

    def is_empty(self):
        return self.root_node is None

    def search(self, search_value, tree_node):
        self._number_of_executions +=1

        if tree_node is None:
            return tree_node

        tree_node_value = tree_node.value

        if tree_node_value == search_value:
            return tree_node

        if search_value > tree_node_value:
            return self.search(search_value, tree_node.right_child)

        return self.search(search_value, tree_node.left_child)

    def generate_test_data(self):
        if self._test_count < max_number_of_tests:
            index = len(self._test_data)
            self._test_data.append([])

            self._test_data[index] = generate_list_of_randomized_int(max_number_of_nodes)

            self._test_count += 1
            yield self._test_data[index]

    def exec_test(self, iteration, test_datum):
        print(f'Insert {len(self._test_data[iteration])} items into the binary tree...\n')
        self.insert(max_number_of_nodes / 2)
        root_node = self.root_node

        for val in self._test_data[iteration]:
            self.insert(val)

        for search_datum in self._search_data[iteration]:
            self._number_of_executions = 0
            search_executions = 0
            string_response = f'\nSearching for {search_datum}: Value '

            val = self.search(search_datum, root_node)

            if val is None:
                string_response += 'not found!'
            else:
                search_executions = self.get_number_of_executions()
                string_response += f'found (in {search_executions} steps)! Now Deleting it!'
                successor_node = self.delete(search_datum, root_node)
                string_response += f' \nDeleted Node: {val}\nSuccessor Node: {successor_node}'

            print(string_response + f' (in {self.get_number_of_executions() - search_executions} steps)...\n')