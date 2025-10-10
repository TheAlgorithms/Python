// Prim's Algorithm - Minimum Spanning Tree (MST)
// Language: C++
// Category: Greedy Algorithms

#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

void primMST(int V, vector<vector<pair<int, int>>> &adj) {
    vector<int> key(V, INT_MAX);
    vector<int> parent(V, -1);
    vector<bool> inMST(V, false);

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    // Start from vertex 0
    key[0] = 0;
    pq.push({0, 0});

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        inMST[u] = true;

        for (auto &[v, weight] : adj[u]) {
            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                pq.push({key[v], v});
                parent[v] = u;
            }
        }
    }

    cout << "Edges in MST:\n";
    int totalWeight = 0;
    for (int i = 1; i < V; ++i) {
        cout << parent[i] << " - " << i << " (" << key[i] << ")\n";
        totalWeight += key[i];
    }
    cout << "Total Weight = " << totalWeight << endl;
}

int main() {
    int V, E;
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;

    vector<vector<pair<int, int>>> adj(V);
    cout << "Enter edges (u v w):\n";
    for (int i = 0; i < E; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    primMST(V, adj);

    return 0;
}
