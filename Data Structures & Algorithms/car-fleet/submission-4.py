class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        stack = []
        for i in range(len(speed)): 
            res.append([position[i],speed[i]])
        res.sort()
        for i in range(len(position)-1,-1,-1): 
            time = ((target - res[i][0])  / res[i][1])
            stack.append(time)
            if len(stack)>=2: 
                if stack[-1]<=stack[-2]: 
                    stack.pop()
        return len(stack)




        