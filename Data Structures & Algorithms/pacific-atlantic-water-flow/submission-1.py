class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      if not heights : 
         return []
      result = []
      rows = len(heights)
      cols = len(heights[0])
      def bfs(r,c,visited ) : 
         queue = [[r,c]]
         visited.add((r,c))
         while queue: 
            recent = queue.pop(0)
            row  = recent[0]
            col = recent[1]
            directions =  [[1,0],[-1,0],[0,1],[0,-1]]
            for dirs in directions: 
               dr = dirs[0]
               dc = dirs[1]
               nr = dr + row 
               nc = dc + col 
               if 0<=nr<rows and 0<=nc<cols and  (nr,nc) not in visited and heights[nr][nc]>=heights[row][col]:
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
      for r in range(rows):
         for c in range(cols):
            if (r,c) in pacific and (r,c) in atlantic : 
               result.append([r,c])
      return result 
