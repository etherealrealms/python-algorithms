from .edge import Edge

class DirectedGraph(object):
    def __init__(self):
        self._nodes = {}
        self._edges = {}

    def has_node(self, node):
        return not self._nodes.get(node.get_id) is None

    def add_node(self, node):
        node_id = node.get_id()
        self._nodes[node_id] = node

        if self._edges.get(node_id) is None:
            self._edges[node_id] = []

    def add_edge(self, edge):
        source_node = edge.get_source_node()
        destination_node = edge.get_destination_node()

        if not self.has_node(source_node):
            self.add_node(source_node)

        if not self.has_node(destination_node):
            self.add_node(destination_node)

        self._edges[source_node.get_id()].append(destination_node.get_id())

    def get_node_with_id(self, node_id):
        return self._nodes.get(node_id)

    def get_direct_children_of_node(self, node):
        node_children = []
        node_id = node.get_id()

        if self.has_node(node) is None:
            raise RuntimeError(f'{str(node)} is not in the graph!')

        for node_id in self._edges[node_id]:
            node_children.append(self.get_node_with_id(node_id))

        return node_children

    def __str__(self):
        graph_str_representation = ''

        for (source_node_id, destination_node_ids) in self._edges.items():
            source_node = self.get_node_with_id(source_node_id)

            for destination_node_id in destination_node_ids:
                destination_node = self.get_node_with_id(destination_node_id)
                graph_str_representation += str(Edge(source_node, destination_node))

        return graph_str_representation
