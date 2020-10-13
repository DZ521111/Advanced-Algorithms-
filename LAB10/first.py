from collections import defaultdict 

class Graph: 
	def __init__(self, vertices):  
		self.V = vertices  
		self.graph = defaultdict(list) 

	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	def MinVertexCover(self): 
		
		visited = [False] * (self.V)  
		for u in range(self.V): 
			if not visited[u]:  
				for v in self.graph[u]: 
					if not visited[v]:  
						visited[v] = True
						visited[u] = True
						break

		for j in range(self.V): 
			if visited[j]: 
				print(j, end = ' ') 
				
		print() 

if __name__ == "__main__":
    print("Enter the number of Vertex and Edges : - ")
    no_vertex, no_edges = map(int, input().split())
    g = Graph(no_vertex)
    print("Enter the Edges :- ") 
    for i in range(no_edges):
        u, v = map(int, input().split())
        g.addEdge(u, v) 

    g.MinVertexCover() 