class Graph:
    def __init__(self) -> None:
        self.graph: dict[str, set[str]] = {}

    def depth_first_search(self, start_vertex: str) -> list[str]:
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited: list[str], current_vertex: str) -> None:
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for city in neighbors:
            if city in visited:
                continue
            self.depth_first_search_r(visited, city)

    def breadth_first_search(self, v: str) -> list[str]:
        visited = []
        queue = [v]
        while queue:
            current = queue[0]
            del queue[0]
            visited.append(current)
            neighbors = sorted(self.graph[current])
            for city in neighbors:
                if city in visited or city in queue:
                    continue
                queue.append(city)
        return visited
        
    # courtesy of boot.dev

    def add_edge(self, u: str, v: str) -> None:
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self) -> str:
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result