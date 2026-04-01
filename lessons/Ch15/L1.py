from lessons.Ch15.graph import Graph


run_cases = [
    (
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
        ],
        "New York",
        ["New York", "Cairo", "London", "Tokyo", "Dubai"],
    ),
]
submit_cases = run_cases + [
    (
        [
            ("New York", "London"),
            ("New York", "Cairo"),
            ("New York", "Tokyo"),
            ("London", "Dubai"),
            ("Cairo", "Kyiv"),
            ("Cairo", "Madrid"),
            ("London", "Madrid"),
            ("Buenos Aires", "New York"),
            ("Tokyo", "Buenos Aires"),
            ("Kyiv", "San Francisco"),
        ],
        "New York",
        [
            "New York",
            "Buenos Aires",
            "Cairo",
            "London",
            "Tokyo",
            "Kyiv",
            "Madrid",
            "Dubai",
            "San Francisco",
        ],
    ),
]


def test(edges_to_add, starting_at, expected_visited):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        bfs = graph.breadth_first_search(starting_at)
        for i, v in enumerate(bfs):
            print(f"Visiting:  {v}")
            print(f"Expected:  {expected_visited[i]}")

        if bfs == expected_visited:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False