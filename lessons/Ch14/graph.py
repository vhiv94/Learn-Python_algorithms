class Matrix:
    def __init__(self, num_vertices: int) -> None:
        if type(num_vertices) is not int or num_vertices <= 0:
            raise ValueError("the number of vertices for a graph must be a possitive integer")
        self.__num_vertices: int = num_vertices
        self.matrix: list[list[bool]] = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int) -> None:
        if u < 0 or u >= self.__num_vertices or v < 0 or v >= self.__num_vertices:
            return
        self.matrix[u][v] = True
        self.matrix[v][u] = True

    # edge_exists() provided by boot.dev
    def edge_exists(self, u: int, v: int) -> bool:
        if u < 0 or u >= len(self.matrix):
            return False
        if len(self.matrix) == 0:
            return False
        row1 = self.matrix[0]
        if v < 0 or v >= len(row1):
            return False
        return self.matrix[u][v]

    def __repr__(self) -> str:
        rep = ""
        for row in self.matrix:
            rep += f"{row}\n"
        return rep
    
class Graph:
    def __init__(self, num_vertices: int | None = None) -> None:
        self.graph: dict[int, set] = dict()
        self.__num_vertices: int = 0
        if num_vertices:
            self.add_vertices(num_vertices)

    # def add_edge(self, u: int, v: int) -> None:
    #     if type(u) is not int or u < 0 or type(v) is not int or v < 0:
    #         raise ValueError("Vertices must be positive integers")
    #     if u >= self.__num_vertices or v >= self.__num_vertices:
    #         self.add_vertices(max(u, v) + 1) 
    #     self.graph[u].add(v)
    #     self.graph[v].add(u)

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

    def add_node(self, u):
        if u not in self.graph:
            self.graph[u] = set()

    def add_vertices(self, num_vertices: int) -> None:
        if type(num_vertices) is not int or num_vertices <= 0:
            raise ValueError("the number of vertices for a graph must be a possitive integer")
        for i in range(self.__num_vertices, num_vertices):
            self.graph.setdefault(i, set())
        self.__num_vertices = num_vertices

    def adjacent_nodes(self, node: int) -> set:
        if node < 0 or node not in self.graph:
            raise ValueError("node does not yet exist")
        return self.graph[node]

    def edge_exists(self, u: int, v: int) -> bool:
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
    
    def unconnected_vertices(self) -> list[int]:
        return list(map(lambda item: item[0], filter(lambda item: not item[1], self.graph.items())))

    def __repr__(self) -> str:
        rep = "{\n"
        for key, val in self.graph.items():
            rep += f"  {key}: {val or '{}'},\n"
        rep += "}"
        return rep

grph = Graph(3)
grph.add_edge(2, 3)
grph.unconnected_vertices()
print(grph)