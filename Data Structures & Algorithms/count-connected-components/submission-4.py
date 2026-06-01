class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        def find(x): 
            if parents[x] != x:
               parents[x] = find(parents[x])
            return parents[x]
        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x !=root_y:
                parents[root_y] = root_x
                return True 
            return False 
        components = n 
        for a,b in edges: 
            if union(a,b):
             components -=1
        return components 