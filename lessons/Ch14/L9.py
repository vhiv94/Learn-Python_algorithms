from lessons.Ch14.graph import Graph


run_cases = [
    (
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        [6, 7],
    ),
    (
        [
            (1, 2),
            (1, 3),
        ],
        [0, 4],
    ),
]
submit_cases = run_cases + [
    (
        [
            (0, 5),
            (7, 0),
        ],
        [1, 2, 3, 4],
    )
]


def test(edges_to_add, expected_vertices):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    for node in expected_vertices:
        graph.add_node(node)
        print(f"Added unconnected node: {node}")
    print("---------------------------------")
    try:
        unconnected = graph.unconnected_vertices()
        print(f" - Expecting: {expected_vertices}")
        print(f" - Actual: {unconnected}")
        if unconnected == expected_vertices:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False