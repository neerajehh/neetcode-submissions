class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
     if not grid: 
        return 0 
     islands = 0 
     rows = len(grid)
     cols = len(grid[0])
     def bfs(r,c): 
        grid[r][c] = '0'
        queue = [(r,c)]
        while queue: 
            current = queue.pop(0)
            nr = current[0]
            nc = current[1]
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for x in directions: 
                dr = nr + x[0]
                dc = nc+x[1]
                if 0<=dr<rows and 0<=dc<cols and grid[dr][dc] == "1": 
                    queue.append((dr,dc))
                    grid[dr][dc] = '0'
     for r in range(rows): 
        for c in range(cols) : 
            if grid[r][c] == '1':
             islands+=1 
             bfs(r,c)
     return islands 
            
