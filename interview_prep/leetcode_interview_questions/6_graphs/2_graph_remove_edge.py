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

    def remove_edge(self, v1, v2):
        if v1 in self.adj_self.keys() and v2 in self.adj_self.keys():
            try:
                self.adj_self[v1].remove(v2)
                self.adj_self[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False


# Instantiate graph
graph = Graph()

# add_vertex
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

# add_edge
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "A")

# print_graph
print("Before removing edge:")
graph.print_graph()

# remove edge
graph.remove_edge("A", "B")

# remove edge
graph.remove_edge("A", "D")

# print_graph
print("After removing edge:")
graph.print_graph()
