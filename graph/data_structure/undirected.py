from .directed import DirectedGraph
from .edge import Edge


class UndirectedGraph(DirectedGraph):
    def add_edge(self, edge):
        DirectedGraph.add_edge(self, edge)
        # add the reverse edge to make the graph bidirectional
        DirectedGraph.add_edge(self, Edge(edge.get_destination_node(), edge.get_source_node()))
