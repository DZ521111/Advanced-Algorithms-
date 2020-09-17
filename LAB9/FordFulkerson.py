# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:40:06 2020

@author: DHRUV
"""
from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)
 
    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * (self.rows)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.rows)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


graph = [[0, 92, 0, 102, 100, 0],
         [0, 89, 100, 0, 154, 0],
         [0, 0, 100, 0, 91, 100],
         [0, 87, 0, 90, 45, 100],
         [0, 40, 100, 100, 0, 100],
         [0, 0, 200, 0, 275, 0],
         [0, 32, 56, 98, 0, 0]]

g = Graph(graph)

source = 1
sink = 5

print(f"Max Flow between {source} to {sink} is : {g.ford_fulkerson(source, sink)}")