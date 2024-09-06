class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        graph = self.create_graph(n, edges)
        count_edges = 0
        for node in range(n):  # Loop over all nodes from 0 to n-1
            if node not in visited:
                size = self.explore(graph, node, visited)
                if size > 0:
                    count_edges += 1
        return count_edges

    def explore(self, graph, curr, visited):
        if curr in visited:
            return 0

        visited.add(curr)
        size = 1
        for neighbor in graph[curr]:
            size += self.explore(graph, neighbor, visited)
        return size
   
    

    def create_graph(self, n, edges):
        graph = {i: [] for i in range(n)}  # Ensure all nodes from 0 to n-1 are in the graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return graph