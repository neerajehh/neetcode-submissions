class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        def find(x) : 
            if parent[x] != x: 
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y : 
                parent[root_x] = root_y
                return True
            return False
        components = n 
        for a,b in edges:
            if union(a,b):
                components -=1
        return components 
            