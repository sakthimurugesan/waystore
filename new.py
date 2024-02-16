from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = deque()

        queue.append(start)
        visited[start] = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Example usage with the given edges
obj = Graph()
obj.addEdge(0, 1)
obj.addEdge(0, 2)
obj.addEdge(1, 2)
obj.addEdge(2, 0)
obj.addEdge(2, 3)
obj.addEdge(3, 3)

# Starting BFS from vertex 2
print("BFS starting from vertex 2:")
obj.bfs(2)
