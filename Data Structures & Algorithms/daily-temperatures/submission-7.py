class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n 
        stack = []
        for i in range(n): 
            todays_temp = temperatures[i]
            while len(stack) > 0 : 
                top_index = stack[-1]
                top_temperature = temperatures[top_index]
                if todays_temp>top_temperature: 
                    stack.pop()
                    res[top_index] = i-top_index
                else: 
                    break 
            stack.append(i)
        return res         