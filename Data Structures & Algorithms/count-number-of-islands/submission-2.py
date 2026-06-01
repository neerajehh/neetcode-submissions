class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: 
            return 0 
        islands = 0 
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            grid[r][c] = '0'
            queue = [[r,c]]
            while queue: 
                current = queue.pop(0)
                row = current[0]
                col = current[1]
                dirns = [[1,0],[-1,0],[0,1],[0,-1]]
                for x in dirns: 
                    dr = x[0]
                    dc = x[1]
                    nr = row + dr
                    nc = col + dc 
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1':
                        queue.append([nr,nc])
                        grid[nr][nc] = '0'
        for r in range(rows) : 
                for c in range(cols) : 
                    if grid[r][c] =='1': 
                        islands+=1
                        bfs(r,c)
        return islands 
