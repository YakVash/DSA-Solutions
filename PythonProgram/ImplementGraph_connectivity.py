class Graph :
     
    def __init__(self) :

        self.graph = {} # Dictionary for adjacency list

    # Add edge between two vertices
    def add_edge(self, u, v) :

        # For undirected graph, add both ways
        if u not in self.graph :

            self.graph[u] = []

        if v not in self.graph :

            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Display the graph
    def display(self) :

        print("\nGraph Representation (Adjacency List):")

        for node in self.graph :

            print(node, "->", self.graph[node])

    # DFS to visit all connected nodes
    def dfs(self, start, visited) :

        visited.add(start)

        for neighbour in self.graph[start] :

            if neighbour not in visited :

                self.dfs(neighbour, visited)

    # Check if the graph is connected
    def is_connected(self) :

        if not self.graph :

            return True
        
        visited = set()
        start_node = next(iter(self.graph)) # pick any node
        self.dfs(start_node, visited)
        return len(visited) == len(self.graph)
    
# --------------------------
# Main Program
# --------------------------
g = Graph()

# Add edges (connections)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

#g.add_edge('F', 'G') # Uncomment this to make graph disconnected
# Display the graph
g.display()

# Check connectivity
if g.is_connected() :
 
 print("\nThe graph is Connected ✅")

else :
 
 print("\nThe graph is Disconnected ❌")
