class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 : 
            return False 
        m = []
        for i in range(n) : 
            m.append([])
        for i in edges: 
            u = i[0]
            v= i[1]
            m[u].append(v)
            m[v].append(u)
        visited = set()
        queue = []
        queue.append(0)
        visited.add(0)
        while queue: 
            current = queue.pop(0)
            for neighbor in m[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return (len(visited)==n)
