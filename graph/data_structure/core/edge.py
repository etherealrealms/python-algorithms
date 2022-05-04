class Edge(object):
    edge_count = 0

    def __init__(self, node_source, node_destination, weight=None):
        self._source_node = node_source
        self._destination_node = node_destination
        self._weight = weight
        self._id = Edge.edge_count
        Edge.edge_count += 1

    def get_id(self):
        return self._id

    def get_source_node(self):
        return self._source_node

    def get_destination_node(self):
        return self._destination_node

    def get_weight(self):
        return self._weight
    
    def __str__(self):
        return f'{{{str(self.get_source_node())} ---weight [id: {self.get_id()}]: {self.get_weight()}---> {str(self.get_destination_node())}}}\n'
