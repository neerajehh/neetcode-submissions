class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1 : 
            return False 
        m = []
        for i in range(n): 
            m.append([])
        for edge in edges: 
            u = edge[0]
            v = edge[1]
            m[u].append(v)
            m[v].append(u)
        visited = set()
        queue = []
        visited.add(0)
        queue.append(0)
        while queue: 
            current = queue.pop(0)
            for neighbors in m[current]: 
                if neighbors not in visited: 
                    visited.add(neighbors)
                    queue.append(neighbors)
        return len(visited) == n 

                


