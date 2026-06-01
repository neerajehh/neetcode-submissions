class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        for i in range (numCourses) : 
            m[i]=[]
        for pre in prerequisites: 
            m[pre[0]].append(pre[1])
        visited = set()
        def cycle(courses) : 
            if courses in visited : 
                return True 
            if m[courses] == [] : 
                return False
        
            visited.add(courses)
            for x in m[courses]: 
             if cycle(x): 
              return True 
            visited.remove(courses)
            m[courses] = []
        for i in range(numCourses): 
            if cycle(i): 
                return False
        return True 

