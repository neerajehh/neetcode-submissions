class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph ={}
        for i in range(numCourses): 
            graph[i] = []
        for pair in prerequisites : 
            graph[pair[0]].append(pair[1])
        visiting = set()
        def hasCycle(course):
            if course in visiting : 
                return True 
            if graph[course] == []: 
                return False
            visiting.add(course)
            for x in graph[course]: 
                if hasCycle(x): 
                    return True 
            visiting.remove(course)
            graph[course]=[]
            return False
        for course in range(numCourses): 
            if hasCycle(course):
                return False
        return True 