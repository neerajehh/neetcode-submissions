class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        rows = len(grid)
        cols = len(grid[0])
        islands = 0 
        seen = set()
        def bfs(r,c):
             q = deque()
             seen.add((r,c))
             q.append((r,c))
             while q: 
                row,col = q.popleft()
                drns = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in drns: 
                    if (0<=dr+row<rows and 0<=dc+col<cols and grid[dr+row][dc+col] =="1" and (dr+row,dc+col) not in seen): 
                        q.append((dr+row,dc+col))
                        seen.add((dr+row,dc+col))
                       


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1" and (r,c) not in seen: 
                    islands+=1
                    bfs(r,c)
        return islands