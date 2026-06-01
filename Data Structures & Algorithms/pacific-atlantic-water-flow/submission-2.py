class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
     rows = len(heights)
     cols  = len(heights[0])
     results = []
   
     def bfs(r,c,visited): 
        queue = [(r,c)]
        visited.add((r,c)) 
        while queue: 
            current = queue.pop(0)
            cr = current[0]
            cc = current[1]
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dirs in directions: 
                nr = dirs[0] + cr 
                nc = dirs[1] + cc 
                if 0<=nr<rows  and 0<=nc<cols and (nr,nc) not in visited and heights[nr][nc]>=heights[cr][cc]: 
                    queue.append([nr,nc])
                    visited.add((nr,nc))
     pacific = set()
     atlantic = set()
     for i in range(rows): 
            bfs(i,0,pacific)
     for i in range(cols): 
            bfs(0,i,pacific)
     for i in range(rows): 
            bfs(i,cols-1,atlantic)
     for i in range(cols): 
            bfs(rows-1,i,atlantic)
     for r in range(rows) : 
        for c in range (cols) : 
               if ( r,c)  in pacific and (r,c) in atlantic : 
                results.append([r,c])
     return results 
 


        
                
