# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:29:50 2019

@author: manum
"""

from collections import defaultdict


class Graph(object):
    def __init__(self,no_of_vertices):
        self.graph = defaultdict(list)
        self.V = no_of_vertices  #No of vertices added to the graph
    #Function to add edge between two nodes/vertices in a graph
    def addEdge(self,vertex1,vertex2):
        self.graph[vertex1].append(vertex2)
    
    
    #Recursive Toplpological sort
    def recursiveTopologicalSort(self,v,visited,stack):
        visited[v] = True #marking current node
        #going through all the adjacent nodes/vertices of the current node/vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.recursiveTopologicalSort(i,visited,stack)
        
        stack.insert(0,v)
    
    def topologicalSort(self):
        visited = [False] * self.V
        stack = list()
        
        
        for i in range(self.V):
            if not visited[i]:
                self.recursiveTopologicalSort(i,visited,stack)
        return stack
if __name__=="__main__":
    #Test case
    g = Graph(6) 
    g.addEdge(5, 2); 
    g.addEdge(5, 0); 
    g.addEdge(4, 0); 
    g.addEdge(4, 1); 
    g.addEdge(2, 3); 
    g.addEdge(3, 1); 
    print(g.topologicalSort())
        
        
        