class Graph:
    def __init__(self, num_vertices: int) -> None:
        if type(num_vertices) is not int or num_vertices <= 0:
            raise ValueError("the number of vertices for a graph must be a possitive integer")
        self.__num_vertices: int = num_vertices
        self.graph: list[list[bool]] = [[False for n in range(num_vertices)] for n in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        if u < 0 or u >= self.__num_vertices or v < 0 or v >= self.__num_vertices:
            return
        self.graph[u][v] = True
        self.graph[v][u] = True

    # edge_exists() provided by boot.dev
    def edge_exists(self, u: int, v: int) -> bool:
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

    def __repr__(self) -> str:
        rep = ""
        for row in self.graph:
            rep += f"{row}\n"
        return rep

grph = Graph(4)
grph.add_edge(3, 3)
print(grph)