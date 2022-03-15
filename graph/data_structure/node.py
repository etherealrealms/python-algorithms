class Node(object):
    node_count = 0

    def __init__(self, name='unknown'):
        self._name = name
        self._id = Node.node_count
        Node.node_count += 1

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        return f'[Node (id: {self.get_id()}): {self.get_name()}]'
