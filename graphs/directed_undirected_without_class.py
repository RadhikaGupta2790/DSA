print("---------Directed Graph---------") 

def create_directed_graph(edges):
    graph = {}
    
    for edge in edges:
        source, destination = edge
        if source not in graph:
            graph[source] = []
        graph[source].append(destination)
    
    return graph

# Example usage for directed graph:
directed_edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (2, 1)]
directed_graph_representation = create_directed_graph(directed_edges)

# Displaying the directed graph
for node, neighbors in directed_graph_representation.items():
    print(f"Node {node}: Outgoing Edges {neighbors}")
    
print("---------Undirected Graph---------")    
    
def create_undirected_graph(edges):
    graph = {}
    
    for edge in edges:
        node1, node2 = edge
        # Adding node1 to node2's neighbors
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph[node1]:
            graph[node1].append(node2)
        
        # Adding node2 to node1's neighbors
        if node2 not in graph:
            graph[node2] = []
        if node1 not in graph[node2]:
            graph[node2].append(node1)
    
    return graph

# Example usage for undirected graph:
undirected_edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (2, 1)]
undirected_graph_representation = create_undirected_graph(undirected_edges)

# Displaying the undirected graph
for node, neighbors in undirected_graph_representation.items():
    print(f"Node {node}: Neighbors {neighbors}")



'''
o/p

---------Directed Graph---------
Node 1: Outgoing Edges [2, 3]
Node 2: Outgoing Edges [4, 1]
Node 3: Outgoing Edges [4]
Node 4: Outgoing Edges [5]
---------Undirected Graph---------
Node 1: Neighbors [2, 3]
Node 2: Neighbors [1, 4]
Node 3: Neighbors [1, 4]
Node 4: Neighbors [2, 3, 5]
Node 5: Neighbors [4]
'''
