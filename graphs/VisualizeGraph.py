import networkx as nx
import matplotlib.pyplot as plt
# https://networkx.org/documentation/latest/tutorial.html
# Link for tutorial


 
def visualize_graph_from_adjacency_matrix(adj_matrix):
    # Create an empty graph
    G = nx.Graph()

    # Add nodes and edges from adjacency matrix
    for i in range(len(adj_matrix)):
        for j in range(i, len(adj_matrix)):  # Iterate only over upper triangle for undirected graph
            if adj_matrix[i][j] > 0:  # There's an edge between node i and j
                G.add_edge(i, j, weight=adj_matrix[i][j])

    # Set up layout for the graph visualization
    pos = nx.spring_layout(G, seed=42)  # Spring layout for better visualization

    # Plot the graph
    plt.figure(figsize=(8, 8))
    
    # Draw the graph with node colors and edge colors
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray', width=2)

    # Optionally draw edge labels if the graph is weighted
    edge_labels = nx.get_edge_attributes(G, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Display the graph
    plt.title("Graph Visualization from Adjacency Matrix", size=15)
    plt.axis('off')
    plt.show()


def visualize(n):
    G = nx.Graph()

    # Add edges where i is divisible by j
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i % j == 0 and i != j:
                G.add_edge(i, j, weight=1)

    # Set up layout for better spacing between nodes
    pos = nx.spring_layout(G, seed=42)

    # Create a figure
    plt.figure(figsize=(10, 10))
    
    # Customize node colors with a color map
    node_colors = range(1, n + 1)
    cmap = plt.cm.viridis  # Use a color map (e.g., 'viridis', 'plasma')

    # Draw nodes with color mapping, size scaling
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=cmap, node_size=800)

    # Draw edges with custom width and transparency
    nx.draw_networkx_edges(G, pos, width=2.5, edge_color="slategrey")

    # Add labels to nodes with larger font size
    nx.draw_networkx_labels(G, pos, font_size=14, font_color="white", font_weight="bold")

    # Optionally draw edge labels (for weighted edges if applicable)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Add a title with larger font
    plt.title(f"Divisibility Graph Visualization (n = {n})", size=20, color="darkblue", pad=20)
    
    # Turn off the axis
    plt.axis("off")

    # Display the graph
    plt.show()


def condition(G,n):
    # Dynamically add edges where i is divisible by j, skip j=1 for clarity
    for i in range(1, n + 1):
        for j in range(2, n + 1):  # Skip j=1 to avoid self-loop-like behavior
            if i % j == 0 and i != j:
                G.add_edge(j, i, weight=1)  # Directed edge from j to i

def visualize_dag(n):
    G = nx.DiGraph()  # Create a directed graph (DAG)

    condition(G,n)    
    
    # Calculate the actual nodes included in the graph
    node_list = list(G.nodes())

    # Set up layout for better spacing between nodes
    pos = nx.spring_layout(G, seed=42)
    # pos = nx.circular_layout(G)
    # pos = nx.shell_layout(G)
    # pos = nx.random_layout(G)
    # pos = nx.kamada_kawai_layout(G)
    # pos = nx.planar_layout(G)
    # pos = nx.spectral_layout(G,seed = 42)
    # pos = nx.spiral_layout(G,seed = 42)
    # pos = nx.multipartite_layout(G,seed = 42)





    # Create a figure
    plt.figure(figsize=(10, 10))
    
    # Customize node colors with a color map
    node_colors = range(len(node_list))  # Range over dynamically created nodes
    cmap = plt.cm.viridis  # Use a color map (e.g., 'viridis', 'plasma')

    # Draw nodes with color mapping, size scaling
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, cmap=cmap, node_size=800)

    # Draw edges with arrows, custom width, and transparency
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2.5, edge_color="slategrey", arrows=True, arrowstyle='->', arrowsize=20)

    # Add labels to nodes with larger font size
    nx.draw_networkx_labels(G, pos, font_size=14, font_color="white", font_weight="bold")

    # Optionally draw edge labels (for weighted edges if applicable)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Add a title with larger font
    plt.title(f"DAG Visualization with Dynamic Nodes (n = {n})", size=20, color="darkblue", pad=20)
    
    # Turn off the axis
    plt.axis("off")

    # Display the graph
    plt.show()

# Visualize the DAG for a given n
# visualize_dag(12)












# Example adjacency matrix (unweighted graph)
adj_matrix = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

# Visualize the graph
# visualize_graph_from_adjacency_matrix(adj_matrix)



# Visualize the graph for a given n
# visualize(12)



# Visualize the DAG for a given n
visualize_dag(15)

    


