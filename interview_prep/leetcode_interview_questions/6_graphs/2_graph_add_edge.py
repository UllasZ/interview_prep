class Graph:

    def __init__(self):
        self.adj_self = {}

    def print_graph(self):
        print("\n" + "-" * 100)
        print("Graph (Adjacency List): ")

        if not self.adj_self:
            print(None)
        for key, value in self.adj_self.items():
            print(key, ":", value)

        print("-" * 100)

    def add_vertex(self, vertex):
        if vertex not in self.adj_self.keys():
            self.adj_self[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):

        if v1 in self.adj_self.keys() and v2 in self.adj_self.keys():
            self.adj_self[v1].append(v2)
            self.adj_self[v2].append(v1)
            return True
        return False


# Instantiate graph
graph = Graph()

# add_vertex
graph.add_vertex(1)
graph.add_vertex(2)

# add_edge
graph.add_edge(1, 2)

# print_graph
graph.print_graph()
