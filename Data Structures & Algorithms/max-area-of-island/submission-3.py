class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0 
        seen = set()
        def bfs(r,c):
             q = deque()
             q.append((r,c))
             seen.add((r,c))
             area = 1 
             while q: 
                r,c = q.popleft()
                drns = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in drns:
                    if ((dr+r) in range(rows) and (dc+c) in range(cols) and (dr+r,dc+c) not in seen and grid[dr+r][dc+c] == 1): 
                        area+=1
                        q.append((dr+r,dc+c))
                        seen.add((dr+r,dc+c))
             return area


        for r in range(rows): 
            for c in range(cols):
                 if grid[r][c] == 1 and (r,c) not in seen: 
                    max_area = max(max_area,bfs(r,c))
        return max_area

    
        