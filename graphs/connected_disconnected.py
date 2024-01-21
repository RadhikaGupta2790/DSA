from enum import Enum

class Color(Enum):
    WHITE = 0   # Not visited
    GRAY = 1    # Visited but in the current DFS path
    BLACK = 2   # Visited and not in the current DFS path

class Graph:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed

    def add_edge(self, source, destination):
        if self.directed:
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

    def is_cyclic(self):
        if not self.graph:
            return False  # An empty graph is considered acyclic
    
        colors = {node: Color.WHITE for node in self.graph}
        
        for node in self.graph:
            if colors[node] == Color.WHITE:
                if self.is_cyclic_util(node, colors, parent=None):
                    return True  # Cycle detected
    
        return False  # No cycle found
    
    def is_cyclic_util(self, node, colors, parent):
        colors[node] = Color.GRAY  # Mark the current node as being in the current DFS path
    
        for neighbor in self.graph.get(node, []):
            if colors[neighbor] == Color.GRAY and neighbor != parent:
                return True  # Cycle detected
            elif colors[neighbor] == Color.WHITE:
                if self.is_cyclic_util(neighbor, colors, parent=node):
                    return True  # Recursively check the neighbor
    
        colors[node] = Color.BLACK  # Mark the current node as visited and not in the current DFS path
        return False

    def is_connected(self):
        if not self.graph:
            return True  # An empty graph is considered connected
    
        start_node = next(iter(self.graph))  # Pick any node as the starting point
    
        visited = set()
        self._dfs(start_node, visited)
    
        # If all nodes are visited, the graph is connected
        return len(visited) == len(self.graph)
    
    def _dfs(self, node, visited):
        visited.add(node)
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def print_graph(self):
        print("Graph:")
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(map(str, neighbors))}")
        print(f"Graph Type: {'Directed' if self.directed else 'Undirected'}")


# Example 1: Directed Cyclic, Connected
graph_example_1 = Graph(directed=True)
edges_example_1 = [(1, 2), (2, 3), (3, 4), (4, 2)]
for edge in edges_example_1:
    graph_example_1.add_edge(edge[0], edge[1])

print("Example 1:")
graph_example_1.print_graph()
print(f"Is the graph cyclic? {graph_example_1.is_cyclic()}")
print(f"Is the graph connected? {graph_example_1.is_connected()}\n")

# Example 2: Directed Acyclic, Disconnected
graph_example_2 = Graph(directed=True)
edges_example_2 = [(1, 2), (3, 4)]
for edge in edges_example_2:
    graph_example_2.add_edge(edge[0], edge[1])

print("Example 2:")
graph_example_2.print_graph()
print(f"Is the graph cyclic? {graph_example_2.is_cyclic()}")
print(f"Is the graph connected? {graph_example_2.is_connected()}\n")

# Example 3: Undirected Acyclic, Connected
graph_example_3 = Graph(directed=False)
edges_example_3 = [(1, 2), (2, 3), (3, 4)]
for edge in edges_example_3:
    graph_example_3.add_edge(edge[0], edge[1])

print("Example 3:")
graph_example_3.print_graph()
print(f"Is the graph cyclic? {graph_example_3.is_cyclic()}")
print(f"Is the graph connected? {graph_example_3.is_connected()}\n")

# Example 4: Undirected Acyclic, Disconnected
graph_example_4 = Graph(directed=False)
edges_example_4 = [(1, 2), (3, 4)]
for edge in edges_example_4:
    graph_example_4.add_edge(edge[0], edge[1])

print("Example 4:")
graph_example_4.print_graph()
print(f"Is the graph cyclic? {graph_example_4.is_cyclic()}")
print(f"Is the graph connected? {graph_example_4.is_connected()}\n")

# Example 5: Directed Cyclic, Disconnected
graph_example_5 = Graph(directed=True)
edges_example_5 = [(1, 2), (3, 4), (4, 5), (5, 3)]
for edge in edges_example_5:
    graph_example_5.add_edge(edge[0], edge[1])

print("Example 5:")
graph_example_5.print_graph()
print(f"Is the graph cyclic? {graph_example_5.is_cyclic()}")
print(f"Is the graph connected? {graph_example_5.is_connected()}\n")

# Example 6: Directed Acyclic, Connected
graph_example_6 = Graph(directed=True)
edges_example_6 = [(1, 2), (2, 3), (3, 4), (4, 5)]
for edge in edges_example_6:
    graph_example_6.add_edge(edge[0], edge[1])

print("Example 6:")
graph_example_6.print_graph()
print(f"Is the graph cyclic? {graph_example_6.is_cyclic()}")
print(f"Is the graph connected? {graph_example_6.is_connected()}\n")

# Example 7: Undirected Cyclic, Connected
graph_example_7 = Graph(directed=False)
edges_example_7 = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 2)]
for edge in edges_example_7:
    graph_example_7.add_edge(edge[0], edge[1])

print("Example 7:")
graph_example_7.print_graph()
print(f"Is the graph cyclic? {graph_example_7.is_cyclic()}")
print(f"Is the graph connected? {graph_example_7.is_connected()}\n")

# Example 8: Undirected Acyclic, Disconnected
graph_example_8 = Graph(directed=False)
edges_example_8 = [(1, 2), (3, 4), (5, 6)]
for edge in edges_example_8:
    graph_example_8.add_edge(edge[0], edge[1])

print("Example 8:")
graph_example_8.print_graph()
print(f"Is the graph cyclic? {graph_example_8.is_cyclic()}")
print(f"Is the graph connected? {graph_example_8.is_connected()}\n")
