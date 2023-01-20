from typing import Container
from graphnet.node import Node
from graphnet.edge import Edge


def read_graph_network_from_xls(filepath: str):
    import pandas as pd
    from pathlib import Path

    filepath = Path(filepath)

    def pop_multiple(dict, keys):
        return (dict.pop(key) for key in keys)

    nodes = pd.read_excel(filepath, sheet_name="nodes")
    nodes = nodes.to_dict(orient="records")

    for node in nodes:
        plot_x = node.pop("plot_x")
        plot_y = node.pop("plot_y")
        node.update(plot={"xy": (plot_x, plot_y)})

    nodes = set(Node(**node) for node in nodes)

    # Edges
    edges_df = pd.read_excel(filepath, sheet_name="edges")
    edges_dict = edges_df.to_dict(orient="records")
    for edge in edges_dict:
        node_ids = set(pop_multiple(edge, ("node0", "node1")))
        nodes_filtered = filter(lambda node: node.id in node_ids, nodes)
        edge.update(nodes=set(nodes_filtered))

    edges = set(Edge(**edge) for edge in edges_dict)

    return GraphNetwork(nodes=nodes, edges=edges)


class GraphNetwork:
    def __init__(self, nodes: Container[Node], edges: Container[Edge] = None):

        self.nodes: set = set(nodes)

        if edges is None:
            self.edges: set = set(edge for node in nodes for edge in node.edges)
        else:
            self.edges = set(edges)

    def update(self, timestep):
        for node in self.nodes:
            node.update(timestep)

    @property
    def nodes_sorted(self):
        id_sort = lambda node: node.id
        return sorted(self.nodes, key=id_sort)
