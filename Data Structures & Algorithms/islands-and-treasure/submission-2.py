class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        rows = len(rooms)
        cols = len(rooms[0])
        q = deque()
        seen = set()
        def addroom(r,c): 
            if not r in range(rows) or not c in range(cols) or rooms[r][c] == -1 or (r,c) in seen: 
                return  
            seen.add((r,c))
            q.append([r,c])


        for r in range(rows): 
            for c in range(cols):
                 if rooms[r][c] == 0: 
                    q.append([r,c])
                    seen.add((r,c))
        
        dist = 0 
        while q: 
         for i in range(len(q)):
            r,c = q.popleft()
            rooms[r][c] = dist
            addroom(r+1,c)
            addroom(r-1,c)
            addroom(r,c+1)
            addroom(r,c-1)
         dist+=1
        