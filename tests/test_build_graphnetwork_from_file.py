def test_build_graphnetwork_from_file():

    from graphnet.graph_network import read_graph_network_from_xls

    filepath = "tests\example_graph_network_input.xlsx"
    network = read_graph_network_from_xls(filepath)
