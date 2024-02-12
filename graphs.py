"""
This file consists of the Python Implementation of Graph and its various methods.
@author: Mateen Sofi
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"Vertex: {vertex}, Connections: {self.adj_list[vertex]}")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


# Create a graph and add a few vertices
print("Creating a graph and adding data to it")
my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')
my_graph.add_vertex('E')
my_graph.add_vertex('F')

# Connect the graph using edges
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'F')
my_graph.add_edge('B', 'D')
my_graph.add_edge('D', 'F')
my_graph.add_edge('C', 'F')

# Print the graph
my_graph.print_graph()

# Remove an edge to check if remove function works
print("\nAfter removing edge between C and F")
my_graph.remove_edge('C', 'F')

# Print the graph
my_graph.print_graph()
