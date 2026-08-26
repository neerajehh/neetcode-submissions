class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n): 
            cars.append([position[i],speed[i]])
        cars.sort()
        stack = []
        for i in range(n-1,-1,-1): 
            pos = cars[i][0]
            speeds = cars[i][1]
            time = ((target - pos) / speeds)
            stack.append(time)
            if len(stack)>=2 : 
                if stack[-1]<=stack[-2]: 
                    stack.pop()
        return len(stack)
