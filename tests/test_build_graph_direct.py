def test_build_graph_direct():

    from src.node import Node
    from src.edge import Edge
    from src.network import GraphNetwork

    # Create nodes
    node0 = Node()
    node1 = Node()
    node2 = Node()

    # Create edges
    path0 = Edge(nodes=set((node0, node1)))
    path1 = Edge(nodes=set((node1, node2)))
    path2 = Edge(nodes=set((node2, node0)))

    nodes = [node0, node1, node2]

    network = GraphNetwork(nodes=nodes)
    print(network.nodes_sorted)
