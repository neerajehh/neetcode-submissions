class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
     if not heights: 
        return []
     rows = len(heights)
     cols = len(heights[0])
     def bfs (r,c,visited): 
        queue=[[r,c]]
        visited.add((r,c))
        while queue:
            current = queue.pop(0)
            row = current[0]
            col = current[1]
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for x in directions: 
                dr=x[0]
                dc=x[1]
                nr= row + dr 
                nc= col+dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[row][col]: 
                  queue.append([nr,nc])  
                  visited.add((nr,nc)) 
     pacific = set()
     atlantic = set()
     for i in range(rows): 
        bfs(i,0,pacific)
     for x in range(cols): 
        bfs(0,x,pacific)
     for i in range(rows): 
        bfs(i,cols-1,atlantic)
     for x in range(cols): 
        bfs(rows-1,x,atlantic )
     result = []
     for r in range(rows) : 
        for c in range(cols) : 
            if (r,c) in atlantic and (r,c) in pacific:
                result.append([r,c])
     return result 
