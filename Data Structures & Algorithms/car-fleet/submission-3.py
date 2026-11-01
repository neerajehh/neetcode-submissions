class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        res = []
        n = len(position)
        for i in range(n): 
            res.append([position[i],speed[i]])
        res.sort() #O(nlogn)
        for i in range(n-1,-1,-1): 
            time = (target - res[i][0]) / res[i][1]
            stack.append(time)
            if len(stack) >=2 : 
                if stack[-1]<=stack[-2]:
                     stack.pop()
        return len(stack)


        