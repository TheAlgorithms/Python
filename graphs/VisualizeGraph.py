import networkx as nx
import matplotlib.pyplot as plt


# For tutorial of networkx visit https://networkx.org/documentation/latest/tutorial.html



def undirected_visualize_from_adjmat(adjmat):
    size = len(adjmat)

    # Create a graph object
    G = nx.Graph()

    for i in range(size):
        for j in range(size):
            if adjmat[i][j] != 0:
                # Add edge to the graph object
                G.add_edge(i, j, weight=adjmat[i][j])


    # Specify the layout of graph
    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 10))
    
    # Draw the vertices
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', alpha=0.9)
    
    # Draw the edges
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray')
    
    # Draw the Vertices Labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_family='sans-serif')

    # Draw the weights of edges
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=10)

    plt.title("Undirected Graph Visualization", size=15)
    plt.axis('off')
    plt.show()




def directed_visualize_from_adjmat(adjmat):
    size = len(adjmat)

    # Create a Digraph object
    G = nx.DiGraph()

    for i in range(size):
        for j in range(size):
            if adjmat[i][j] != 0:
                # Add edges to the graph object
                G.add_edge(i, j, weight=adjmat[i][j])

    # Specify the layout to use while plotting the graph 
    pos = nx.spring_layout(G)

    plt.figure(figsize=(10, 10))
    
    # Draw the vertices
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', alpha=0.9)
    
    # Draw the labels for vertices
    nx.draw_networkx_edges(G, pos,arrowstyle='-|>', arrowsize=30, width=2, alpha=0.5, edge_color='gray')
    
    # Draw the weights
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black', font_family='sans-serif')

    # Draw the weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black', font_size=10)

    plt.title("Directed Graph Visualization", size=15)
    plt.axis('off')
    plt.show()


def visualize_from_adjmat(adjmat,isdirected):
    if isdirected:
        directed_visualize_from_adjmat(adjmat)
    else:
        undirected_visualize_from_adjmat(adjmat)




def edges_to_adjacency_matrix(vertex_count, edge_count, is_directed):
    '''
    Takes input in form of edges and convert it to adjacency matrix.
    '''

    adjacency_matrix = [[0] * vertex_count for _ in range(vertex_count)]
    for _ in range(edge_count):
        u, v, weight = map(int, input().split())
        adjacency_matrix[u][v] = weight
        if not is_directed:
            adjacency_matrix[v][u] = weight
    return adjacency_matrix

def matinput(vertex_count, edge_count, is_directed):
    '''
    Takes input in form of adjacency matrix and convert it to adjacency matrix.
    '''

    adjacency_matrix = []
    print("Enter the adjacency matrix row by row:")
    for _ in range(vertex_count):
        row = list(map(int, input().split()))
        adjacency_matrix.append(row)
    return adjacency_matrix

def list_to_adjacency_matrix(vertex_count, edge_count, is_directed):
    '''
    Takes input in form of adjacency list and convert it to adjacency matrix.
    '''

    adjacency_matrix = [[0] * vertex_count for _ in range(vertex_count)]
    print("Enter the adjacency list:")
    for u in range(vertex_count):
        print("Neighbours of ",u,end=": ")
        neighbours = input().split()
        for neigh in neighbours:
            v,weight = map(int,neigh.split(','))
            adjacency_matrix[u][v] = weight
            if not is_directed:
                adjacency_matrix[v][u] = weight
    return adjacency_matrix


def main():
    vertex_count = int(input("Enter the number of vertices: "))
    edge_count = int(input("Enter the number of edges: "))
    is_directed = int(input("Is the graph Directed?? 1 or 0 :"))

    print("Enter the type of input:")
    print("1: Edge List")
    print("2: Adjacency Matrix")
    print("3: Adjacency List")
    input_type = int(input())

    if input_type == 1:
        print("The expected input is of the form u v w where w is the weight.")
        adjacency_matrix = edges_to_adjacency_matrix(vertex_count, edge_count, is_directed)
    elif input_type == 2:
        print("Expected input is of the form V columns and V rows with the weights of the edges.")
        adjacency_matrix = matinput(vertex_count, edge_count, is_directed)
    elif input_type == 3:
        print("Expected input is of the form for neighbour vertex v,w")
        adjacency_matrix = list_to_adjacency_matrix(vertex_count, edge_count, is_directed)
    else:
        print("Enter valid input.")
        return

    visualize_from_adjmat(adjacency_matrix, is_directed)

if __name__ == "__main__":
    main()



'''
Example Inputs:

1) Edge List:

The expected input is of the form u v w where w is the weight.
0 1 1
0 2 1
0 3 1
3 1 1
3 2 1

2) Adj Mat:

Expected input is of the form V columns and V rows with the weights of the edges.
Enter the adjacency matrix row by row:
0 1 1 1
1 0 0 1
1 0 0 1
1 1 1 0

3) Adj List:
Expected input is of the form for neighbour vertex v,w
Enter the adjacency list:
Neighbours of  0: 1,2 2,3 3,-3
Neighbours of  1: 2,3
Neighbours of  2: 3,-3
Neighbours of  3: 

'''