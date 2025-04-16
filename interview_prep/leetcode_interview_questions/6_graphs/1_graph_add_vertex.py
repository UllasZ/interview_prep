class Graph:

    def __init__(self):
        self.adj_self = {}

    def print_graph(self):
        print("\n" + "-" * 100)
        print("Graph (Adjacency List): ")

        if not self.adj_self:
            print(None)
        for key, value in self.adj_self.items():
            print(key + " :", value)

        print("-" * 100)

    def add_vertex(self, vertex):
        if vertex not in self.adj_self.keys():
            self.adj_self[vertex] = []
            return True
        return False


# Instantiate graph
graph = Graph()

# add_vertex
graph.add_vertex("A")

# print_graph
graph.print_graph()
