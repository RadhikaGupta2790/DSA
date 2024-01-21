from enum import Enum

class Color(Enum):
    WHITE = 0   # Not visited
    GRAY = 1    # Visited but in the current DFS path
    BLACK = 2   # Visited and not in the current DFS path

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, directed=True):
        if directed:
            if source not in self.graph:
                self.graph[source] = []
            self.graph[source].append(destination)
            if destination not in self.graph:
                self.graph[destination] = []
        else:
            if source not in self.graph:
                self.graph[source] = []
            self.graph[source].append(destination)

            if destination not in self.graph:
                self.graph[destination] = []
            self.graph[destination].append(source)

    def is_cyclic_util(self, node, colors):
        colors[node] = Color.GRAY  # Mark the current node as being in the current DFS path

        for neighbor in self.graph.get(node, []):
            if colors[neighbor] == Color.GRAY:
                return True  # Cycle detected
            elif colors[neighbor] == Color.WHITE:
                if self.is_cyclic_util(neighbor, colors):
                    return True  # Recursively check the neighbor

        colors[node] = Color.BLACK  # Mark the current node as visited and not in the current DFS path
        return False

    def is_cyclic(self):
        colors = {node: Color.WHITE for node in self.graph}

        for node in self.graph:
            if colors[node] == Color.WHITE:
                if self.is_cyclic_util(node, colors):
                    return True  # Cycle detected

        return False  # No cycle found

# Example usage:
graph = Graph()

# Example usage for directed graph 1:
directed_edges = [(1, 2), (2, 3), (3, 4), (4, 2), (2, 1)]
for edge in directed_edges:
    graph.add_edge(edge[0], edge[1], directed=True)

# Check if the directed graph 1 is cyclic
is_cyclic_directed_1 = graph.is_cyclic()
print(f"Is directed graph 1 cyclic? {is_cyclic_directed_1}")

# Example usage for directed graph 2:
graph = Graph()
directed_edges_2 = [(1, 2), (5, 3), (5, 4), (4, 2), (2, 3)]
for edge in directed_edges_2:
    graph.add_edge(edge[0], edge[1], directed=True)

# Check if the directed graph 2 is cyclic
is_cyclic_directed_2 = graph.is_cyclic()
print(f"Is directed graph 2 cyclic? {is_cyclic_directed_2}")

# Example usage for undirected graph 1:
graph = Graph()
undirected_edges = [(1, 2), (2, 3), (3, 4), (4, 2), (2, 1)]
for edge in undirected_edges:
    graph.add_edge(edge[0], edge[1], directed=False)

# Check if the undirected graph 1 is cyclic
is_cyclic_undirected_1 = graph.is_cyclic()
print(f"Is undirected graph 1 cyclic? {is_cyclic_undirected_1}")

# Example usage for undirected graph 2:
graph = Graph()
undirected_edges_2 = [(1, 2), (5, 3), (5, 4), (4, 2), (2, 3)]
for edge in undirected_edges_2:
    graph.add_edge(edge[0], edge[1], directed=False)

# Check if the undirected graph 2 is cyclic
is_cyclic_undirected_2 = graph.is_cyclic()
print(f"Is undirected graph 2 cyclic? {is_cyclic_undirected_2}")
