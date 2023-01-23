def main():
    from graphnet.edge import Edge
    from graphnet.node import Node
    from graphnet.network import GraphNetwork

    # create nodes
    node0 = Node()
    node1 = Node()

    # create edge
    edge0 = Edge()

    # link nodes with edge
    node0.add_edge(edge0, target=node1)

    # create graph network
    network = GraphNetwork(nodes=[node0, node1])


if __name__ == "__main__":
    main()
