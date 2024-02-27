def no_of_graphs(vertices: int):
    ## no of edges for given n vertices would be: n*(n-1)/2 (undirected graph)
    edges = vertices * (vertices - 1) / 2
    return pow(2, edges)


if __name__ == "__main__":
    vertices = input("Enter no of vertices")
    vertices = int(vertices)
    graphs = no_of_graphs(vertices)
    print(f"possible graphs for {vertices} vertices are {graphs}:")
