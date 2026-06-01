class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 :
            return False 
        graph =[]
        for i in range (n) : 
            graph.append([])
        for edge in edges:
           u = edge[0]
           v=edge[1]
           graph[u].append(v)
           graph[v].append(u)
        visited = set()
        queue = []
        queue.append(0)
        visited.add(0)
        while queue:
         node = queue.pop(0)
         for neighbour in graph[node]:
          if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
        return len(visited) == n 